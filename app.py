from flask import Flask,request,jsonify,render_template
import matplotlib.pyplot as plt
from flask_cors import CORS
import matplotlib

import sql

import datetime
import yfinance as yf
import mplfinance as mpf

from matplotlib import pyplot as plt
from dateutil.relativedelta import relativedelta
matplotlib.use('Agg')
app = Flask(__name__)

CORS(app)
@app.route("/")
#載入起始頁面
def index():
    return render_template('index.html')
@app.route("/select",methods=['GET'])
#績優股所有資料回傳前端
def select():
    sq=sql.main()
    query = sq.execute("SELECT * FROM merit")
    df=[dict(i) for i in query]
    return jsonify(df)
@app.route("/toward",methods=['POST'])
# 把個股評分回傳以及製作線圖
def towards():
    id=request.values['id']
    res={'data':{
        'ok':True,
        'msg':'成功',
        'id':'nknk'
    }}
    con=sql.main()
    count = con.execute(f'SELECT * FROM `count` WHERE `有價證券代號`="{id}" OR `有價證券名稱`="{id}"')
    countcontent=[list(i) for i in count]
    stock = con.execute(f'SELECT * FROM `stock` WHERE `有價證券代號`="{id}" OR `有價證券名稱`="{id}"')
    stockcontent=[list(i) for i in stock]
    img(stockcontent[0][0])
    return jsonify({'id':stockcontent[0][0],'name':stockcontent[0][1],'count':countcontent ,'stock':stockcontent})
def img(id):
    stock=yf.Ticker(f'{id}.TW') #獲得參數(股票代碼)取股票
    past=datetime.date.today()-relativedelta(years=3) #取三年前今天的日期
    now=datetime.date.today() #取今天日期
    df=stock.history(start=past,end=now,interval='1wk') #取股票三年歷史資料 頻率為一周
    df=df.drop(['Dividends','Stock Splits'],axis=1) #刪除資料兩列資料
    mc=mpf.make_marketcolors(up='r',down='g',inherit=True) #設定線圖顏色 紅色為漲 綠色為跌
    s=mpf.make_mpf_style(base_mpf_style='yahoo',marketcolors=mc) #設定線圖格式
    kwargs=dict(type='candle',mav=(5),volume=True,figratio=(10,5),figscale=0.75,style=s,savefig=f'./static/img/{id}.png') #設定線圖格式:蠟燭圖 圖片大小 標題名稱
    mpf.plot(df,**kwargs)

if __name__ == "__main__":
    app.run(port=8000,debug=True)
