from django.shortcuts import render,redirect
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Beca,Detail,Group,Orden,Student,Payment
from django.contrib import messages

def home(request):
    return render(request, "core/index.html")
    
#Funciones de pagos
def payments(request):
    students=Student.objects.all()
    details=Detail.objects.all()
    payments=Payment.objects.all()
    return render(request, "core/payments.html",
    {
        'students':students,
        'details':details,
        'payments':payments
         }
    )

def PostPayments(request):
    if request.method == 'POST':
        id_student=request.POST.get('nombre')
        id_details=request.POST.get('tipo')
    
        payments=Payment(
            student_id=id_student,
            details_id=id_details
        )
        payments.save()
        messages.success(request,'Pago Realizado')
        return redirect('history')
#Mostrar alumnos

#Mostrar detalles de pagos



def students(request):
    return render(request, "core/student.html")

def ordenPayments(request):
    students=Student.objects.all()
    details=Detail.objects.all()
    payments=Payment.objects.all()
    return render(request, "core/ordenpayment.html", {
        'students':students,
        'details':details,
        'payments':payments
         })

def PostOrden(request):
    if request.method == 'POST':
        id_student=request.POST.get('nombre')
        id_details=request.POST.get('tipo')
    
        ordens=Orden(
            student_id=id_student,
            details_id=id_details
        )
        ordens.save()
        messages.success(request,'Revise que la informacion sea correcta antes de descargar el PDF')
        return redirect('pre-orden')

    

def PreOrden(request):
    ordens=Orden.objects.all().order_by('-id')[:1]  
    return render(request, "core/preorder.html",{'ordens': ordens})

def pdf_report(request,id):
    ordens=Orden.objects.get(pk=id)
    template_path = 'core/pdf.html'
    context = {
        'ordens': ordens,
        'comp':{'name':'Academia Costa del Pacifico','ruc':'ORDEN DE PAGO','Address':'Avenida, Universidad Tecnológica 1, Barrio la Villita, 75483 Tecamachalco, Pue.'}
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def history(request):
    payments = Payment.objects.all()
    return render(request, "core/history.html",{'payments': payments})

def index(request):
    ...

    num_authors=Author.objects.count()  # El 'all()' se obvia en este caso.

    # Numero de visitas a esta view, como está contado en la variable de sesión.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_authors':num_authors,
        'num_visits':num_visits,
    } 

    # Carga la plantilla index.html con la información adicional en la variable context.
    return render(request, 'index.html', context=context)


    



