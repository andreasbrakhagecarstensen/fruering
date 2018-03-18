from wagtail.core.models import Page


class BasePage(Page):
    is_abstract = True
    menu_items = Page.objects.live().in_menu()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['menu_items'] = self.menu_items

        context['homepage'] = self.get_site_homepage()
        return context

    def get_site_homepage(self):
        return self.get_site().root_page

    class Meta:
        abstract = True
