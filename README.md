## 关于本项目 :octocat:
- 分布式微博爬虫,为微博数据抓取而生
- 欲实现内容包括用户信息、微博信息、微博搜索、微博评论和微博转发关系抓取等
- 该项目本来是我们项目组的一个子模块，作用是舆情分析。整个系统比较庞大，我只能开源自己写
的代码部分，希望能帮到对微博数据采集有需求的同学，对爬虫进阶感兴趣的同学也可以看看。该项目
*从模拟登陆到各个页面的请求*、*从简单页面到复杂页面解析处理和相关的异常处理*、
*从单机到分布式迁移*都做了大量的工作和反复测试，花了我绝大部分业余的时间。
- 本项目不会承诺每天能抓到多少数据，因为数据量的大小很大程度上取决于用户可用微博账户的数量
- 与该项目类似的项目大概有[SinaSpider](https://github.com/LiuXingMing/SinaSpider),[weibo_terminater](https://github.com/jinfagang/weibo_terminater)。
前者是一个基于```scrapy```的项目，爬的是移动版微博用户信息，质量还不错；后者嘛,还是用户
自己判断吧。

## 你可以用它来干嘛 :star:
- 微博舆情分析，比如是**热门微博转发分析**
- 微博数据分析，比如基于**微博用户信息**的分析
- 论文撰写的一些数据
- 自然语言处理的**语料**
- **爬虫进阶学习**

## 为何选择本项目 :u6709:
- 项目爬取的是PC端的微博信息，那么为何不采集移动端的呢？虽然它的限制更少，并且解析
的工作量也更小，但是数据采集经验比较丰富的同学应该也知道**移动端的微博和用户信息并不全面**，
所以在项目设计的时候定位就是**PC端的微博数据采集**。
- 稳定！项目可以长期稳定运行。在速度和稳定性之间，项目选择了后者。并且对于抓取微博和解析微博
可能出现的大量异常，都在项目中处理了。对于IP和账号的安全性，本项目也做了一定的考虑，因为现在
购买微博账号的成本也越来越高了。
- 复用性和二次开发性很好。项目很多地方都有详细的代码注释，方便阅读。即使本项目不能完全满足你
对微博数据采集和分析的需求，你也可以自己在该项目的基础上做二次开发，项目已经在微博抓取和各个
模版解析上做了大量工作。
- 由于本项目与本人实际工作挂钩，所以可以放心它会长期更新。目前已经迭代近一年了。


## TODO :dart:
- 微博内容抓取相关
  - [x] 模拟登陆
  - [x] 微博常见用户和企业用户信息抓取：通过粉丝和关注进行增量式抓取
  - [ ] 微博搜索功能：正在开发
  - [ ] 指定用户的主页：主要是微博内容
  - [ ] 指定微博的评论：主要是热门微博
  - [ ] 指定微博的转发情况：主要是热门微博

- 反爬虫相关
  - [ ] 测试单机单账号访问阈值
  - [ ] 测试单机多账号访问效果
  - [ ] 验证不同模块，微博系统的容忍度是否相同
  - [ ] 验证UA头使用百度、Google等搜索引擎的时候请求是否放宽了：先通过寻找哪些内容是不用
 登录就能查看的，这一点主要是从移动端找，因为PC端限制更加严格，然后伪装UA测试请求量。在这个
 基础上再使用登录的账号测试
  - [x] 验证登录状态的cookies和代理ip是否可以成功抓取：测试结果是可以使用登录后的cookie
 从别的地方进行数据采集，根据这一点，可以考虑使用代理IP，但是代理IP的质量和稳定性可能会
 有问题，可能需要找一个或者自己写一个**高可用**的代理池，这一点还**有待考察**)
  - [ ] 验证移动端登录cookie和pc端是否可共享，如果可以共享则为PC端大规模抓取提供了可能
  - [x] 比较单IP和单账号哪个的限制更多，从而制定更加高效的数据采集方案：测试得知，经常是
 账号被封了，然后同一个IP用别的账号还能登陆，所以账号的限制比IP更加严格

