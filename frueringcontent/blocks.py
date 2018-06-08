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

    heading = CharBlock(template='frueringcontent/article/blocks/article_header_block.html')
    text = RichTextBlock(template='frueringcontent/article/blocks/article_text_block.html', features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link'])
    image = ImageChooserBlock(template='frueringcontent/article/blocks/article_image_block.html')

    class Meta:
        icon = 'placeholder'


class ArticleBlock(StructBlock):
    banner_image = ImageChooserBlock(required=False)
    article_title = CharBlock(required=True)
    article_body = ArticleStreamBlock()

    class Meta:
        template = 'frueringcontent/article/blocks/article_block.html'
