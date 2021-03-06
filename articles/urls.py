from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.FeedList.as_view(), name="feed_list"),
    path('<int:feed_pk>/', views.FeedDetail.as_view(), name="feed_detail"),
    path('<int:feed_pk>/comments/', views.FeedCommentList.as_view(), name="feed_comment_list"),
    path('<int:feed_pk>/comments/<int:comment_pk>/', views.FeedCommentDetail.as_view(), name="feed_comment_detail"),
    path('<int:feed_pk>/comments/<int:comment_pk>/like/', views.FeedCommentLike.as_view(), name="feed_comment_like"),
    path('<int:feed_pk>/comments/<int:comment_pk>/unlike/', views.FeedCommentUnLike.as_view(), name="feed_comment_unlike"),
    # path('<int:feed_pk>/likes/', views.FeedLikeUsers.as_view()),
    path('<int:feed_pk>/like/', views.FeedLike.as_view()),
    path('<int:feed_pk>/unlike/', views.FeedUnLike.as_view()),
    path('search', views.Search.as_view())
]