- 其它
  - [ ] 已有代码修改：将存储后端从Oracle转向Mysql
  - [x] 优化代码，让程序运行更加快速和稳定：水平有限，已经优化过一次了。下一次可能
    要等一段时间了
  - [x] 修复某些时候抓取失败的问题(已添加重试机制)
  - [x] 改成分布式爬虫(使用celery做分布式任务调度和管理)
  - [ ] 完善文档，包括注明python版本，怎么快速**创建虚拟环境**，怎么**安装相关依赖库**；讲解**celery
    的基本概念和用法**，为不会python的同学提供使用的可能性;讲解微博的反爬虫策略;各个```tasks```模块的作用
    和使用方法
  - [ ] 完善代码注释，方便用户做二次开发
  - [ ] 直接使用dockerfile部署项目
  - [ ] 支持单个任务执行，在执行单个任务(比如分析指定微博的传播)的时候使用进度条
  - [ ] 可视化展示某条微博具体传播信息，微博用户信息等。这个优先级会比较低，目前重点
    解决数据抓取和复杂页面解析的问题

## 项目结构 :bell:

- 功能模块
 - 微博模拟登陆任务[login.py](./tasks/login.py)和[login_first.py](login_first.py)
 - 微博用户抓取任务:[user.py](./tasks/user.py)
 - 微博特定话题搜索任务:[search.py](./tasks/search.py)


```
    config/
        sql/
            spider.sql  # 项目所用表
    db/
        __init__.py
        basic_db.py # 数据库元操作
        login_info.py # 微博账号管理操作
        models.py # sqlalchemy中用到的models
        redis_db.py # redis相关操作，比如管理cookies和urls
        seed_ids.py # 种子用户id管理操作
        user.py # 用户相关操作
    decorator/
        __init__.py
        decorators.py # 项目中用到的装饰器，比如处理超时和模版解析异常
    logger/
        __init__.py
        log.py        # 日志操作
    logs/             # 该目录用于存放日志文件，由于程序没有创建文件夹的权限，所以需要提前建好
    page_get/
        __init__.py
        basic.py      # 基本的数据抓取操作
        user.py       # 微博用户抓取
    page_parse/
        user/
            __init__.py
            enterprise.py # 解析服务号
            person.py     # 解析个人用户
            public.py     # 公共模版解析
    tasks/
        __init__.py
        workers.py        # celery worker
        login.py          # 模拟登陆相关任务
        user.py           # 用户抓取相关任务
    tests/                # 一些解析模版，没多少用
    utils/                # 工具类
    wblogin/
        __init__.py
        login.py          # 微博模拟登陆具体实现
    headers.py            # 请求头，主要是UA
    login_first.py        # 由于celery的定时器会有一定时间的间隔，所以第一次需要手动登陆
    test_wbspider.py      # 没什么用的单元测试
    requirements.txt      # 项目相关依赖

```
有的文件和模块在项目代码中存在，却没有在项目结构中呈现，那么就说明该模块或者该文件还未进行
修改（oracle=>mysql）或者稳定性测试，实现并且测试完成后会补充


