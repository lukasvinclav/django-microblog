from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CategoryManager, PostManager


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    objects = CategoryManager()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        Category, verbose_name=_('Category'), null=True, default=None, blank=True, on_delete=models.SET_NULL
    )
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)
    preview = models.ImageField(_('preview'), blank=True)
    excerpt = models.TextField(_('excerpt'), blank=True)
    content = models.TextField(_('content'), blank=True)
    is_visible = models.BooleanField(_('visible'), default=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    objects = PostManager()

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-created']

    def __str__(self):
        return self.title
