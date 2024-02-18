from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=200)

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class TagModels(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class PostModel(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='posts/')
    description = models.TextField()
    auther = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagModels, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CommentModels(models.Model):
    name = models.CharField(max_length=250)
    post_c = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    auther = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class ChangeBack(models.Model):
    back_img = models.ImageField(upload_to='back_img/', null=True, blank=True)
    auther = models.ForeignKey(UserModel, on_delete=models.CASCADE)