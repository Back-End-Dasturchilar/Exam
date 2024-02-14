from rest_framework.serializers import ModelSerializer
from app.models import *




class TagApi(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CatApi(ModelSerializer):
    class Meta:
        model = Cat
        fields = '__all__'

class SubApi(ModelSerializer):
    class Meta:
        model = Sub
        fields = '__all__'
     
class InstaApi(ModelSerializer):
    class Meta:
        model = Insta
        fields = '__all__'

class AuthorApi(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AdApi(ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'

class ContApi(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class InfoApi(ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'

class PostApi(ModelSerializer):
    tag = TagApi
    cat = CatApi
    author = AuthorApi
    class Meta:
        model = Post
        fields = '__all__'

class ComApi(ModelSerializer):
    post = PostApi
    class Meta:
        model = Comment
        fields = '__all__'