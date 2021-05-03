#!/usr/bin/python3
from pymysql import connect


def connect_newfs_bt():
    # 打开数据库连接
    db = connect(host="192.168.180.104", port=3306, user="test", password="test123456", db="newfs_bt", charset="utf8")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句

    sql = """
    SELECT content from push_fail_log WHERE callid in('202124823881658040517','202124823881658040519','202124823881658040520');
    """
    sql = """
    SELECT content from push_fail_log WHERE callid in('202124823881658040522','202124823881658040523','202124823881658040524');
        """
    sql = """
    SELECT content from push_fail_log WHERE callid in('202124823881658040525','202124823881658040526','202124823881658040527','202124823881658040528');
        """
    sql = """
    SELECT content from push_fail_log WHERE create_time >=UNIX_TIMESTAMP('2021-04-29 17:30:00') ORDER BY id ;
    """
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

            # # 打印结果
            # print("content=%s" % \
            #       (content))
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接
    db.close()
    return content_list


if __name__ == '__main__':
    connect_newfs_bt()
