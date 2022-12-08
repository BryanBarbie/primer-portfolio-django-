from django.db import models

# Create your models here.

#modelo para formacion/course
class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    degree_title = models.CharField(max_length=150, verbose_name="Credencial", blank=True)
    link = models.URLField(max_length=180, blank=True,)
    description = models.TextField(verbose_name="Descripción") 
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField (auto_now=True, verbose_name="Fecha Modificacion")
    
    #pasos para convertir en español la aplicacion en el admin
    class Meta:
        verbose_name= 'formacion'
        verbose_name_plural = 'formaciones'
        ordering = ['-created']
    
    #para que muestre el titulo como link para acceder desde el admin
    def __str__(self):
        return self.title

#modelo para conocimientos/skills
class Skill(models.Model):
    title = models.CharField(max_length=80, verbose_name="Titulo")
    image = models.ImageField(upload_to= 'skills', verbose_name="Imagen")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField (auto_now=True, verbose_name="Fecha Modificacion")
    
    #pasos para convertir en español la aplicacion en el admin
    class Meta:
        verbose_name= 'Conocimiento'
        verbose_name_plural = 'Conocimientos'
        ordering = ['-created']
    
    #para que muestre el titulo como link para acceder desde el admin
    def __str__(self):
        return self.title
    