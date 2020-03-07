## DailyFresh

**天天生鲜**：小型电商购物网站，基于Python3.x和Django2.x



## 功能简介：

- 登录注册：用户的登录与注册。
- 生鲜浏览：图片，价格，种类，简介以及库存，评论等信息。
- 全文检索：支持对商品种类以及商品名称，简介的检索。
- 用户中心：可以查看用户订单，收获地址、电话等信息。
- 商品下单：在支付接口和企业资质的支持下可完成商品的下单功能，按照原子事务处理，下单异常则终止此次下单过程。
- 后台管理：支持后台管理功能，商品及用户信息的增加，更新与删除，可自定制样式与功能，日志，以及权限的管理和分配。


## 在线样例：

### 在线地址

[http://39.108.176.210](http://39.108.176.210)


## 预览：

![index](https://raw.githubusercontent.com/weilanhanf/Photos/master/DailyFresh/index.png)



### 数据库配置

数据库默认Django自带的小型数据库<code>sqlite</code>



### 创建超级用户

终端下执行:

<code>./python manage.py createsuperuser</code>

然后输入相应的超级用户名以及密码，邮箱即可。

### 运行

终端下执行:

<code>./python manage.py runserver</code>

浏览器打开: <code>http://127.0.0.1:8000</code> 即可进入普通用户入口

浏览器打开: <code>http://127.0.0.1:8000/admin</code> 即可进入超级用户入口



