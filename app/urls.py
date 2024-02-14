from django.urls import path
from app.views import *

urlpatterns = [
    path('', PostPage.as_view(), name='post'),
    path('det/<int:pk>', DetailPostPage.as_view(), name='detail'),
    path('home/', HomePostPage.as_view(), name='hom'),
    path('pop/', PopularPostPage.as_view(), name='pop'),
    path('tag/', TagPage.as_view(), name='tag'),
    path('cat/', CatPage.as_view(), name='cat'),
    path('com/', CommPage.as_view(), name='com'),
    path('contact/', ContactPage.as_view(), name='contact'),
    path('info/', InfoPage.as_view(), name='info'),
    path('insta/', InstaPage.as_view(), name='insta'),
    path('ad/', AdPage.as_view(), name='ad'),
    path('author/', AuthorPage.as_view(), name='author'),
    path('sub/', SubPage.as_view(), name='sub'),
    path('cat/<str:cat>/', catS, name='cat'),
    path('name/<str:name>/', nameS, name='name'),


]
