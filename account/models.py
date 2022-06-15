from django.db import models

class User(models.Model):
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    user_type = models.CharField(choices=(('A', 'Admin'), ('U', 'User')), max_length=1)
    blocked = models.BooleanField(default=False)

    def __str__(self):
        return self.login
        
    def __repr__(self) -> str:
        return super().__repr__()