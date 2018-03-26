/**
 * Created by diego on 14/3/17.
 */

    //# thanks the snippet video tutorial django likes: https://www.youtube.com/watch?v=pkPRtQf6oQ8

     $(document).ready(function(){
          function updateText(btn, newCount){
          btn.attr("data-likes", newCount)
          btn.html(newCount + " " + '<i class="fa fa-thumbs-up"></i>')
      }

      $(".like-btn").click(function(e){
        e.preventDefault()
        var this_ = $(this)
        var likeUrl = this_.attr("data-href")
        var likeCount = parseInt(this_.attr("data-likes")) | 0
        var addLike = likeCount + 1
        var removeLike = likeCount - 1
        if (likeUrl){
           $.ajax({
            url: likeUrl,
            method: "GET",
            data: {},
            success: function(data){
              console.log(data)
              var newLikes;
              if (data.liked){
                  updateText(this_, addLike)
              } else {
                  updateText(this_, removeLike)
                  // remove one like
              }

            }, error: function(error){
              console.log(error)
              console.log("error")
            }
          })
        }

      })
  })
