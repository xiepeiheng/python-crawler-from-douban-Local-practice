**<font size=6>零基础使用beautifulsoup4模拟爬取解析豆瓣网Top250电影信息</font>**

由于频繁爬取豆瓣网信息容易被暂时封禁，所以将豆瓣的网页保存下来，使用Flask在本地运营，然后使用`beautifulsoup`练习对网页的解析

## 使用方法

本项目分为三个部分，来循序渐进的最终掌握如何使用beautifulsoup来爬取豆瓣网页

### 第一部分

首先是使用**[beautifulsoup中文文档]([Beautiful Soup 4.4.0 文档 — Beautiful Soup 4.2.0 中文 文档](https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/#))**提供的`Alice`样例学习beautifulsoup的使用方法

练习方法是首先运行`sever`文件夹中的`app.py`，然后运行`crawler`文件夹中的`alice crawler.py`尝试进行爬取练习。爬取的本地地址是`http://127.0.0.1:5000/alice`

同时`crawler`文件夹中有名为`beautifulsoup note.md`的文件是我学习beautifulsoup中文文档时记的笔记，方便遗忘时快速查阅

### 第二部分

在基本掌握beautifulsoup的使用方法后尝试爬取解析由Flask驱动的[**豆瓣电影 Top 250**](https://movie.douban.com/top250)的内容。因为直接练习过多的爬取会导致被临时封禁，所以将前两页内容保存至本地，再使用Flask本地运行。作为样例的两页网页在Flask运行后的地址分别是`http://127.0.0.1:5000/0`和`http://127.0.0.1:5000/25`

首先运行`sever`文件夹中的`app.py`，然后运行`crawler`文件夹中的`douban1 crawler.py`即可完成爬取工作。爬取并解析后的数据存储在名为`movie1.db`的sqlite3数据库中

同时`crawler`文件夹中有名为`douban note.md`的文件是在学习是做的笔记，可供参考

### 第三部分

在完成前两步的练习后，就可以进行实战演练了。运行运行`crawler`文件夹中的`douban2 crawler.py`即可爬取全部相关数据。爬取并解析后的数据存储在名为`movie2.db`的sqlite3数据库中





