from django.contrib.admin import register , ModelAdmin
from .models import Khedmat , Nobat 


@register(Khedmat)
class KhedmatAdmin(ModelAdmin):
    list_display = [  #-----------------vaght namayesh in sooton ha ro ham neshoon mide
        'title', #----------------
        'price'
    ]
    
@register(Nobat)
class CopunAdmin(ModelAdmin):
    list_display = [  #-----------------vaght namayesh in sooton ha ro ham neshoon mide
    'bimar_name', 
    'khedmat_type',
    'date',
    'doctor',
    'pay_status' 
    ]

