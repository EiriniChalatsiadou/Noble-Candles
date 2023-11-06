from django.shortcuts import render
# from .models import Product


def all_products(request):

    # products = Product.objects.all()

    context = {
        # 'products': products,
        'products': [
            {
                'name': 'Eirini',
                'sku': '1332432423',
                'category': 'Christmas',
                'description': '',
                'price': '',
                'rating': '',
                'image_url': '',
                'image': '',
            }
        ]
    }
    return render(request, 'products/products.html', context)
