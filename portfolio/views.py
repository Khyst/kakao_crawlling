from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def portfolio(request):
    portfolios = Portfolio.objects # 포트폴리오 model 객체
    return render(request, 'portfolio/portfolio.html',
    {'portfolios':portfolios}) # 객체 전달
