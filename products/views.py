from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from profiles.models import UserProfile
from .models import Product, Category
from .forms import ProductForm
from .models import Product
from reviews.models import Review


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
        user_profile = get_object_or_404(UserProfile, user=request.user)
    except Http404:
        return render(request, '404.html')

    reviews = Review.objects.all().filter(
        product=product).order_by('-created_at')
    product_reviewed_by_user = request.user.is_authenticated and Review.objects.all().filter(
                product=product).filter(user=user_profile.id).exists()
    
    print('product_reviewed_by_user', product_reviewed_by_user )

    context = {
        'product': product,
        'reviews': reviews,
        'product_reviewed_by_user': product_reviewed_by_user

    }
    return render(request, 'products/product_detail.html', context)


def handler404(request, exception):
    return render(request, '404.html')


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to add product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
