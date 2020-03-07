from django.db import models

from df_user.models import UserInfo
from df_goods.models import GoodsInfo
# 当一对多关系时例如生鲜分类对生鲜具体商品， 将关系维护在多的那张表中，即在具体商品表中维护
# 当多对多关系，则新建一张表，在再第三张表中维护表关系
# 用户表与商品表则将关系维护在购物车表中

# 在购物车的逻辑删除与物理删除  选择物理删除，
# 购物车中的商品不属于重要的信息，可以直接删除


class CartInfo(models.Model):
    # verbose_name 获取字段名  on_delete=models.CASCADE联级删除，当从表数据删除时，主表数据也删除
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="用户")
    goods = models.ForeignKey(GoodsInfo, on_delete=models.CASCADE, verbose_name="商品")
    count = models.IntegerField(verbose_name="", default=0)  # 记录用户买个多少单位的商品

    # 元选项，自定义表的名字，默认名字为 < app_name > _ < model_name


    class Meta:
        verbose_name = "购物车"       # 指定在admin管理界面中显示中文
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.uname + '的购物车'     # verbose_name_plural表示复数形式的显示；
                                               # 中文的单数和复数一般不作区别。



