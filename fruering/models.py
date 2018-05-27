from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class RichTextPage(Page):
    body = RichTextField(blank=True, features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link'])

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
