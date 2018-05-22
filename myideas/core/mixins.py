from django.shortcuts import get_object_or_404

from rest_framework.response import Response

from myideas.core.models import Ideas


class LikeIdeasMixin(object):
    def get(self, request, slug=None):
        obj = get_object_or_404(Ideas, slug=slug)
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)


# class TagsIdeasMixin(View):
#     def get(self, request, tags):
#         queryset = Ideas.objects.filter(tags=tags)
#
#         context = {
#             'queryset': queryset
#         }
#         return render(request, 'by_tags.html', context)
