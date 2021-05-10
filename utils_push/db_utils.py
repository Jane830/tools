#!/usr/bin/python3
from pymysql import connect


def connect_newfs_bt(timestamp):
    # 打开数据库连接
    db = connect(host="192.168.180.104", port=3306, user="test", password="test123456", db="newfs_bt", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句"
    sql = """
    SELECT content from push_fail_log WHERE create_time >=%s ORDER BY id ;
    """ % timestamp

    content_list = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        # content_list = list(results)
        # print(content_list)
        for row in results:
            content = row[0]
            content_list.append(content)
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return content_list


def connect_newfs_bt_autocall(timestamp, send_url):
    # 打开数据库连接
    db = connect(host="192.168.180.104", port=3306, user="test", password="test123456", db="newfs_bt", charset="utf8")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = """
    SELECT content from push_fail_log WHERE create_time >=%s and send_url like '%s' ORDER BY id ;
    """ % (timestamp, send_url)
    content_list = []
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        print(results)
        # content_list = list(results)
        # print(content_list)
        for row in results:
            content = row[0]
            content_list.append(content)
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return content_list


if __name__ == '__main__':
    connect_newfs_bt_autocall(1620462444, '%print')
