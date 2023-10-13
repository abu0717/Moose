from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatar/')
    bio = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class PostModel(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='posts/')
    description = models.TextField()
    auther = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

