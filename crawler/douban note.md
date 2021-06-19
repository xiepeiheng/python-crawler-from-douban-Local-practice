# 豆瓣爬虫项目练习笔记



## <font color=orange>项目框架</font>

本项目的步骤如图所示

```flow
st=>start: 开始
op1=>operation: 获取网页HTML代码
op2=>operation: 从代码中爬取信息
op3=>operation: 存入数据库
sp=>end: 结束
st->op1->op2->op3->sp
```

综合以上分析，设置了以下函数。因为页面分布在很多页面上，所以设置一个数组用于存储所有待爬取的网页，在每个for循环内使用`askurl(url)`函数抓取网页HTML代码

```python
basic_url = 'http://127.0.0.1:5000/'
savepath = 'C:\\Users\\谢佩恒\\Desktop\\爬虫训练练习端 - 副本\\movie.db'
data = getdata(basic_url)
savedate(data, savepath)

def getdata(basic_url):
    html = askurl(url)
	……
def askurl(url):
    ……
def savedate(data, savepath):
```



## <font color=orange>使用urllib获取网页</font>

urllib中的`urllib.request.urlopen`方法即可实现最基本的请求发起。但是为了加入`headers`等信息实现最基本的绕过反爬措施的功能，可以利用Request类来构造请求。构造方法如下所示，将`headers`的值变为自身浏览器的值

```python
url = 'http://127.0.0.1:5000/0'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"}
request = urllib.request.Request(url, headers=headers)
```

随后再使用`urlopen`方法发起请求并将得到的数据转换为`utf-8`格式

```python
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
```



## <font color=orange>确定需要爬取的内容块</font>

首先使用`soup = BeautifulSoup(html, 'html.parser')`对网页内容进行解析得到`soup`对象，它是一个复杂的树形结构，包含四种对象类型。其中的`(html, 'html.parser')`意为使用Python自带的`html.parser`解析器进行解析。

对拿到的网页进行分析后可以看出每个`<div class="item">`标签中存储一部电影的全部信息。所以只要找出这页网页中存在的所有`<div class="item">`标签进行解析即可获得全部信息

```html
            <div class="item">
                <div class="pic">
                    <em class="">1</em>
                    <a href="https://movie.douban.com/subject/1292052/">
                        <img width="100" alt="肖申克的救赎" src="./豆瓣电影 Top 250_files/p480747492.webp" class="">
                    </a>
                </div>
                <div class="info">
                    <div class="hd">
                        <a href="https://movie.douban.com/subject/1292052/" class="">
                            <span class="title">肖申克的救赎</span>
                                    <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
                                <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
                        </a>


                            <span class="playable">[可播放]</span>
                    </div>
                    <div class="bd">
                        <p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
                            1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
                        </p>

                        
                        <div class="star">
                                <span class="rating5-t"></span>
                                <span class="rating_num" property="v:average">9.7</span>
                                <span property="v:best" content="10.0"></span>
                                <span>2312755人评价</span>
                        </div>

                            <p class="quote">
                                <span class="inq">希望让人自由。</span>
                            </p>
                    </div>
                </div>
            </div>
```

