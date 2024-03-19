from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from profiles.models import UserProfile
from .models import Review, review_exists_for_product
from .forms import ReviewForm
from products.models import Product


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    product_reviewed_by_user = review_exists_for_product(product, user_profile)
    if product_reviewed_by_user:
        return redirect(reverse('product_detail', args=[product_id]))

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
        'product': product
    }

    return render(request, template, context)


@login_required
def edit_review(request, review_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Retrieve the review object
    review = get_object_or_404(Review, pk=review_id)
    product_reviewed_by_user = review_exists_for_product(
        review.product, user_profile)

    if not product_reviewed_by_user:
        redirect(reverse('product_detail', args=[review.product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            product = review.product
            reviews = Review.objects.all().filter(product=product)
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('product_detail', args=[review.product.id]))
        else:
            messages.error(
                request,
                'Failed to update review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(
            request, f'You are editing your review for {review.product.name}'
        )

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': review.product,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    # Retrieve the review object
    review = get_object_or_404(Review, pk=review_id)
    product_reviewed_by_user = review_exists_for_product(
        review.product, user_profile)

    if product_reviewed_by_user:
        # Delete the review
        review.delete()

    return redirect(reverse('product_detail', args=[review.product.id]))
