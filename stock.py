
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np

#找出所有股票代號以及名稱
s=requests.get('https://isin.twse.com.tw/isin/C_public.jsp?strMode=2')
soup=BeautifulSoup(s.text, 'html.parser')
rows = soup.find('table',{'class':'h4'}).find_all('tr')
stocktitle=[]
#取得股票表格標題
for row in rows[0:1]:
    all_tds = row.find_all('td')
    for i in all_tds:
        stocktitle.append(i.text)
stock=[]
#取得所有股票表格內容
for row in rows[2:960]:
    all_tds = row.find_all('td')
    for i in all_tds:
        stock.append(i.text)
#把所有內容轉成7欄958列

stock=np.reshape(stock,(958,7))
stockcontent=pd.DataFrame(stock,columns=stocktitle )
#將代號及名稱分開成兩欄並將除了這兩欄以外的其他欄刪除,並會出成csv
stockcontent.insert(0,'有價證券代號',stockcontent['有價證券代號及名稱 '].map(lambda x: x.split('\u3000',1)[0]))
stockcontent.insert(1,'有價證券名稱',stockcontent['有價證券代號及名稱 '].map(lambda x: x.split('\u3000',1)[1]))
stockcontent=stockcontent.drop(stockcontent.iloc[:,2:],axis=1)
stockcontent.to_csv('stock.csv',index=False)





