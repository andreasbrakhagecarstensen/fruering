from wagtail.core.blocks import StreamBlock, CharBlock, RichTextBlock, StructBlock

from django.conf import settings
from wagtail.images.blocks import ImageChooserBlock


class ArticleStreamBlock(StreamBlock):
    def __init__(self, **kwargs):
        if settings.FRUERING_CONTENT_ARTICLE_BLOCK_TYPES:
            local_blocks = []
            for block_type in settings.FRUERING_CONTENT_ARTICLE_BLOCK_TYPES:
                local_blocks.append(block_type())
            super().__init__(local_blocks=settings.FRUERING_CONTENT_ARTICLE_BLOCK_TYPES)
        else:
            super().__init__(local_blocks=None, **kwargs)

    heading = CharBlock()
    paragraph = RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link'])
    image = ImageChooserBlock()

    class Meta:
        icon = 'placeholder'


class ArticleBlock(StructBlock):
    banner_image = ImageChooserBlock()
    title = CharBlock(required=True)
    body = ArticleStreamBlock()

    class Meta:
        template = 'frueringcontent/article/article.html'
