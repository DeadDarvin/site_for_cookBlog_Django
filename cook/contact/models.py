from django.db import models
from ckeditor.fields import RichTextField


class ContactModel(models.Model):
    """ Класс модели обратной связи """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """ Класс модели контактов """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class AboutModel(models.Model):
    """ Модель для размещения в about """
    title = models.CharField(max_length=200)
    text = RichTextField()
    gen_image = models.ImageField(upload_to='about/', help_text='Главная картинка')
    second_image = models.ImageField(upload_to='about/', help_text='1 дополнительная картинка')
    third_image = models.ImageField(upload_to='about/', help_text='2 дополнительная картинка')

    def __str__(self):
        return self.title
