from django.db import models

class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Exchange(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='exchanges')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exchanges')
    date = models.DateTimeField(auto_now_add=True)
