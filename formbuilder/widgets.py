from django.forms import RadioSelect


class FrueringRadio(RadioSelect):
    template_name = 'formbuilder/widgets/radio.html'
