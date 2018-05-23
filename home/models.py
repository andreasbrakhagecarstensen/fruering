from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import CharBlock, RichTextBlock

from blog import blocks


class HomePage(Page):
    body = StreamField([
        ('blogroll', blocks.BlogIndexPageBlock()),
        ('richtext_article', blocks.StructBlock(
            [
                ('header', CharBlock()),
                ('paragraph', RichTextBlock()),
            ],
            template='fruering/blocks/richtext_article_block.html'))
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
