# coding: UTF-8
"""This script parse stock info"""

import tushare as ts

def get_guba():
    """新浪股吧"""
    df = ts.guba_sina()  # 新浪股吧
    print(df)

def get_area():
    """股票地域，暂时还能用"""
    df =  ts.get_area_classified()
    print(df)


def get_sme():
    """获取中小板股票数据，即查找所有002开头的股票"""
    df = ts.get_sme_classified()
    print(df)


def get_gem():
    """获取创业板股票数据，即查找所有300开头的股票"""
    df = ts.get_gem_classified()
    print(df)

def get_st():
    """获取ST股票"""
    df = ts.get_st_classified()
    print(df)


def get_hs_weight():
    """获取沪深300当前成份股及所占权重"""
    df = ts.get_hs300s()
    print(df)

def get_zz_500():
    '''获取中证500成份股'''
    df = ts.get_zz500s()
    print(df)

def test():
    print(ts.get_index())

if __name__ == '__main__':
    test()

    
   

    
