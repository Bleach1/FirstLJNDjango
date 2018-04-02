from django.urls import path
from . import views

# 添加命名空间需要加上
app_name = 'LJNDjango'
urlpatterns = [
    path('ljnDjango/', views.index),
    path('article_ljn/', views.article_ljn),
    path('article_all/', views.article_all),
    path(r'edit_page/<int:article_id>', views.edit_page, name='edit_page'),
    path('edit_action/', views.edit_action, name='edit_action'),
    # https://blog.csdn.net/qq_40272386/article/details/78800507
    path(r'article_page/<int:article_id>', views.article_page, name='article_page'),
]
