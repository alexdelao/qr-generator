from django.db import models

# Create your models here.
class QRCode(models.Model):

    def path_to_qr(self, instance, filename):
        return f'qr_codes/{instance.id}/{filename}'

    url = models.URLField('Enlace')
    qr_image = models.ImageField(upload_to=path_to_qr)

    def __str__(self):
        return f'Es es el enlace {self.url}'