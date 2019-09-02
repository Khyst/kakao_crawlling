from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests

year = 2017

while year <= 2019:
     for j in range(1,12):
          if(j<10):
               naming = str(year) + "0" + str(j)
               
          else:
               naming = str(year) + str(j)

          url = "https://store.kakaofriends.com/kr/brand/wallpaper" + naming
               
          print(url, "로 데이터 분석 시작")
          print("====================================================================")
          
          resObj = requests.get(url)
          soupObj = BeautifulSoup(resObj.text, "html.parser")
          imgRoute = soupObj.select("#mArticle > div > div:nth-child(2) > img")
          
          print('-----------------------------------------------------------------------------------------------------------')

          try:
               for list_num in range(1):
                    print(imgRoute[list_num]['src'])
                    savename = "./img/" + naming + '.jpg'
                    urllib.request.urlretrieve(imgRoute[list_num]['src'], savename)
                    
          except:
               print(' 파일이 존재 하지 않습니다.!')
               if year == 2019 :
                    break;
          
          print("====================================================================")
          
          
     year += 1
     
     
