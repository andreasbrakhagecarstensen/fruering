from wagtail.core.models import Page


class BasePage(Page):
    is_abstract = True
    menu_items = Page.objects.live().in_menu()

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        context['menu_items'] = self.menu_items

        homepage = self.get_root()
        context['homepage'] = homepage
        return context

    class Meta:
        abstract = True
