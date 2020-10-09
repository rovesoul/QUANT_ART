import tushare as ts
import pandas as pd
import datetime
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 360) # 设置打印宽度(**重要**)

def get_red():
    """分配预案
    year : 预案公布的年份，默认为2014
    top :取最新n条数据，默认取最近公布的25条
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0
    """
    df = ts.profit_data(year=2020, top=60)
    # df.sort('shares', ascending=False)
    print(df)


def fore_data():
    # 获取2014年中报的业绩预告数据
    df = ts.forecast_data(2020, 3)
    print(df)


def fund_hold():
    """
    获取每个季度基金持有上市公司股票的数据。
    year:年份,默认为当前年
    quarter:季度（只能输入1，2，3，4这个四个数字）
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0
    """
    print('返回参数有问题')
    df = ts.fund_holdings(2020, 2)
    print(df)


def new_stock():
    """
    新股数据
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

    code：股票代码           name：股票名称
    ipo_date:上网发行日期    issue_date:上市日期
    amount:发行数量(万股)    markets:上网发行数量(万股)
    price:发行价格(元)       pe:发行市盈率
    limit:个人申购上限(万股)  funds：募集资金(亿元)
    ballot:网上中签率(%)
    """
    df = ts.new_stocks()
    print(df.head(10))
    print(df)
    print(datetime.datetime.today())

if __name__ == '__main__':
    fund_hold()
