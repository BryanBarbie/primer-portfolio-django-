from django.apps import AppConfig


class PortafolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portafolio'
    verbose_name: 'Portafolio'   #configuracion extendida para cambiar el nombre de la aplicacion en el sector admin
    
