from django.db import models
from datetime import datetime
# Create your models here.


class Project(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32,verbose_name='项目名称',unique=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '项目'
        verbose_name_plural = verbose_name

State_choices = (
    ('AVAILABLE','可用'),
    ('UNAVAILABLE','不可用')
)
class Region(models.Model):
    region = models.CharField(max_length=32,verbose_name='大区ID',unique=True)
    name = models.CharField(max_length=64,verbose_name='大区名称')
    state = models.CharField(max_length=32,choices=State_choices,verbose_name='RegionState',)
    ctime = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    utime = models.CharField(max_length=50, verbose_name='最近一次更新时间', blank=True, null=True)
    def __str__(self):
        return self.region
    class Meta:
        verbose_name = 'Region列表'
        verbose_name_plural = verbose_name

class Zone(models.Model):
    region = models.ForeignKey(Region,verbose_name='大区ID')
    zone = models.CharField(max_length=64,verbose_name='可用区',unique=True)
    name = models.CharField(max_length=64,verbose_name='可用区名')
    zid = models.IntegerField(verbose_name='可用区ID',primary_key=True)
    state = models.CharField(max_length=32,choices=State_choices,verbose_name='ZoneState')
    ctime = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    utime = models.CharField(max_length=50, verbose_name='最近一次更新时间', blank=True, null=True)

    def __str__(self):
        return self.zone
    class Meta:
        verbose_name = 'Zone列表'
        verbose_name_plural = verbose_name

class Image(models.Model):
    region = models.ForeignKey(Region,verbose_name='大区ID')
    imageid = models.CharField(max_length=32,verbose_name='镜像ID',unique=True)
    os = models.CharField(max_length=64,verbose_name='操作系统')
    size = models.IntegerField(verbose_name='镜像大小')
    type = models.CharField(max_length=64,verbose_name='镜像类型')
    state = models.CharField(max_length=32,verbose_name='镜像状态')
    source = models.CharField(max_length=32,verbose_name='镜像源')
    code = models.CharField(max_length=64,verbose_name='ProductCode',blank=True,null=True)
    name = models.CharField(max_length=64,verbose_name='镜像名')
    des = models.CharField(max_length=64,verbose_name='镜像描述')
    init = models.BooleanField(verbose_name='是否初始化',default=False)
    platform = models.CharField(max_length=32,verbose_name='系统类型')
    arch = models.CharField(max_length=32,verbose_name='系统位数')
    ctime = models.DateTimeField(default=datetime.now, verbose_name='创建时间')
    utime = models.CharField(max_length=50, verbose_name='最近一次更新时间', blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "镜像"
        verbose_name_plural = verbose_name

class InstancesType(models.Model):
    region = models.ForeignKey(Region, verbose_name='大区ID')
    zone = models.CharField(max_length=32,verbose_name='可用区')
    family = models.CharField(max_length=32,verbose_name='实例机型系列')
    type = models.CharField(max_length=32,verbose_name='实例机型')
    cpu = models.IntegerField(verbose_name='CPU')
    memory = models.IntegerField(verbose_name='内存')
    def __str__(self):
        return self.type
    class Meta:
        verbose_name = '实例机型'
        verbose_name_plural =verbose_name
        unique_together = ('family','type','zone')


class Instances(models.Model):
    Restrict_choices = (
        ('NORMAL','正常状态'),
        ('EXPIRED','已过期'),
        ('PROTECTIVELY_ISOLATED','已被隔离')
    )
    ChangeType_choices = (
        ('PREPAID','预付费'),
        ('POSTPAID_BY_HOUR','后付费'),
        ('CDHPAID','CDH付费')
    )
    Renew_Choices=(
        ('NOTIFY_AND_MANUAL_RENEW','要过期不续费'),
        ('NOTIFY_AND_AUTO_RENEW','要过期自动续费'),
        ('DISABLE_NOTIFY_AND_MANUAL_RENEW','不通知过期续费')

    )
    InstanceState_Choices =(
        ('PENDING','在创建'),
        ('RUNNING','在运行'),
        ('STOPPED','关机'),
        ('STARTING','在开机'),
        ('STOPPING','在关机'),
        ('REBOOTING','在重启'),
    )
    region = models.ForeignKey(Region, verbose_name='region')
    placement = models.CharField(max_length=32,verbose_name='所在位置')
    project = models.CharField(max_length=32,verbose_name='项目')
    instance_id = models.CharField(max_length=64,verbose_name='实例ID',unique=True)
    instancestate = models.CharField(max_length=32,choices=InstanceState_Choices,verbose_name='实例运行状态')
    restrictstate = models.CharField(max_length=32,choices=Restrict_choices,default='NORMAL',verbose_name='实例业务状态')
    type = models.CharField(max_length=32,verbose_name='实例机型')
    cpu = models.IntegerField(verbose_name='CPU核数/核')
    memory = models.SmallIntegerField(verbose_name='内存/G')
    name = models.CharField(max_length=32,verbose_name='实例名称')
    systemdisk = models.CharField(max_length=128,verbose_name='系统盘信息')
    datadisk = models.CharField(max_length=128,verbose_name='数据盘信息',blank=True,null=True)
    nip = models.GenericIPAddressField(verbose_name='内网地址')
    wip = models.GenericIPAddressField(verbose_name='公网地址')
    chargetype = models.CharField(max_length=32,choices=ChangeType_choices,default='PREPAID',verbose_name='实例计费模式')
    bandwith = models.CharField(max_length=64,verbose_name='带宽信息')
    securityid = models.CharField(max_length=32,verbose_name='安全组')
    image = models.CharField(max_length=32,verbose_name='镜像')
    os = models.CharField(max_length=32,verbose_name='操作系统')
    renewflag = models.CharField(max_length=32,choices=Renew_Choices,verbose_name='自动续费标识')
    ctime = models.CharField(max_length=64,verbose_name='创建时间')
    etime = models.CharField(max_length=64,verbose_name='过期时间')
    def __str__(self):
        return self.instance_id
    class Meta:
        verbose_name = '实例信息'
        verbose_name_plural = verbose_name










