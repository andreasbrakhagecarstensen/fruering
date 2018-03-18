from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from core.models import BasePage


class BlogIndexPage(BasePage):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = BasePage.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = ['blog.BlogPage']


class BlogPage(BasePage):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = BasePage.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname='full'),
    ]

    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []
