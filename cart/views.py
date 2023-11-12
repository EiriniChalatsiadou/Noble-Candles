from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

# Create your views here.
def view_cart(request):
    """ A view to return the cart contents page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                            (f'Updated {product.name} '
                            f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request,
                            (f'Removed {product.name} '
                            f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
