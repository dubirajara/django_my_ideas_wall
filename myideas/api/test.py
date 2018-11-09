from django.shortcuts import resolve_url as r
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from myideas.core.models import Idea


class ApiTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = 'diego'
        self.email = 'test@djangoapp.com'
        self.password = 'test'
        self.user = User.objects.create_user(
            self.username, self.email, self.password
        )
        self.idea = Idea.objects.create(
            user=self.user, title='test app'
        )

        self.response = self.client.get(r('list_api'))
        self.client.login(username=self.username, password=self.password)

    def test_api_get(self):
        """GET 'Idea list api' must return status code 200"""
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)

    def test_api_create(self):
        """Check created data in db"""
        self.assertEqual(Idea.objects.count(), 1)

    def test_api_data(self):
        """check retrieve data in db"""
        self.assertEqual(Idea.objects.get().user.username, self.username)
        self.assertEqual(Idea.objects.get().title, 'test app')
        self.assertEqual(Idea.objects.get().user.email, self.email)

    def test_api_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

    def test_api_id_get(self):
        """GET 'Idea id list api' must return status code 200"""
        self.response.id = self.client.get(r('id_api', self.idea.id))
        self.assertEqual(status.HTTP_200_OK, self.response.id.status_code)

    def test_id_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

    def test_api_user_get(self):
        """GET 'Idea id list user' must return status code 200"""
        self.response.user = self.client.get(r('user_api', 'user?username=' + self.idea.user.username))
        self.assertEqual(status.HTTP_200_OK, self.response.user.status_code)
        username = Idea.objects.get().user.username
        if username is not None:
            self.assertEqual('diego', username)

    def test_user_html(self):
        """Test returns json contents"""
        contents = (self.idea.user.username, self.idea.likes.count(),
                    self.idea.title)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

    def test_post_idea(self):
        """POST 'Idea list api' must return status code 201"""
        response = self.client.post(r('list_api'),
                                    {'title': 'new idea', 'description': 'new idea', 'slug': 'idea'},
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Idea.objects.count(), 2)
        self.assertEqual(response.data.get('title'), 'new idea')

    def test_patch_idea(self):
        """PATCH 'Idea ID api' must return status code 200"""
        response = self.client.patch(r('id_api', self.idea.id),
                                     {'title': 'new idea NEW PATCH'},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Idea.objects.count(), 1)
        self.assertEqual(Idea.objects.get().title, 'new idea NEW PATCH')

    def test_put_idea(self):
        """PUT 'Idea ID api' must return status code 200"""
        response = self.client.put(r('id_api', self.idea.id),
                                   {'title': 'new idea NEW PUT', 'description': 'new idea', 'slug': 'idea'},
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Idea.objects.count(), 1)
        self.assertEqual(Idea.objects.get().title, 'new idea NEW PUT')

    def test_delete_idea(self):
        """DELETE 'Idea ID api' must return status code 200"""
        response = self.client.delete(r('id_api', self.idea.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Idea.objects.count(), 0)

    def test_logout_no_permissions(self):
        """If user not login and try create, update and delete must return status code 403"""
        self.client.logout()
        response = (
            self.client.post(r('list_api'),
                             {'title': 'new idea', 'description': 'new idea', 'slug': 'idea'},
                             format='json'),
            self.client.patch(r('id_api', self.idea.id),
                              {'title': 'new idea NEW PATCH'},
                              format='json'),
            self.client.put(r('id_api', self.idea.id),
                            {'title': 'new idea NEW PUT', 'description': 'new idea', 'slug': 'idea'},
                            format='json'),
            self.client.delete(r('id_api', self.idea.id)),
            )

        with self.subTest():
            for expected in response:
                self.assertEqual(expected.status_code, status.HTTP_403_FORBIDDEN)
