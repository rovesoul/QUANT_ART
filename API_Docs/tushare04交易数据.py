import tushare as ts

"""历史行情数据
复权历史数据
实时行情数据
历史分笔数据
实时报价数据
当日历史分笔
大盘指数列表
大单交易数据
"""


def get_history(code='600848'):
    """
    参数较多，周月日，都在里边了，详细看下边连接
    http://tushare.org/trading.html
    """
    type = 'W'
    df = ts.get_hist_data(code, ktype='W')
    print(df)


def get_first_market():
    """上市首日
    http://tushare.org/trading.html#id3

    """
    # 获取首个上市日期
    df = ts.get_stock_basics()
    date = df.ix['600848']['timeToMarket']  # 上市日期YYYYMMDD
    print(date)


def get_all_today():
    """获得今日全部股票数据
    作废
    """
    print('本接口旧版作废了')
    df = ts.get_today_all()
    print(df)


def tick():
    """获取个股以往交易历史的分笔数据明细，通过分析分笔数据，可以大致判断资金的进出情况。
    在使用过程中，对于获取股票某一阶段的历史分笔数据，需要通过参入交易日参数并append到一个DataFrame或者直接append到本地同一个文件里。
    历史分笔接口只能获取当前交易日之前的数据，当日分笔历史数据请调用get_today_ticks()接口或者在当日18点后通过本接口获取。
    """
    df = ts.get_tick_data('600848', date='2020-10-09', src='tt')
    print(df)


def indexs():
    """获取指数数据"""
    df = ts.get_index()
    print(df)


def bigs():
    """大于400手的大单
    参数说明：
    code：股票代码，即6位数字代码
    date:日期，格式YYYY-MM-DD
    vol:手数，默认为400手，输入数值型参数
    retry_count : int, 默认3,如遇网络等问题重复执行的次数
    pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题"""
    df = ts.get_sina_dd('600848', date='2020-10-09', vol=500)  # 默认400手
    print(df)


def test():
    print(ts.get_hist_data('600848', ktype='W'))


if __name__ == '__main__':
    bigs()
