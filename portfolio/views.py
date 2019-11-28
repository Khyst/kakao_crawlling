#Django Basis Source
from django.shortcuts import render, redirect
from .models import Portfolio

#Image Crawlling Module
from bs4 import BeautifulSoup
import urllib 
import urllib.request
import requests

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects # 포트폴리오 model 객체
    return render(request, 'portfolio/portfolio.html',
    {'portfolios':portfolios}) # 객체 전달

def imageCrawlling(request):

    """img_url = "https://t1.kakaocdn.net/friends/prod/brand/201907_type1_2880.jpg"
    content = urllib.request.urlopen(img_url)

    portfolios.title = "savename"
    portfolios.description = "KAKAO FRIENDS BACKGROUND"
    #portfolios.image("name", content)
    portfolios.image.save("name", content,save=True)"""

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
            #print(imgRoute)
            
            #print('-----------------------------------------------------------------------------------------------------------')

            try:
                for list_num in range(1):
                        #print(imgRoute[list_num]['src'])
                        savename = "./portfolio/static/img/" + naming + '.jpg'
                        #print(savename)
                        urllib.request.urlretrieve(imgRoute[list_num]['src'], savename)
                        flag = 1
                        
            except:
                #print(' 파일이 존재 하지 않습니다.!')
                if year == 2019 :
                        return redirect('portfolio')
                        break
            
            if flag == 1:
                portfolios = Portfolio() #portfolio 객체 생성
                img_url = imgRoute[list_num]['src']
                content = urllib.request.urlopen(img_url)

                portfolios.title = str(year) + "년 " + str(month) +"월 배경화면"
                portfolios.description = "store.kakaofriends.com/kr/"
                #portfolios.image("name", content)
                portfolios.image.save(naming, content,save=True)

            ##print("====================================================================")
            
        year += 1
    
    print('End')
    return redirect('portfolio')