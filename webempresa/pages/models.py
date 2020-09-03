from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = RichTextField(verbose_name='Contenido')
    order = models.SmallIntegerField(verbose_name='Orden', default=0)
    url = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name = 'Fecha de creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name = 'Ultima edicion')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['order', 'title']
    

    def __str__(self):
        return self.title

