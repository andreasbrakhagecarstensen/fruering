from wagtail.core import blocks
from wagtail.core.blocks import StructBlock

from .models import BlogPage


class BlogPageBlock(StructBlock):
    block_title = blocks.CharBlock(required=True, max_length=80)
    blog_page = blocks.PageChooserBlock(target_model=BlogPage)
    post_count = blocks.IntegerBlock(required=False,
                                     help_text="Number of post shown in this block. Default is 5. Max is 10.",
                                     min_value=1,
                                     max_value=10)
