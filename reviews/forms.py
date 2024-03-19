from django import forms
from .models import Review, RatingEnum


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=RatingEnum.choices,
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-inline ', 'style': 'list-style:none'},
        )
    )
    content = forms.CharField(
        # Bootstrap textarea styles
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': 10, 'maxlength': 1024}),
        label='Please Write Your Review'
    )

    class Meta:
        model = Review
        fields = ['rating', 'content']
        labels = {'content': 'Please Write Your Review '}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
