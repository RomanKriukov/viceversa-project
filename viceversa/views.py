from django.http import HttpResponse
from django.shortcuts import render
from collections import Counter


def home(request):
    return render(request, 'home.html', {'greeting': 'Hello from views!'})


def reverse(request):
    user_text = request.GET['usertext']
    counter_words = len(Counter(user_text.split()))
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': user_text,
                                            'reversedtext': reversed_text,
                                            'counterwords': counter_words})
