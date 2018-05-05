from wagtail.core import hooks
from wagtail.core.models import Page, Site


@hooks.register('before_serve_page')
def add_menu_items(page, request, serve_args, serve_kwargs):
    page.menu_items = Page.objects.live().in_menu()
    page.home = Site.find_for_request(request).root_page
