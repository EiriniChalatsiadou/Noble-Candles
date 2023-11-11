from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.db.models import Q
from .models import Product


def all_products(request):

    products = Product.objects.all()
    query = ''

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request,
                           ("Please provide a search term!"))
            return redirect(reverse('products'))

        queries = Q(name__icontains=query)
        queries |= Q(description__icontains=query)
        queries |= Q(category__name__icontains=query)
        products = products.filter(queries)

    elif 'category' in request.GET:
        category = request.GET['category']
        if not category:
            messages.error(request,
                           ("Wrong category!"))
            return redirect(reverse('products'))
        products = products.filter(Q(category__name__icontains=category))

    context = {
        'products': products,
        'q': query
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    try:
        product = get_object_or_404(Product, pk=product_id)
    except Http404:
        return render(request, '404.html')

    context = {
        'product': product,

    }
    return render(request, 'products/product_detail.html', context)


def handler404(request, exception):
    return render(request, '404.html')