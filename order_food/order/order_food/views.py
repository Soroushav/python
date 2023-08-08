from django.shortcuts import render
from order_food.models import *
from django_comments.forms import CommentForm
from django.contrib import messages

def menu_view(request):
    query_param = request.GET.get('c')
    if not query_param == None:
        if not request.session.get(f'message_shown_{query_param}', False):
            messages.info(request, 'your comment successfully submitted')
            request.session[f'message_shown_{query_param}'] = True

    foods = Food.objects.all()
    return render(request, 'order_food/menu.html', {
        'foods': foods,
    })
