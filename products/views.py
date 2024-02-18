from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Product, Category

from .forms import ProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

#To view all the products in the showproductss.html
def ShowAllProducts(request):

    category = request.GET.get('category')   # get the clicked category name

    if category == None:
        products = Product.objects.filter(is_published=True).order_by('-created_at')
    else:
        products = Product.objects.filter(category__name =category)

    page_num = request.GET.get('page')            # creating the total pages
    paginator = Paginator(products, 2)    # settting total number of products in a page

    try:
        products = paginator.page(page_num)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    categories = Category.objects.all()
    #DB -> Table -> records
    context = {
        'products': products,
        'categories': categories
    }

    return render(request, 'showProducts.html', context)

#To view the single product details in the productDetail.html
def productDetail(request, pk):
    eachproduct = Product.objects.get(id=pk)

    context = {
        'eachproduct': eachproduct
    }

    return render(request, 'productDetail.html', context)

#To add the new product from the html template page, addProduct.html
@login_required(login_url='showProducts')
def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
        'form': form
    }

    return render(request, 'addProduct.html', context)

# To update product form the html template page, updateProduct.html
@login_required(login_url='showProducts')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showProducts')

    context = {
            'form': form
        }
    return render(request, 'updateProduct.html', context)

# Deleting the record from the database from the table, base on the primary key or unique
@login_required(login_url='showProducts')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)      #storing record of 1 or 2 or 3 or 4 in product
    product.delete()             # 1 => Deleted

    return redirect('showProducts')

# creating a function for searching the data from the database using the keyword
@login_required(login_url='showProducts')
def searchBar(request):
    if request.method == 'GET':    # get = GET ==> True
        query = request.GET.get('query')   # query = 999
        if query:
            products = Product.objects.filter(price__contains=query) | Product.objects.filter(name__contains=query)
            return render(request, 'searchbar.html', {'products': products})
        else:
            print('No Products to show in the Database')
            return render(request, 'searchbar.html', {})

