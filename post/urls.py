from django.contrib import admin
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.posts),
    path('<int:post_id>/', views.post_detail),
    re_path(r'^archive/(?P<year>\d{4})/$', views.post_archive),
    path('get_post/', views.get_post_handler),
    path('template_example/', views.template_test),
    path('<int:post_id>/', views.get_post_by_id),
    path('delete/<post_id>',views.delete_post,name='delete'),
]

    #re_path(r'^about/s/$', views.about), 
    #re_path(r'^g+/$', views.ggg),
    #re_path(r'^contact(?:s)?/$', views.contacts),
    #re_path(r'^archive/\d{4}/$', views.archive),
    #re_path(r'^archive_2/1[7-9]\d{2}/$', views.archive_2),
    #re_path(r'^group/[a-cA-C]\d{4}/$', views.group),
    #re_path(r'^home/', views.home_1), 