from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

def home(request):
    return render(request, "core/home.html")

def payments(request):
    return render(request, "core/payments.html")

def students(request):
    return render(request, "core/student.html")

def ordenPayments(request):
    return render(request, "core/ordenpayment.html")

def pdf_report(request):
    template_path = 'core/pdf.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
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
    return render(request, "core/history.html")



    



