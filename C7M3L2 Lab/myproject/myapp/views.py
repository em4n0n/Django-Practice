from django.shortcuts import render
from myapp.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

# Create your views here.
def form_view(request):
    form = CommentForm() # create a form object
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data # cleaned_data helps with data normalization
            uc = UserComments(
                first_name = cd['first_name'],
                last_name = cd['last_name'],
                comment = cd['comment']
            )
