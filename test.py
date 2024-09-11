from flask import Flask, render_template, request, jsonify
import sql
import pymysql
import numpy as np
app = Flask(__name__)

# 首頁路由
@app.route('/')
def index():
    return render_template('index.html')
#地圖路由
@app.route('/map')
def map():
    return  render_template('index2.html')

# 購物車路由
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        # 在這裡處理購物車相關的邏輯
        # 獲取從前端傳遞的數據，執行購物車操作
        # 返回適當的響應或執行相應的後續處理
        x1 = request.form['']
        print("POST ")
        # 例如，你可以獲取從前端傳遞的餐點和價格
        item = request.form.get('item')
        price = float(request.form.get('price'))

        # 在這裡執行購物車操作，例如將餐點添加到購物車中

        # 返回 JSON 格式的響應
        return jsonify({'message': 'Item added to cart successfully'})

    # 如果是 GET 請求，返回購物車頁面
    return render_template('cart.html')
#帳戶路由
@app.route('/account')
def account():
    return  render_template('account.html')
#設定路由
@app.route('/settings')
def settings():
    return  render_template('settings.html')


@app.route('/location', methods=['POST'])
def save_location():
    return render_template('index5.html')



@app.route('/sss')
def sql_sss():
    
    con = sql.main()
    
    # #新增資料
    #     insert_query = "INSERT INTO stock (name, price) VALUES ('Apple', 200)"
    #     con.execute(insert_query)
    #
    # #修改資料
    #     update_query = "UPDATE stock SET price = 250 WHERE name = 'Apple'"
    #     con.execute(update_query)
    #
    # #刪除資料
    #     delete_query = "DELETE FROM stock WHERE name = 'Apple'"
    #     con.execute(delete_query)

    # 查詢資料
 
    result = con.execute(('SELECT * FROM `user`'))
    for row in result:
        print(row)
    # Close the database connection
    con.close()
    return  render_template('settings.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
