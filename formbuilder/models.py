from django.db import models
from django.db.models import CharField
from django.forms import widgets
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel, StreamFieldPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel

from formbuilder.widgets import FrueringRadio
from frueringcontent.blocks import ArticleStreamBlock


class FormField(AbstractFormField):
    page = ParentalKey('FormEmailPage', on_delete=models.CASCADE, related_name='form_fields')


class FormEmailPage(AbstractEmailForm):
    header_image = models.ForeignKey('wagtailimages.Image',
                                     on_delete=models.SET_NULL,
                                     related_name='+',
                                     null=True,
                                     blank=True)
    form_body = StreamField(ArticleStreamBlock(required=False), blank=True)
    submit_button_text = CharField(max_length=50, default='Send')
    thank_you_text = StreamField(ArticleStreamBlock(), blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        ImageChooserPanel('header_image'),
        StreamFieldPanel('form_body'),
        InlinePanel('form_fields', label='Form fields'),
        FieldPanel('submit_button_text', classname='full'),
        StreamFieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)

        for name, field in form.fields.items():
            if isinstance(field.widget, widgets.RadioSelect):
                field.widget = FrueringRadio(field.widget.attrs, field.widget.choices)
        return form
