from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import Review
from .forms import ReviewForm
from products.models import Product

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                user=user_profile,
                product=product,
                rating=request.POST.get('rating'),
                content=request.POST.get('content')
            )
            messages.success(request, 'Review sucessfully added')
        else:
            print(form.errors.as_data())
            messages.error(
                request,
                'Review failed to submit. \
                Please correct the errors or ensure your review does not contain profanity.'
                )
        return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product':product
    }

    return render(request, template, context)