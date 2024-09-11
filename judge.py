import json

import pandas as pd
import requests
from bs4 import BeautifulSoup


class jud():
    def __init__(self, id):
        self.id = id
    # 找出所有財務資料

    def fr(self):
        set = requests.get(
            f'https://marketinfo.api.cnyes.com/mi/api/v1/statement/TWS%3A{self.id}%3ASTOCK/ratio/year')
        set = json.loads(set.content)['data']['datas']
        name = []
        percent = []
        amout = []
        try:
            # 分別將營業毛利率,營業利益率,負債占資產比率,每股盈餘取出來並將它放入list
            for i in set:
                name.append(i['name'])
                percent.append(i['datasets'][0]['percent'])
                amout.append(i['datasets'][0]['amount'])
            namecontent = [name[i] for i in [0, 1, 11]]
            namecontent.append(name[6])  # 取出名稱
            percent = [percent[i] for i in [0, 1, 11]]
            percent.append(amout[6])  # 取出內容
        except:
            return 0
        count = 0
        for a in percent:
            p = percent.index(a)
            # 判斷這四個是否符了我們條件
            if a == None:
                continue

            elif p == 0: 
                #營業毛利率
                if percent[p] > 30:
                    count += 1
            elif p == 1:
                #營業利益率
                if 10 < percent[p]:
                    count += 1
            elif p == 2:
                #負債比率
                if 50 > percent[p]:
                    count += 1
            elif p == 3:
                #每股盈餘EPS
                if 0 < percent[p]:
                    count += 1
            else:
                continue
        return count, percent, namecontent
    # 找出本益比

    def pe(self):
        url = f'https://invest.cnyes.com/twstock/tws/{self.id}'
        list_req = requests.get(url)
        try:
            soup = BeautifulSoup(list_req.content, "html.parser")
            pe = soup.find_all('div', {'class': 'jsx-2687283247'})[22].text
        except:
            return 0, None
        # 判斷本益比是否符了我們條件
        if pe == '本益比為負值':
            return 0, pe
        elif pe[0] == '-':
            return 0, pe
        elif pe[1] == ',':
            return 0, pe
        elif 10 <= float(pe) < 20:
            return 1, pe
        else:
            return 0, pe
     # 找出本淨比

    def pbr(self):
        url = f'https://invest.cnyes.com/twstock/tws/{self.id}'

        list_req = requests.get(url)

        try:
            soup = BeautifulSoup(list_req.content, "html.parser")
            pbr = soup.find_all('div', {'class': 'jsx-2687283247'})[25].text

        except:
            return 0, None
        # 判斷本淨比是否符了我們條件
        if pbr == '本淨比為負值':
            return 0, pbr
        elif pbr[0] == '-':
            return 0, pbr
        elif pbr[1] == ',':
            return 0, pbr
        elif float(pbr) < 1.5:
            return 1, pbr
        else:
            return 0, pbr
    # 算出近三年平均殖利率
    def yie(self):
        url = f"https://marketinfo.api.cnyes.com/mi/api/v1/TWS%3A{self.id}%3ASTOCK/divided"
        response = requests.get(url)
        data = json.loads(response.content)
        df = data["data"]['divides']
        if df == []:
            return 0, None
        else:
            #把日期只留西元年 ex:2021-09-09->2021
            df = pd.DataFrame(df)
            df = df[["formatDate", "formatDividendYield"]]
            df.insert(0, 'year', df["formatDate"].map(lambda x: x.split('/')[0]))
            df = df.drop('formatDate', axis=1)
            # 處理空字串
            for i in range(len(df['formatDividendYield'])):
                if df['formatDividendYield'][i] == "":
                    df['formatDividendYield'][i] = 0
            df['formatDividendYield'] = df['formatDividendYield'].astype(
                "float64")
            
            sum = 0
           #把三年殖利率相加起來並算出平均
            for i in range(2018, 2021):
                a = df[df['year'] == str(i)]
                for j in a['formatDividendYield']:
                    sum += j
            sum /= 3
            if sum > 4:
                return 1, round(sum, 2)
            else:
                return 0, round(sum, 2)


