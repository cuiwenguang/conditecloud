from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    """租户基础信息表"""
    name = models.CharField(max_length=100)  # 企业名称
    contracts = models.CharField(max_length=20)  # 联系人
    mobile = models.CharField(max_length=20)  # 联系电话
    created_on = models.DateField(auto_now_add=True)  # 注册日期
    is_active = models.BooleanField()  # 是否激活
    expire_date = models.DateTimeField()  # 过期时间
    address = models.CharField(max_length=200, null=True, blank=True)  # 地址
    site_url = models.CharField(max_length=200, null=True, blank=True)  # 企业网址
    secret = models.UUIDField(auto_created=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = False


class Payment(models.Model):
    """支付信息表"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    paid_date = models.DateTimeField()  # 付款日期
    total_money = models.DecimalField(max_digits=8, decimal_places=2)  # 付款总金额
    pay_type = models.CharField(max_length=10)  # 支付方式，微信，支付宝，转账，现金
    remark = models.CharField(max_length=100)  # 备注

