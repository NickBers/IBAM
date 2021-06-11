from django.contrib import admin
from .models import Beca,Detail,Group,Orden,Student,Payment

# Register your models here.
class PostBeca(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class PostStudent(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id_alumno', 'name', 'lastname','group','beca')
class PostBeca(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class PostOrden(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
class PostPayment(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'created', 'details','student')


    
admin.site.register(Beca,PostBeca)
admin.site.register(Detail)
admin.site.register(Group)
admin.site.register(Orden,PostOrden)
admin.site.register(Student,PostStudent)
admin.site.register(Payment,PostPayment)

