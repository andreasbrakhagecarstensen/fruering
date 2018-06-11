from django.db import models

# Create your models here.
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page

from .blocks import ArticleBlock


class ContentPage(Page):
    body = StreamField([
        ('article', ArticleBlock())
    ], blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]
