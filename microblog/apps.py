from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MicroblogConfig(AppConfig):
    name = 'microblog'
    verbose_name = _('Blog')
