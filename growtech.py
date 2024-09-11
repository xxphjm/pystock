import numpy as np
from bs4 import BeautifulSoup
import requests
import yfinance as yf

from main import contentout
class growtech:
    def __init__(self,id):
        self.id=id
    #成長面
    def grow(self):
        tr=[]
        while(tr==[]):
            try:
                s=requests.get(f'https://tw.stock.yahoo.com/quote/{self.id}/revenue')
                soup=BeautifulSoup(s.text,'html.parser')
                #抓取月增、年增以及近12月營收成長的資料
                tr=[float((soup.find('li',{'class':"List(n)"}).find_all('li',{'class':"Jc(c) D(ib) Fxs(0) W(85px) Ta(end) Mend(0)"})[i].text.replace('%',"").replace(',',""))) for i in range(0,3)]
            except:
                continue
        count=0
        #判斷這三個值是否符合
        for i in tr:
            p=tr.index(i)
            if p==0:
                #月增率
                if tr[p]>5:
                    count+=1   
            elif p==1:
                #年增率
                if tr[p]>10:
                    count+=1  
            elif p==2:
                if tr[p]>15:
                    count+=1
            else:
                continue
        return count,tr
    #技術面
    def tech(self):
        count=0
        stock_id = f'{self.id}.TW'
        data = yf.Ticker(stock_id)
        moma=data.history(period='3mo')['Close']#抓取前三個月的資料
        stock=moma.tail(1)[0]#抓取現價
        ma=[round(np.mean(moma.tail(i)),2) for i in [5,20,60]]#分別算出5ma,20ma,60ma值
        #判斷現價是否大於三個值
        for m in ma:
            if float(stock)>float(m):
                count+=1

        return(count,ma,round(stock,2))




