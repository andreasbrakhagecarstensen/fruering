from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from blog import blocks


class HomePage(Page):
    body = StreamField([
        ('blogroll', blocks.BlogIndexPageBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
