from django.db import models
from django.utils.timezone import now

# Create your models here.
class Beca(models.Model):
    nombre_beca=models.CharField(max_length=200, verbose_name="nombre de beca")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "Beca"
        verbose_name_plural = "Becas"
        ordering = ["-created"]

    def __str__(self):
        return (self.nombre_beca)

class Group(models.Model):
    name_group=models.CharField(max_length=200,verbose_name="Nombre_grup")
    grado=models.CharField(max_length=200,verbose_name="Grado")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "Grupo"
        verbose_name_plural = "Grupos"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s' % (self.name_group, self.grado)


class Student(models.Model):
    id_alumno=models.BigAutoField(primary_key=True, verbose_name="Matricula")
    name=models.CharField(max_length=200, verbose_name="Nombre")
    lastname=models.CharField(max_length=200, verbose_name="Apellidos")
    adress=models.CharField(max_length=200,verbose_name="Direccion")
    phoneNumber=models.CharField(max_length=200,verbose_name="Numero Telefonico")
    email=models.CharField(max_length=200,verbose_name="Correo")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    beca=models.ForeignKey(Beca,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s' % (self.name, self.lastname)



class Detail(models.Model):
    num_referencia=models.CharField(max_length=200, verbose_name="Numero Referencia")
    tipe_pay=models.CharField(max_length=200, verbose_name="Tipo de Pago")
    amount=models.FloatField()
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    class Meta:
        verbose_name = "Detalle"
        verbose_name_plural = "Detalles"
        ordering = ["-created"]

    def __str__(self):
        return '%s %s %s' % (self.num_referencia,self.tipe_pay, self.amount)


class Payment(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    details=models.ForeignKey(Detail,on_delete=models.CASCADE,verbose_name="Delles del pago")
    student=models.ForeignKey(Student, on_delete=models.CASCADE,verbose_name="Alumno")
    
    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-created"]
    
    

class Orden(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    details=models.ForeignKey(Detail,on_delete=models.CASCADE,verbose_name="Detalles del pago")
    student=models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Estudiante")

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
        ordering = ["-created"]
    