## 配置和使用 :sparkles:
- 项目需要的Python解释器环境是Python3.x
- 项目存储后端使用**mysql**，所以需要在存储服务器上安装mysql
- 由于项目是使用[celery](http://docs.celeryproject.org/en/latest/)做分布式任务调度，所以
需要使用broker和各个分布式节点通信，项目使用的是redis，所以需要先安装[redis](https://redis.io/download)。
注意修改redis的配置文件让它能监听除本机外的别的节点的请求，**建议给redis设置密码**，如
果没设置密码，需要关闭保护模式(不推荐，这个**有安全风险**)才能和各个节点通信。
- 由于高版本的celery不支持windows,所以请在**类Unix系统**部署。如果实在需要在windows
上部署的话，可以把celery版本降为3.1.25: ```pip install celery==3.1.25```，这是
celery最后支持的一个windows版本；**特别注意，windows平台上celery的定时功能不可用！
所以如果需要用到定时任务分发的话，请务必将beat部署到linux或者mac上**
- 安装相关依赖```pip install -r requirements.txt```

- 打开[配置文件](./config/spider.yaml)修改数据库和微博账号相关配置
- 打开[sql文件](./config/sql/spider.sql)查看并使用建表语句
- 入口文件：如果有同学有修改源码的需求，那么建议从入口文件开始阅读
 - [login.py](./tasks/login.py)和[login_first.py](login_first.py):微博登
 陆客户端程序
 - [user.py](./tasks/user.py):微博用户抓取程序

- 微博登录和数据采集
 - 下面说明该项目分布式抓取的基本概念和用法:
   - 项目使用了[任务路由](http://docs.celeryproject.org/en/latest/userguide/routing.html)，
   在```tasks/workers```中可以查看[所有的queue](./tasks/worker.py),所以需要在启动
   worker的时候**指定分布式节点的queue**,这个queue的作用就是规定该节点能接什么任务，不会接什么任务。比如我的节点1需要做登录任务和用户信息抓取任务，那么我就
   需要在节点1指定登录任务的queue```login_queue```和抓取用户信息的queue```user_crawler```,
   这里启动worker的语句就应该是```celery -A tasks.workers -Q login_queue,user_crawler worker -l info --concurrency=1 -Ofair```。这样节点1
   就只会执行*模拟登陆*和*用户信息*的相关任务。这样做的好处是：某些任务耗时比较多，就需要更多节点执行，有的耗时小，就不需要这么多节点，比如用户抓取，一个http请求
   只能得到一个用户信息，而对于用户关注和粉丝抓取，一个http请求可以得到几十个关注或者粉丝用户的uid。然后再说说各个启动参数的意思：```-A```指定celery app为
   [```tasks.workers```](./tasks/workers), ```-Q```指定节点1能接受的任务队列是```login_queue```和```user_crawler```，即使你对它发送抓取用户粉丝
   和用户关注的任务(这个任务在该项目中的queue是```fans_followers```,在[tasks.workers](./tasks/workers)中可查看)，它也不会执行。```-l```表示的是日志等级，
   ```--concurrency```是worker的线程数，这里规定为1，celery默认采用多线程的方式实现并发,我们也可以让它使用
   基于异步IO的方式实现并发，具体参考[Celery Concurrency](http://docs.celeryproject.org/en/master/userguide/concurrency/eventlet.html)，
   -Ofair```是避免让celery发生死锁。启动worker的语句需要切换到项目根目录下执行。关于celery更为详细的
   知识请参考[celery的任务路由说明](http://docs.celeryproject.org/en/latest/userguide/routing.html)
   - 如果是**第一次运行该项目**，为了让抓取任务能马上执行，需要在任意一个节点上，切换到项目根目录执行```python
   login_first.py```**获取首次登陆的cookie**，需要注意它只会分发任务到指定了```login_queue```的节点上
   - 在其中一个分布式节点上，切换到项目根目录，再启动beat任务(beat只启动一个，否则会重复执行定时任务)：
   ```celery beat -A tasks.workers -l info```，因为beat任务会有一段时间的延迟(比如登录任务会延迟10个小时再执行)，所以通过```python login_first.py```来获取worker
   首次运行需要的cookie是必须的
   - 通过*flower*监控节点健康状况：先在任意一个节点，切换到项目根目录，再执行```flower -A tasks.workers```，通过'http://xxxx:5555'
   访问所有节点信息，这里的```xxxx```指的是节点的IP

 - 定时登录是为了维护cookie的时效性，据我实验，微博的cookie有效时长为24小时,因此设置定时执行登录的任务频率必须小于24小时，该项目默认10小时就定时登录一次。

 - 为了保证cookie的可用性，除了做定时登录以外(可能项目代码有未知的bug)，另外也**从redis层面将cookie过期时间设置为23小时**，每次更新cookie就重设过期时间


## 常见问题 :question:
1. 问：项目部署好复杂啊，我可以单机而不是单节点运行吗？
答：可以通过单机运行，单机运行的话，需要对代码做少许修改。主要修改方法是找到你需要的功能的
入口文件，然后跟着改，需要改的地方是```@app.task```这些函数的代码。以登录为例，如果需要
单机登录的话，那么就先到[login模块](./tasks/login.py)中把```send_task()```这条语句
去掉，直接改成调用```login_task()```函数即可。这里```send_task()```是网络调用，修改
后就成了本地调用了

2. 关于redis的问题：为什么我在给redis设置密码后，并且把redis设置成了守护进程，但是没起作用？
答：其实这个问题和项目关系不是特别大吧。。。不过考虑到有的同学并不熟悉redis，我这里还是阐明一下，
如果在linux上面搭redis的话，当我们修改了```redis.conf```文件后，我们在启动redis的时候也**需要指定redis.conf
文件**，启动之前，最好把```redis-server```加入到环境变量中。比如我的```redis.conf```放在```/etc/redis```中，
那么我可以通过先切换到```/etc/redis```目录，再通过```redis-server redis.conf```来启动redis server，也可以
直接```redis-server /etc/redis/redis.conf```来启动，前提是 **redis-server**文件需要在环境变量中

3. 这个项目的模拟登陆和抓取的时候是怎么处理验证码的啊？
答：这个项目并没有处理验证码，如果要从工程化的角度来解决微博的验证码的问题，研发成本太高了。但是可以通过一些打码平台，来
解决验证码问题。我们现在做的和要做的工作是如何规避验证码，比如模拟登陆的时候尽量在账号常用地登录，还有一个点就是测试微博
的容忍边界，小于它的阈值做采集就不容易被封（不过速度很慢），毕竟按规矩来被封的风险要小得多。如果有图形图像识别的牛人解决了
验证码的问题，欢迎提PR，帮助更多人。

4. 这个项目能在windows上执行吗？
答：window上可以执行worker节点，beat节点是不可以的，因为windows不支持crontab。如果要混用windows和linux，那么一定
要将celery版本降级为3.1.25。虽然celery4和celery3都可以同时跑，但是这样做flower是没法同时监控两个版本的worker的。

5. 这个项目一天能抓多少数据？
答：这个实在是没办法保证。数据量由你的账号和分布式节点数量决定的，最关键的是账号数量，目前我6个账号，4个节点，每天抓取量大概
2w条，如果需要更快，那么更多的账号是必不可少的。所以用户需要在速度和稳定性上做一些考量。

6. 这个项目解析模块用的是bs,会不会性能很差？
答：本项目的瓶颈不在解析模块上，解析再快，还是会被IO请求所拖累，因为微博服务端对相同cookie的一个时间段的访问次数有限制，而且
bs的解析速度也不算慢了。

其它问题暂时还没发现，如果有朋友在使用中遇到问题，欢迎提issue或者直接加我微信询问，我看到的话都会回答的。


## 其它说明
- 本项目**运行环境是Python3.x**，由于Py2和Py3关于字符编码完全不同，所以如果需要在Py2上运行该程序，需要修改解析模块的相关代码
- 建议**使用linux或者mac**作为worker节点，windows平台也可以作为worker节点，**但是一定不能作为beat节点**，并且celery版本要注意一致。
- 在运行项目之前，需要在数据库中建表，建表语句参见[sql表](./config/sql/spider.sql)，也需要**把自己的多个微博账号存入表(weibo.login_info)中**，把
搜索关键词存入关键词表(keywords)中。这里我已经预插入用户抓取用的一些种子用户了，如果想抓别的用户，请在种子用户表(seed_ids)中做插入操作。等抓取的用户信息
大概十万条时候，我会导出数据，传到本项目中
- 本项目目前默认采用单线程进行抓取，因为多线程和协程等方式抓取会极大增加封号的危险，只能
在速度和稳定性之间进行取舍。可能在~~尝试代理IP有效性后~~弄清楚了微博的反爬虫策略后，可能会采
用多线程(也可能采用非阻塞IO)。目前只能通过分布式的方式来提高抓取速度，分布式目前已经可用，所以具有较强的横向扩展性。
- 如果不需要登录的模块建议就别使用cookie进行抓取，因为这样账号的负载更小。至于哪些信息不需要登录，且是有价值的，这个还会再进行调研，和等待用户的反馈。
- 如果是**开发版，可能会存在运行出问题的情况**，所以建议通过[release](https://github.com/ResolveWang/WeiboSpider/releases)页面下载稳定版
- 文档方面，暂时不会撰写特别详细的文档，[WiKi](https://github.com/ResolveWang/WeiboSpider/wiki)中有一些零散的知识点。等时间宽裕了，会写一个关于该项目的详细使用和
开发教程。如果目前有什么问题，可以给该项目提issue,也可以加我微信交流，我的微信号是
```wpm_wx```，添加的时候请**备注微博爬虫**。
- 项目由于目前是一个人开发的，所以速度比较慢，目前我只会关注自己会用到或者觉得有趣的部分，有别的
需求的朋友可以提feture，如果恰巧也懂Python，**欢迎提PR**
- 如果试用了本项目，**觉得项目还不错的，麻烦多多宣传**啦。觉得项目太渣或是大家有一些有意义、有趣的想法，欢迎
拍砖、吐槽或者**提PR**,作者接受一切有意义的建议和提问。另外，随手点个```star```也是对本人工作的肯定和鼓励:kissing_heart:，
作者也接受捐赠:laughing:。送人玫瑰，手有余香:blush:。


## 如何贡献 :loudspeaker:
- 如果遇到使用中有什么问题，可以在[issue](https://github.com/ResolveWang/WeiboSpider/issues)中提出来
- 代码中如果有逻辑不合理或者内容不完善的地方，可以fork后进行修改，然后Pull Request，如果一经采纳，就会将你加入[contributors](https://github.com/ResolveWang/WeiboSpider/graphs/contributors)
- 欢迎在[issue](https://github.com/ResolveWang/WeiboSpider/issues)中提有意义的future
- 希望有仔细研究过微博反爬虫策略的同学积极提建议

点击查看[贡献者名单](https://github.com/ResolveWang/WeiboSpider/wiki/%E8%B4%A1%E7%8C%AE%E8%80%85%E5%90%8D%E5%8D%95)

## 一点想法 :laughing:
- 目前我有一个比较有趣的想法：我也加了一个QQ群，是关于微博爬虫数据抓取的。看群里很多时候都有
同学在求微博数据，包括用户信息数据、微博数据、评论数据、用户主页微博等等，各种各样的数据。由于
微博限制得比较严格，单人想获取千万级甚至亿级的数据，需要特别大的成本，主要是账号的成本，那么为何
不把数据放共享呢？由于本项目是一个分布式的爬虫程序，所以对数据有要求的同学只需要在自己的服务器或者
本机上跑该程序，把抓取的结果放在一个大家都可以用的地方，人多力量大，采集量自然就多，这样也方便
了自己，方便了别人。当前这也有一些问题，最主要的就是数据如何保护，不会被别人恶意破坏。这个目前
只是一个想法，如果反馈比较热烈，可能在功能都实现得差不多了，会搞这么一个东西，想起来还是比较有意思。

## 赞助本项目:thumbsup:
- [微信或者支付宝打赏作者](https://github.com/ResolveWang/WeiboSpider/wiki/%E6%8D%90%E8%B5%A0%E8%AF%A5%E9%A1%B9%E7%9B%AE)
- [捐赠记录](https://github.com/ResolveWang/WeiboSpider/wiki/%E6%8D%90%E8%B5%A0%E8%AF%A5%E9%A1%B9%E7%9B%AE)

如果本项目对你有用，欢迎对本项目进行捐赠，捐赠时候请留下你的```github ID```，当然您也可以匿名捐赠。

## 致谢:heart:
- 感谢大神[Ask](https://github.com/ask)的[celery](https://github.com/celery/celery)分布式任务调度框架
- 感谢大神[kennethreitz](https://github.com/kennethreitz/requests)的[requests](https://github.com/kennethreitz/requests)库
- 感谢网友 李* 热心测试和提供建议
- 感谢网友 sKeletOn 捐赠
