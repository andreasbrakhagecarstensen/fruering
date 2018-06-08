from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, RichTextBlock

from blog import blocks
from frueringcontent.blocks import ArticleBlock


class HomePage(Page):
    body = StreamField([
        ('blogroll', blocks.BlogIndexPageBlock()),
        ('article', ArticleBlock())
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
