# -*- coding:utf-8 -*-

import os
import pymysql

def query_database_info(host, port, uesrname, password):
    #
    db_info = {}
    #
    db_names = None
    with pymysql.connect(host = host, port = port,
                         user = uesrname, passwd = password) as cursor:
        #
        sql_command = "SHOW DATABASES"
        cursor.execute(sql_command)
        db_names = cursor.fetchall()
        #
    if db_names is not None:
        db_names = [name[0] for name in db_names]
        db_info.update({"database_count":len(db_names),
                        "database_name":db_names})
    return db_info

class MySQLDBManagement():

    def __init__(self, host, port, uesrname, password, db_name):
        #
        self.db_host = host
        self.db_port = port
        self.db_uesrname = uesrname
        self.db_password = password
        self.db_name = db_name
        #
        self.connect_db()

    def connect_db(self):
        #
        self.db = pymysql.connect(host = self.db_host,
                                  port = self.db_port,
                                  user = self.db_uesrname, 
                                  passwd = self.db_password,
                                  db = self.db_name,
                                  charset='utf8')
        self.cursor = self.db.cursor()

    def show_datatables(self):
        #
        show_datatables_command = "SHOW TABLES"
        self.cursor.execute(show_datatables_command)
        table_names = self.cursor.fetchall()
        table_names = [name[0] for name in table_names]
        #
        return table_names

    def query_field_count(self, table_name, record_name):
        #
        sql_table_record_count_command = "SELECT COUNT(" + record_name + ") FROM" + " " + table_name
        self.cursor.execute(sql_table_record_count_command)
        record_count = self.cursor.fetchone()
        #
        return record_count[0]

    def query_table_info(self, table_name):
        #
        table_field = []
        #
        sql_command = "SHOW COLUMNS FROM" + " " + table_name
        ## or use this command: sql_command = "DESCRIBE " + table_name
        ## or use this command: sql_command = "DESC " + table_name
        #
        self.cursor.execute(sql_command)
        fields_info = self.cursor.fetchall()
        #
        for field_info in fields_info:
            field_name = field_info[0]
            field_type = field_info[1]
            field_count = self.query_field_count(table_name, field_name)
            table_field.append([field_name, field_type, field_count])
        #
        return table_field

    def insert_record(self, table_name, record_list):
        #
        sql_command = "INSERT INTO" + " " + table_name + " " + "VALUES("
        format_char = "%s"
        for _ in range(len(record_list[0]) - 1):
            format_char += ",%s" 
        sql_command = sql_command + format_char + ")"
        self.cursor.executemany(query = sql_command, args = record_list)
        self.db.commit()

    def disconnect_database(self):
        #
        self.db.close()

if __name__ == "__main__":
    #
    db_host = "localhost"
    db_port = 3306
    db_uesrname = "root"
    db_password = "cnu616"
    #
    database_info = query_database_info(db_host, db_port, db_uesrname, db_password)
    print("database_info:\n",database_info)
    #
    db_name = database_info.get("database_name")[5]
    mySQLDBManagement = MySQLDBManagement(db_host, db_port, db_uesrname, db_password, db_name)
    print("datatables:\n", mySQLDBManagement.show_datatables())
    table_info = mySQLDBManagement.query_table_info("guanting_table")
    print("table info:\n", table_info)
    #
##    new_record_list = [('5','TN','Landsat8','2018082500','https://wwww.baidu.com'),
##                       ('6','Chl-a','GOCI','2018082500','https://wwww.baidu.com'),
##                       ('7','TSS','Sentinel2','2018082500','https://wwww.baidu.com')]
##    new_record_list1 = [['11','TN','Landsat8','2018082500','https://wwww.baidu.com']]
    # mySQLDBManagement.insert_record("wq_tabel_01", new_record_list)
