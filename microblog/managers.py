from django.db import models


class PostManager(models.Manager):
    def visible(self):
        return self.filter(is_visible=True)


class CategoryManager(models.Model):
    pass
