# coding: UTF-8
"""This script parse stock info"""

import tushare as ts


def get_all_price(code_list):
    '''按列表内容获取stk实时数据'''
    df = ts.get_realtime_quotes(STOCK)
    print(df)


if __name__ == '__main__':
    STOCK = [
        'sh510880',  # 510880
        'sh',        # 指数
    ]

    get_all_price(STOCK)

    # df = ts.get_realtime_quotes('sh510880') #Single stock symbol
    # print(df)
