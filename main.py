from pandas.core.frame import DataFrame

import growtech
import chip
import judge

import sql
import pandas as pd
def contentout(str):
    stockid = pd.read_csv('stock.csv')  # 讀取csv
    #取出csv檔的title和所有股票代號及名稱
    stock = []
    idnamecontent = []
    records = stockid.to_dict(orient='records')
    for j in records:
        title = [i[0] for i in j.items()]
        idname = [i[1] for i in j.items()]
        stock.append(idname)
    # 把每隻股票丟進去迴圈
    for id, name in stock:
        if id == stock[644][0]:  # 由於3714今年剛上市，因此無資料得以分析
            continue
        else:
            run=judge.jud(id)
            run2=growtech.growtech(id)
            run3=chip.chip(id)
            # 判斷績優股的資料
            if str=='merit':
               print(id,name)
               b = run.pbr()[0]+run.pe()[0]+run.fr()[0]+run.yie()[0]#算出每支股票有符合幾個條件
               #假如符合條件超過六筆就把那筆個股資料放入list
               if b > 6:
                  content = [id,name,run2.tech()[2]]
                  content.extend(run.fr()[1])
                  content.extend([run.pe()[1], run.pbr()[1], run.yie()[1]])
                  idnamecontent.extend([content])
           
                      
            # 將各個股票評分夾到list
            elif str=='count':
               print(id,name)
               
               count=[(run.pbr()[0]+run.pe()[0]+run.yie()[0])*3+1,int(round(run.fr()[0]*2.5,0)),run2.grow()[0]*3+1,(run3.legal()+run3.supvisor()+run3.force())*3+1,run2.tech()[0]*3+1]
               content = [id,name]
               content.extend(count)
               print(content)
               idnamecontent.extend([content])
            #全部上市個股的資料
            else:
               print(id,name)
               content = [id,name,run2.tech()[2]]
               content.extend(run.fr()[1])
               content.extend([run.pe()[1], run.pbr()[1], run.yie()[1]])
               content.extend(run2.grow()[1])
               content.extend(run2.tech()[1])
               content.extend([run3.legal(),run3.force(),run3.supvisor()])
               print(content)
               idnamecontent.extend([content])
               
    #建立績優股判斷的名稱
    
    if str=='merit':
      title.append('現價')
      title.extend(run.fr()[2])
      title.extend(['本益比', '股價淨值比', '近三年殖利率'])
   #建立評分的名稱
    elif str=='count':
      title.extend(['價值','安全','成長','籌碼','技術'])
   #建立全部上市個股的名稱
    else:
      title.append('現價')
      title.extend(run.fr()[2])
      title.extend(['本益比', '股價淨值比', '近三年殖利率','grow1','grow2','grow3','tech1','tech2','tech3','legal','force','supvisor'])
      
    return idnamecontent,title
#將各個資料轉成DataFrame並上傳資料庫
def mainout(surface):
   con=sql.main()
   value,name=contentout(surface)
   df=DataFrame(value,columns=name)
   print(df)
   df.to_sql(name=surface,con=con,if_exists='replace',index=False)
   df.to_csv(f'{surface}.csv',index=False)
if __name__=='__main__':
   mainout('merit')
   mainout('count')
   mainout('stock')
 
   
  
  
 
 
        
   