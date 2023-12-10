# signals.py

import os
from email.mime.image import MIMEImage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from .models import Produto, Subscriber

@receiver(post_save, sender=Produto)
def send_product_creation_email(sender, instance, created, **kwargs):
    if created:
        
        subject = 'Novo Produto Adicionado: {}'.format(instance.titulo_produto)
        message_html = render_to_string('email/newslatter.html', {'product': instance})
        plain_message = strip_tags(message_html)
        from_email = settings.DEFAULT_FROM_EMAIL

        # Criar instância do EmailMultiAlternatives
        email_message = EmailMultiAlternatives()
        email_message.subject = subject
        email_message.body = plain_message
        email_message.from_email = from_email

        # Adicionar versão HTML com a imagem incorporada
        email_message.attach_alternative(message_html, 'text/html')

        # Adicionar a imagem como MIMEImage
        with open(instance.imagem_produto.path, 'rb') as img_file:
            image = MIMEImage(img_file.read())
            image.add_header('Content-ID', f'<{instance.titulo_produto}_image>')
            email_message.attach(image)

        # Buscar assinantes no banco de dados
        assinantes = Subscriber.objects.values_list('email', flat=True)

        # Enviar e-mail para cada assinante
        for to_email in assinantes:
            email_message.to = [to_email]
            email_message.send()
