from django.db import models
from django.core.urlresolvers import reverse


class Student (models.Model):
    name = models.CharField(max_length = 100)
    created = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(blank=True)
    github_url = models.URLField(max_length=200)



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ("students:detail", kwargs={"id":self.pk})






