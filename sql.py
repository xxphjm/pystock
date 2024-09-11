from sqlalchemy import create_engine 
def main():
    username = 'root'     # 資料庫帳號
    password = '0805'     # 資料庫密碼
    host = 'localhost'    # 資料庫位址
    database = 'stock'   # 資料庫名稱
    charset='utf8'
    # 建立連線引擎
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:8889/{database}?charset={charset}')
    con=engine.connect()
    return con
  
       
    
