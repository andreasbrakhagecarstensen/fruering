from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from frueringcontent.blocks import ArticleStreamBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    subpage_types = ['blog.BlogPage']


class BlogPage(Page):
    date = models.DateField("Post date")
    header_image = models.ForeignKey('wagtailimages.Image',
                                        on_delete=models.SET_NULL,
                                        related_name='+',
                                        null=True,
                                        blank=True)

    body = StreamField(ArticleStreamBlock(), blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('header_image'),
        StreamFieldPanel('body')
    ]

    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []
