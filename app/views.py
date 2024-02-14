from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView
from app.models import *
from app.ser import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.request import Request

# Create your views here.
class TagPage(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagApi

class CatPage(ListAPIView):
    queryset = Cat.objects.all()
    serializer_class = CatApi

class AdPage(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdApi

class SubPage(CreateAPIView):
    queryset = Sub.objects.all().filter()
    serializer_class = SubApi

class AuthorPage(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorApi

class ContactPage(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContApi

class InfoPage(CreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = InfoApi

class CommPage(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ComApi

class PostPage(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi

class InstaPage(ListCreateAPIView):
    queryset = Insta.objects.all()
    serializer_class = InfoApi

class HomePostPage(ListAPIView):
    queryset = Post.objects.all()[0:6]
    serializer_class = PostApi


class DetailPostPage(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostApi


class PopularPostPage(ListAPIView):
    queryset = Post.objects.all()[0:4]
    serializer_class = PostApi


@api_view(http_method_names=['GET'])
def catS(req: Request,cat):
    db = Post.objects.all().filter(cat__name=cat)
    return Response({'posts':list(PostApi(db,many=True).data)})

@api_view(http_method_names=['GET'])
def nameS(req: Request,name):
    db = Post.objects.all().filter(title=name)
    return Response({'posts':list(PostApi(db,many=True).data)})

