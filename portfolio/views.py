#Django Basis Source
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Portfolio, portfolioKey
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
import datetime

#Image Crawlling Module
from bs4 import BeautifulSoup
import urllib 
import urllib.request
import requests

def home(request):
    return redirect('portfolio')

def portfolio(request): # Backbone!!
    portfolios = Portfolio.objects # 포트폴리오 model 객체
    return render(request, 'portfolio/portfolio.html',
    {'portfolios':portfolios}) # 객체 전달


""" initalizer()
portfolio 객체를 생성할때, portfolioKey와 연결하기 때문에 ( 데이터베이스 수작업 )
portfolioKey가 DoesNotExist해서 오류가 되는 케이스를 방지하기 위해서
portfolioKey를 미리 initialization(초기화)한다.

23개는 그냥 임의로 초기화 함, (사실 2019년 12월 1일인 현재, 웹 상에 총 23개의 이미지가 올라왔기 때문임)
"""
def initializer(request): 
    for i in range(0, 23, 1):
            key_save = portfolioKey()
            key_save.portfolio_id = i
            key_save.save()
    return redirect('portfolio')
            
def delete_single_portfolio(request, delete_id): # CUSTOM delete
    objects = Portfolio.objects
    objects.get(img_id=delete_id).delete() 
    return redirect('portfolio')

def delete_portfolio(request): # ALL delete
    objects = Portfolio.objects
    key = portfolioKey.objects
    for i in range(0, objects.count(), 1):
        num = key.get(portfolio_id=i)
        objects.filter(img_id=num)[0].delete()
    return redirect('portfolio')

    
def create_portfolio():
    id_step = 0
    year = 2018
    objects = Portfolio.objects # Portfolio Objects Query
    key = portfolioKey.objects # portfolioKeys Objects Query

    now = datetime.datetime.utcnow()
    nowYear = now.year

    while year <= nowYear:
        for j in range(1,13):
            isExistFlag = 0
            if(j<10):
                month = "0" + str(j)          
            else:
                month = str(j)

            naming = str(year) + month
            overlap_flag=False # 중복 플래그

            """ 중복 방지 """
            try:
                for i in range(0, objects.count(), 1):
                    filtered = key.filter(portfolio_id=i)
                    object_filtered = objects.filter(img_id=i)

                    if not object_filtered:
                        break # 중복을 찾을 필요 없음, Empty Queryset 이기 때문에
                    else:
                        num = filtered.first().portfolio_id # Empty가 아니면 코드 실행

                        if naming == object_filtered.first().name: ## 중복 확인
                            overlap_flag = True
                            continue
                    
                if overlap_flag is True:
                    continue
            except ObjectDoesNotExist: 
                pass

            """ Except ObjectDoesNotExist
            아무 portfolio Instance가 없는 초기에 에러가 뜨지않고
            웹상에서 크롤링작업을 이어서 할수 있도록 예외처리
            """
            
            url = "https://store.kakaofriends.com/kr/brand/wallpaper" + naming
                
            ##print((url, "로 데이터 분석 시작")
            ##print(("====================================================================")
            
            resObj = requests.get(url)
            soupObj = BeautifulSoup(resObj.text, "html.parser")
            imgRoute = soupObj.select("#mArticle > div > div:nth-child(2) > img")

            try:
                for list_num in range(1):
                        #1pass
                        urllib.request.urlretrieve(imgRoute[list_num]['src'], "./portfolio/static/img/" + naming + '.jpg')
                        isExistFlag = 1 # 크롤링 하려는 파일이 존재하면 ( isExistFlag = 1 )
                        
            except:
                ##print((' 파일이 존재 하지 않습니다.!')
                if year == nowYear :
                        return redirect('portfolio')
                        break
            
            if isExistFlag == 1:
                portfolios = Portfolio() #portfolio 객체 생성
                key_save = portfolioKey()

                content = urllib.request.urlopen(imgRoute[list_num]['src'])
                portfolios.img_id = id_step
                portfolios.name = naming
                portfolios.title = str(year) + "년 " + str(month) +"월 배경화면"
                portfolios.description = "store.kakaofriends.com/kr/"

                if key.count() <= id_step :
                    key_save.portfolio_id = id_step
                    key_save.save()
                
                portfolios.image.save(naming + '.jpg', content,save=True)
                id_step += 1

        year += 1

def imageCrawlling(request):

    create_portfolio()

    return redirect('portfolio')