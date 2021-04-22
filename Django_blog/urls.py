from django.urls import path,include
from . import views
from .views import HomeView,PostView,CreatePostView,LikeView,UpdatePostView,DeletePostView,CreateCategoryView,CategoryView,CategoryListView,text_analysis,Post_Cards_View

urlpatterns = [
    #path('',views.home,name='home_link') #fuction view
    path('',HomeView.as_view(),name="home_link"),

    #showing single post by pk id!
    path('artical/<pk>',PostView.as_view(),name='post_link'),

    path('artical_cards_view/',Post_Cards_View.as_view(),name="cards_view"),
    
    path('create_post/',CreatePostView.as_view(),name="crate_post_link"),

    path('like/<int:pk>',LikeView, name='like_post'),

    path('create_category_post/',CreateCategoryView.as_view(),name="crate_category_link"),
    path('view_category/<str:cats>/',views.CategoryView,name="category_view_link"),
    path('view_category_lsit/',views.CategoryListView,name="category_view_list_link"),

    path('artical/update_post/<int:pk>',UpdatePostView.as_view(),name="update_post_view_link"),
    path('artical/<int:pk>/delete_post,',DeletePostView.as_view(),name="delete_post_link"),

    path('text_analysis/',views.text_analysis,name='analysis_link')

]
