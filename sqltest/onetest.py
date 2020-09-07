from pymysql import connect, cursors
from pymysql import OperationalError
import os
import configparser as cparser
import time
from sqltest.settings import DATABASES1

# ====================读取db_config.ini文件设置=========
# base_dir = str(os.path.dirname(os.path.dirname(__file__)))
# base_dir = str(os.path.dirname(__file__))
# print(base_dir)
# base_dir = base_dir.replace('\\', '/')
# file_path = base_dir + '/settings'
# print(file_path)
#
# cf = cparser.ConfigParser()
# print(cf)
# cf.read(file_path)
# host = cf.get('mysqlconf', 'host')
# port = cf.get('mysqlconf', 'port')
# db = cf.get('mysqlconf', 'db_name')
# user = cf.get('mysqlconf', 'user')
# password = cf.get('mysqlconf', 'password')

print(DATABASES1)
host = DATABASES1.get('default').get('HOST')
user = DATABASES1.get('default').get('USER')
password = DATABASES1.get('default').get('PASSWORD')
db = DATABASES1.get('default').get('DBNAME')
port = DATABASES1.get('default').get('PORT')
print(host)


class DB:
    def __init__(self):
        try:
            # self.conn = connect(host="192.168.42.65", port=3306, user="root", password="123456", db="openroad")
            self.conn = connect(host=host, port=port, user=user, password=password, db=db)
        except Exception as e:
            print('连接数据库失败')

    # def delete(self, table_name, data):
    #     # DELETE FROM customer WHERE phone = '15035461679';
    #     real_sql = 'DELETE FROM ' + table_name + ' WHERE phone = ' + str(data)
    #     print(real_sql)
    #     with self.conn.cursor() as cursor:
    #         cursor.execute(real_sql)
    #     self.conn.commit()

    def select(self, table_name1, table_name2, data, data1):
        # SELECT a.account_id from easy_agent_account a , easy_agent b WHERE b.phone="15035461679" and a.easy_agent_id = b.easy_agent_id;
        real_sql = 'SELECT a.easy_agent_id from ' + table_name1 + ' a ,' + table_name2 + ' b WHERE b.phone=' + "'" + str(
            data) + "'" + ' and a.easy_agent_id = b.easy_agent_id;'
        # real_sql = 'select easy_agent_id from ' + table_name2 + ' where phone=' + "'" + str(data) + "';"
        print(real_sql)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql)
            a = cursor.fetchall()[0][0]
            print(a)
        # update easy_agent_account set balance='200000' where easy_agent_id=3177129;
        real_sql1 = 'update ' + table_name1 + ' set balance=' + "'" + str(data1) + "'" + ' where easy_agent_id =' + str(
            a) + ';'
        print(real_sql1)
        with self.conn.cursor() as cursor:
            cursor.execute(real_sql1)
        self.conn.commit()

    def close(self):
        self.conn.close()


# if __name__ == '__main__':
#     db = DB()
#     table_name = 'sign_guest'
#     table_name1 = 'easy_agent_account'
#     table_name2 = 'easy_agent'
#     data = {'phone': 18768494086}
#     data1 = {'balance': 6000000}
#     db.select(table_name1, table_name2, data['phone'], data1['balance'])

    # db.delete(table_name, data['phone'])
