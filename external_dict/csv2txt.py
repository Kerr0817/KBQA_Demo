# encoding=utf-8

"""
把从mysql导出的csv文件按照jieba外部词典的格式转为txt文件。
nz代表专名，本demo主要指电影名称。
nr代表人名。

"""
import pandas as pd
# movie名转化
df = pd.read_csv('./movie_title.csv')
title = df['movie_title'].values

with open('./movie_title.txt', 'a', encoding='utf-8') as f:
    for t in title[1:]:
        f.write(t + ' ' + 'nz' + '\n')
# movie名转化
df = pd.read_csv('./person_name.csv')
title = df['person_name'].values

with open('./person_name.txt', 'a', encoding='utf-8') as f:
    for t in title[1:]:
        f.write(t + ' ' + 'nz' + '\n')
