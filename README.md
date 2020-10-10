## Tushare接口
[tushare官网](http://tushare.org/)

### 记录调用接口学习笔记如下
- [获取实时数据](API_Docs/tushare01.py) 通过股票列表获得实时数据
- [股票分类数据这个文档](API_Docs/tushare02-message.py) 比较鸡肋：新浪股吧 & 股票地域 & 中小板分类 & 沪深300 & 中证500
- [股票基本面数据](API_Docs/tushare03基本面数据.py) 获取上市公司基本情况信息 & 业绩报告 & 盈利能力 & 成长能力 & 偿债能力 & 现金流量
- [股票交易数据](API_Docs/tushare04交易数据.py) 日周月k线等数据 & 上市首日 & 分笔数据 & 获取指数数据 & 大于400手的大单 
- [投资参考数据](API_Docs/tushare05投资参考数据.py) 分红预案 & 业绩预告 & 新股数据 &获取每个季度基金持有上市公司股票的数据
- [十年国债收益率](API_Docs/十年国债.py) 爬到中国十年国债收益率
### 作废接口
```python
df = ts.get_latest_news()  # 默认获取最近80条新闻数据，只提供新闻类型、链接和标题
df = ts.get_notices()  # 信息地雷
df = ts.get_sz50s()  # 上证50接口
df = ts.get_terminated() # 终止上市的
df = ts.get_suspended() # 暂停上市的
df = ts.get_today_all() # 获取今日全部数据

# 需要用pro接口 
df =  ts.get_industry_classified() # 行业列表
df =  ts.get_concept_classified() # 概念板块分类
```
## Tushare-Pro接口
- [Pro官网](https://tushare.pro/document/2?doc_id=27)
- [数据索引页面](https://tushare.pro/document/2?doc_id=209) 查看所有数据类、经济类的链接
```python
# 通用初始化代码
ts.set_token('your token here')
pro = ts.pro_api()
data = pro.some_func()
data.head()
```






## 策略&选股
### 记录策略笔记如下
- [待定](Strategy_Docs)
- [指标汇总](指标汇总.md)
### 选股
"连续5年ROE大于18%，连续5年净利润现金含量大于70%，连续3年派息比率大于22%，资产负债率小于60%，连续5年毛利率大于30%，上市大于三年"

> - v1.2.  `update：20201010` tushare接口研究(续)
> - v1.1.  `update：20201009` tushare接口研究