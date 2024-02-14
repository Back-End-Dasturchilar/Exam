from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Sub(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.email
    
class Ad(models.Model):
    img = models.ImageField(upload_to='ad/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Insta(models.Model):
    img = models.ImageField(upload_to='insta/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Author(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    job = models.CharField(max_length=200)
    tw_link = models.URLField()
    git_link = models.URLField()
    fb_link = models.URLField()
    insta_link = models.URLField()
    img = models.ImageField(upload_to='author/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    cat = models.OneToOneField(Tag, on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to='post/')  
    ex_img = models.ImageField(upload_to='post_plus/') 
    tag = models.ManyToManyField(Tag,related_name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.title
    

class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200)
    post = models.ManyToManyField(Post,related_name='posts')
    msg = models.TextField()
    img = models.ImageField(upload_to='com/')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name
    

class ContactInfo(models.Model):
    addres = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.addres
    

class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.name