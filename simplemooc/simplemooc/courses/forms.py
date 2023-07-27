from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactCourse(forms.Form):

    name = forms.CharField(label= 'Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        label='Mensagem/Dúvida', widget=forms.Textarea
    )

    # Configurando o envio de emails pelo formulario
    def send_mail(self, courses):
        subject = '[%s] Contato' % courses
        message = 'Nome: %(name)s;Email: %(email)s;%(message)s'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message'],
        }
        message = message % context
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.CONTACT_EMAIL])

