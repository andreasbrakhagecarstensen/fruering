from wagtail.core import blocks
from wagtail.core.blocks import StructBlock

from .models import BlogIndexPage


class BlogIndexPageBlock(StructBlock):
    block_title = blocks.CharBlock(required=True, max_length=80)
    blog_page = blocks.PageChooserBlock(target_model=BlogIndexPage)
    post_count = blocks.IntegerBlock(required=False,
                                     help_text="Number of post shown in this block. Default is 5. Max is 10.",
                                     min_value=1,
                                     max_value=10)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context)
        blogpages = value['blog_page'].get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    class Meta:
        template = 'blog/blocks/block_index_page_block.html'
        label = 'Blog roll'
