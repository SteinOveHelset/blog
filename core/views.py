from django.shortcuts import render, redirect
from django.contrib import messages

from article.models import Article
from core.models import NewsletterSubscriber


def index(request):
    articles = Article.objects.all()
    return render(request, 'core/index.html', {'articles': articles})


def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            _, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'You have successfully subscribed!')
            else:
                messages.info(request, 'You are already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('index')
