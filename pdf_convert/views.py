from django.shortcuts import render

from products.models import Product

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def show_products(request):
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'pdf_convert/showinfo.html', context)


def pdf_report_create(request):
    products = Product.objects.all()

    template_path = 'pdf_convert/pdfReport.html'

    context = {'products': products}

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="products_report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
