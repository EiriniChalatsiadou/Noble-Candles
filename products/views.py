from django.shortcuts import render
# from .models import Product


def all_products(request):

    # products = Product.objects.all()

    context = {
        # 'products': products,
        'products': [
            {
                'name': 'Secret Rose',
                'sku': '1234',
                'category': 'candles',
                'description': 'soya wax candle, floral-vetiner-sandalwood',
                'price': '15,00 euro',
                'rating': '4,5',
                'image_url': "/media/products/candle-1.jfif",
                'image': '1',
            }
        ]
    }
    return render(request, 'products/products.html', context)
