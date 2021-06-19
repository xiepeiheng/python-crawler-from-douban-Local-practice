import re
import urllib.error
import urllib.request
from bs4 import BeautifulSoup
import sqlite3


# findLink = re.compile(r'<a href="(.*?)">')
# findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # 忽略换行的情况
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
# findInq = re.compile(r'<span class="inq">(.*)</span>')
# findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

def main():
    basic_url = 'https://movie.douban.com/top250?start='
    data = getdata(basic_url)
    savepath = 'C:/Users/谢佩恒/Desktop/crawler/movie2.db'
    savedate(data, savepath)

def getdata(url):
    datalist = []  # 存储全部爬取的数据
    num = 0  # 显示目前完成了几条存储
    for i in range(0, 10):  # 一共两页，逐页提取
        uurl = url + str(i * 25) + '&filter='
        print(f'目前所在网址{uurl}')
        html = askurl(uurl)
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', class_='item'):
            data = []  # 保存一部电影的所有信息

            # 存储中文名和外文名
            name = item.find_all('span', class_='title')  # 找到的东西会保存在数组里，以逗号分隔
            if len(name) == 2:
                data.append(name[0].string)
                data.append(name[1].string.replace(u'\xa0/\xa0', u''))
            else:
                data.append(name[0].string)
                data.append(' ')

            # 存储详情页的网址
            movie_url = item.a.get('href')
            data.append(movie_url)

            # 存储分数
            score = item.find(
                'span', class_='rating_num').string
            data.append(score)

            # 存储评价人数
            people_num = item.find('div', class_='star').select("div > span:nth-of-type(4)")
            abcd = re.findall('(\d*)人评价', people_num[0].string)[0]
            data.append(abcd)

            # 存储一句话简介
            abc = item.find('span', class_='inq')
            if abc is not None:
                abc = abc.string
            data.append(abc)

            datalist.append(data)  # 将包含电影全部信息的数组加入总数组中
            num = num + 1
            print(f'已完成{num}条')

    # print(datalist)
    return datalist


# 获取网页
def askurl(url):
    # head告诉服务器我的机器的基本情况和我可以接收的内容
    # head中的键值对必须和真实浏览器上的数据完全一致，比如"User-Agent"不能写为"User - Agent"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"}
    request = urllib.request.Request(url, headers=head)
    try:
        response = urllib.request.urlopen(request)
        abc = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return abc


def savedate(datalist, savepath):
    # 建表

    init_db(savepath)



    conn = sqlite3.connect(savepath)
    cur = conn.cursor()



    for data in datalist:
        sql = '''
            insert into movie250(
                chinese_name,
                foreign_name,
                info,
                score,
                num,
                recommend
            )
        values(
            ?,
            ?,
            ?,
            ?,
            ?,
            ?
        )
        '''
        cur.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5]))
    conn.commit()
    cur.close()
    conn.close()


def init_db(savepath):

    sql = '''
        create table movie250
        (
        id integer primary key autoincrement,
        chinese_name text,
        foreign_name text,
        info text,
        score text,
        num text,
        recommend text
        )
    '''
    conn = sqlite3.connect(savepath)
    cursor = conn.cursor()
    # 判断数据库中是否含有表，如果有就删掉，没有就创建
    num = cursor.execute('select count(*) from sqlite_master where name = "movie250"')
    jsk = 0
    for i in num:
        jsk = i[0]
    if jsk == 1:
        cursor.execute('DROP TABLE movie250')
    cursor.execute(sql)
    conn.commit()
    conn.close()


main()
