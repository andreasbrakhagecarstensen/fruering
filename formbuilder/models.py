from django.db import models
from django.db.models import CharField
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.core.fields import RichTextField


class FormField(AbstractFormField):
    page = ParentalKey('FormEmailPage', on_delete=models.CASCADE, related_name='form_fields')


class FormEmailPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    form_section_header = CharField(max_length=50, blank=True)
    submit_button_text = CharField(max_length=50, default='Send')
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname='full'),
        FieldPanel('form_section_header', classname='title full'),
        InlinePanel('form_fields', label='Form fields'),
        FieldPanel('submit_button_text', classname='full'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]