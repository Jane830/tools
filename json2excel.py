import json, xlwt
from collections import OrderedDict


# from django.collection import OrderedDict


def readExcel(file):
    with open(file, 'r', encoding='utf8') as fr:
        data = json.load(fr)  # 用json中的load方法，将json串转换成字典
    return data


alist = ['callStartTime', 'callAnswerTime', 'callEndTime', 'Ring', 'RingTime', 'Begin', 'End', 'AgentRing',
         'AgentRingEnd', 'AgentHangup',
         'InboundIVREndTime', 'QueueTime', 'QueueEndTime']

header_list_call = ['callStartTime', 'callAnswerTime', 'callEndTime', 'userCallDuration']
header_list_call_2 = ['Ring', 'RingTime', 'Begin', 'End', 'AgentRing', 'AgentRingEnd', 'AgentHangup',
                      'InboundIVREndTime', 'QueueTime', 'QueueEndTime']
header_list_bot = ['btime', 'altime', 'antime', 'botResponseTime', 'etime', 'createTime', 'duration']


def to_order_dict(origin_dict, custom_list):
    for key1, value1 in origin_dict.items():  # 当字典的key值为时间的话
        if key1 in custom_list:  # 将字典中的值保存到字典中，筛选需要的字典
            origin_dict[key1] = value1
    order_dict = OrderedDict()
    for key in custom_list:  # 获取orderdict，自定义顺序的字典
        if key in origin_dict.keys():
            order_dict[key] = origin_dict.get(key)
    return order_dict


def get_time(book, a, sheet_name, field_list):
    sheet_time = book.add_sheet(sheet_name, cell_overwrite_ok=True)  # 添加一个sheet页
    h = 0
    for key, value in a.items():
        order_dict_01 = to_order_dict(a, field_list)
        write_order_dict(sheet_time, order_dict_01, h)
        # if key in field_list:
        #     sheet_time.write(h, 0, key)
        #     sheet_time.write(h, 1, value)
        #     h = h + 1
        if isinstance(value, list):
            y = 1
            for index, inner_dict in enumerate(value):  # 获取list中数据
                # y = y + 2  # 获取到list中的dict，循环字典;
                # origin_dict = {}
                # for key1, value1 in l_value.items():  # 当字典的key值为时间的话
                #     if key1 in field_list:  # 将字典中的值保存到字典中，筛选需要的字典
                #         origin_dict[key1] = value1
                # order_dict = OrderedDict()
                # for key in field_list:  # 获取orderdict，自定义顺序的字典
                #     if key in origin_dict.keys():
                #         order_dict[key] = origin_dict.get(key)
                order_dict = to_order_dict(inner_dict, field_list)
                write_order_dict(sheet_time, order_dict, y)
                # x = 0  # 循环字典，打印值
                # for key_order, v_order in order_dict.items():
                #     sheet_time.write(4 + x, y, key_order)
                #     sheet_time.write(4 + x, y + 1, v_order)
                #     x = x + 1


def write_order_dict(sheet, order_dict, y):
    y = y + 2
    x = 0  # 循环字典，打印值
    for key, value in order_dict.items():
        sheet.write(4 + x, y, key)
        sheet.write(4 + x, y + 1, value)
        x = x + 1


def writeM(file):
    a = readExcel(file)
    book = xlwt.Workbook()  # 创建一个excel对象
    sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页
    i = 0
    for key, value in a.items():
        if key not in header_list_call:
            # sheet.write(i, 0, key)
            i = i + 1
            if isinstance(value, list):
                j = 1
                for index, l_value in enumerate(value):
                    j = j + 2
                    k = 1
                    for key1, value1 in l_value.items():
                        if key1 not in alist:
                            sheet.write(len(a) - len(header_list_call) + k, j, key1)
                            sheet.write(len(a) - len(header_list_call) + k, j + 1, value1)
                            k = k + 1
            else:
                sheet.write(i, 0, key)
                sheet.write(i, 1, value)
    # 获取时间
    get_time(book, a, 'Sheet_time01', alist)

    book.save(file + '.xls')


if __name__ == '__main__':
    writeM('45')
    # getTime('46')
