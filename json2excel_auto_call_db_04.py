import json, xlwt
from collections import OrderedDict
import os
import db_utils


def to_order_dict(origin_dict, custom_list):
    for key1, value1 in origin_dict.items():  # 当字典的key值为时间的话
        if key1 in custom_list:  # 将字典中的值保存到字典中，筛选需要的字典
            origin_dict[key1] = value1
    order_dict = OrderedDict()
    for key in custom_list:  # 获取orderdict，自定义顺序的字典
        if key in origin_dict.keys():
            order_dict[key] = origin_dict.get(key)
    return order_dict


def write_order_dict(sheet, order_dict, y):
    x = 0  # 循环字典，打印值
    for key, value in order_dict.items():
        sheet.write(x, y, key)
        sheet.write(x, y + 1, value)
        x = x + 1


def get_time(book, json_data, sheet_name, field_list):
    sheet_time = book.add_sheet(sheet_name, cell_overwrite_ok=True)  # 添加一个sheet页
    order_dict_01 = to_order_dict(json_data, field_list)
    write_order_dict(sheet_time, order_dict_01, 0)
    for key, value in json_data.items():
        if isinstance(value, list):
            y = 2
            for index, inner_dict in enumerate(value):  # 获取list中数据
                order_dict = to_order_dict(inner_dict, field_list)
                write_order_dict(sheet_time, order_dict, y)
                y = y + 2


def write_content(content, alist):
    json_data = json.loads(content)
    call_id = json_data['callid']

    book = xlwt.Workbook()  # 创建一个excel对象
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页
    i = 0
    for key, value in json_data.items():
        if key not in alist:
            i = i + 1
            if isinstance(value, list):
                j = 1
                for index, l_value in enumerate(value):
                    j = j + 2
                    k = 12
                    for key1, value1 in l_value.items():
                        if key1 not in alist:
                            sheet.write(k, j, key1)
                            sheet.write(k, j + 1, value1)
                            k = k + 1
            else:
                sheet.write(i, 0, key)
                sheet.write(i, 1, value)
    # 获取时间
    get_time(book, json_data, 'Sheet_time01', alist)

    book.save(call_id + '.xls')


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


def get_files_of_dir(file_dir):
    file_list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list  # 当前路径下所有非目录子文件


def get_root_of_dir(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root  # 当前目录路径


if __name__ == '__main__':

    all_list = ['callStartTime', 'callAnswerTime', 'callEndTime', 'userCallDuration', 'Ring', 'RingTime',
                'Begin', 'End',
                'AgentRing',
                'AgentRingEnd', 'AgentHangup',
                'InboundIVREndTime', 'QueueTime', 'QueueEndTime', 'btime', 'altime', 'antime', 'botResponseTime',
                'etime', 'createTime', 'duration', 'hangupdir']

    content_list = db_utils.connect_newfs_bt()
    for content in content_list:
        write_content(content, alist=all_list)
