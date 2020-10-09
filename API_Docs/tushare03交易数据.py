# coding: UTF-8
"""This script parse stock info"""

import tushare as ts


def get_day_data(code = '600848'):
    """
    参数较多，周月日，都在里边了，详细看下边连接
    http://tushare.org/trading.html
    """
    type='W'
    df = ts.get_hist_data(code, ktype='W')
    print(df)

def test():
    print(ts.get_hist_data('600848', ktype='W')) 

if __name__ == '__main__':
    test()