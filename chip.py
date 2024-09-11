
import requests
from bs4 import BeautifulSoup
import requests
import pandas as pd

class chip:
    def __init__(self,id):
        self.id=id
        self.crawler=requests.get(f"https://tw.stock.yahoo.com/quote/{self.id}/institutional-trading")
        self.soup=BeautifulSoup(self.crawler.text,'lxml')
        self.date()
     

    #時間處理
    def date(self):
        div_date=self.soup.find_all("div",class_="W(96px) Ta(start)") #取出日期資料
        del div_date[0] #將標題欄位刪除
        div_date=list(map(lambda i:i.text,div_date)) #取出標籤裡的內容

        month=div_date[0][:7] #取出年份及月分
        if int(div_date[0][5:7])-1==0: #如果月份是1取前一年12月的資料
            month2=str(int(div_date[0][:4])-1)+"/12"
        else:
            month2=div_date[0][:5]+str(int(div_date[0][5:7])-1)
        date=[[month,month2],[div_date[0],div_date[1]]]
        #將時間資料輸出成csv最為暫存檔
        date=pd.DataFrame(date,columns=['now','before'])
        date.to_csv('date.csv',index=False)
        return [month,month2],[div_date[0],div_date[1]]
        
#籌碼面
    #法人買賣超
    def legal(self):
        
        div_legal=self.soup.find_all("span",attrs={"class":["Jc(fe) D(f) Ai(c) C($c-trend-down)","Jc(fe) D(f) Ai(c) C($c-trend-up)","Jc(fe) D(f) Ai(c)"]}) #取出法人買賣超合計
        div_legal=list(map(lambda i:i.text.replace(",",""),div_legal)) #取出標籤裡的內容及字串處理
        
        #判斷連兩篇買賣超得分
        leg_score=0
        if int(div_legal[0])>0 and int(div_legal[1])>0:
            leg_score=1
        return leg_score

    #董監持股
    def supvisor(self):
        
        content=[]
        cra=requests.get(f"https://tw.stock.yahoo.com/quote/{self.id}/major-holders")
        soup=BeautifulSoup(cra.text,"lxml")
        div=soup.find("ul",{"class":"M(0) P(0) List(n)"}) #縮小範圍
        #取得內容
        date=div.find_all("div",{'class':'Fxg(1) Fxs(1) Fxb(0%) Miw($w-table-cell-min-width) Ta(end) Mend($m-table-cell-space) Mend(0):lc'}) 
        for i in date:
            content.append(i.text)
        date=div.find_all("span",attrs={"class":""}) #日期資料
        date=list(map(lambda i:i.text,date)) #取出標籤裡的內容
        supervisor=[content[i:i+4] for i in range(0,len(content),4)] #每四筆資料一組
        month=pd.read_csv('date.csv')[0:1] #存放近兩月的董監持股比例
        compare=[]
        #取出月底的董監資料
        for d in date:
            if month.loc[0]['now'] in d:
                ind=date.index(d) 
                compare.append(supervisor[ind][2].replace("%","")) #新增這個月的董監資料
                for j in date:
                    if month.loc[0]['before'] in j:
                        ind=date.index(j)
                        compare.append(supervisor[ind][2].replace("%","")) #新增前個月的董監持股
                        break 
                break
        #評分
        sup_score=0
        if compare[0]>compare[1]:
            sup_score=1
        return sup_score
    
    #主力買賣超
    def cralwer(self,date,stockid):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
        requests.packages.urllib3.disable_warnings()
        cra=requests.get(f"https://fubon-ebrokerdj.fbs.com.tw/z/zc/zco/zco.djhtm?a={stockid}&e={date}&f={date}",headers=headers,verify=False)
        soup=BeautifulSoup(cra.text,"lxml")
        td=soup.find_all("td",attrs={"colspan":"4"}) #買超、賣超資料
        #即使開盤日也有沒有主力資料
        if len(td)==0:
            return 0
        else:
            buy=int(td[0].text.replace(",",""))
            sell=int(td[1].text.replace(",",""))
            return buy-sell
    def force(self):
        month=pd.read_csv('date.csv')[1:2]
        date=[i.replace("/","-") for i in month]
        ma=[self.cralwer(date[0],self.id),self.cralwer(date[1],self.id)] #date格式是ex.2021-12-17
        main_score=0
        if ma[0]>0 and ma[1]>0:
            main_score=1
        return main_score

    

