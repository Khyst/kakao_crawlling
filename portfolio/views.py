#Django Basis Source
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Portfolio

#Image Crawlling Module
from bs4 import BeautifulSoup
import urllib 
import urllib.request
import requests

def portfolio(request):
    portfolios = Portfolio.objects # 포트폴리오 model 객체
    return render(request, 'portfolio/portfolio.html',
    {'portfolios':portfolios}) # 객체 전달

def delete_portfolio():
    
    objects = Portfolio.objects

    for i in range(0, objects.count(), 1):
        objects.get(img_id=i).delete()
        #print('deletePortfolio', i)

def create_portfolio():
    id_step = 0
    year = 2018

    while year <= 2019:
        for j in range(1,12):
            flag = 0
            if(j<10):
                month = "0" + str(j)
                
            else:
                month = str(j)

            naming = str(year) + month
            
            url = "https://store.kakaofriends.com/kr/brand/wallpaper" + naming
                
            #print(url, "로 데이터 분석 시작")
            #print("====================================================================")
            
            resObj = requests.get(url)
            soupObj = BeautifulSoup(resObj.text, "html.parser")
            imgRoute = soupObj.select("#mArticle > div > div:nth-child(2) > img")

            try:
                for list_num in range(1):
                        #1pass
                        urllib.request.urlretrieve(imgRoute[list_num]['src'], "./portfolio/static/img/" + naming + '.jpg')
                        flag = 1
                        
            except:
                #print(' 파일이 존재 하지 않습니다.!')
                if year == 2019 :
                        return redirect('portfolio')
                        break
            
            if flag == 1:
                portfolios = Portfolio() #portfolio 객체 생성
                #img_url = imgRoute[list_num]['src']

                #1pass
                content = urllib.request.urlopen(imgRoute[list_num]['src'])
                portfolios.img_id = id_step
                portfolios.title = str(year) + "년 " + str(month) +"월 배경화면"
                portfolios.description = "store.kakaofriends.com/kr/"
                #portfolios.image("name", content)
                portfolios.image.save(naming + '.jpg', content,save=True)
                id_step += 1
            ##print("====================================================================")
        year += 1

def imageCrawlling(request):

    delete_portfolio()

    create_portfolio()

    return redirect('portfolio')