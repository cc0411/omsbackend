from django.db import models
from datetime import datetime
# Create your models here.
class Assets(models.Model):

    ASSET_STATUS = (
        ('online','上线'),
        ('offline','下线')
    )
    ASSET_TYPE = (
        ('physical', '物理机'),
        ('virtual', '虚拟机'),
        ('instance', '云主机')
    )
    hostname = models.CharField(max_length=32,verbose_name=u'主机名',unique=True,error_messages={'unique':'该主机名已存在，请不要重复添加'})
    server_type = models.CharField(choices=ASSET_TYPE,default='instance',max_length=10,verbose_name=u'服务器类型')
    wip = models.GenericIPAddressField(verbose_name=u'外网地址',unique=True,error_messages={'blank':"WIP不能为空",'unique':"该WIP已存在，请不要重复添加",'invalid':"WIP地址格式错误"})
    nip = models.GenericIPAddressField(verbose_name=u'内网地址',unique=True,error_messages={'blank':"NIP不能为空",'unique':"该NIP已存在，请不要重复添加",'invalid':"NIP地址格式错误"})
    status = models.CharField(max_length=10,choices=ASSET_STATUS,default='offline',verbose_name=u'状态')
    instance_id = models.CharField(max_length=64,verbose_name=u'云服务器id',blank=True,null=True)
    sn = models.CharField(max_length=64,blank=True,null=True,verbose_name=u'SN编号')
    cpu_info = models.CharField(verbose_name=u'cpu信息',max_length=128,blank=True,null=True)
    os = models.CharField(verbose_name=u'系统类型',blank=True,null=True,max_length=64)
    memory = models.SmallIntegerField(verbose_name=u'内存/GB',default=0)
    disk = models.IntegerField(verbose_name=u'硬盘/GB',default=0)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    utime = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    idc = models.ForeignKey('IDC', verbose_name=u'机房',blank=True,null=True,related_name='idc')
    group = models.ManyToManyField('HostGroup',verbose_name=u'主机组',blank=True,null=True,related_name='tag')
    business_unit = models.ForeignKey('BusinessUnit',verbose_name=u'业务线',blank=True,null=True,related_name='businessunit')
    desc = models.CharField(max_length=200, verbose_name=u'描述',blank=True,null=True)
    class Meta:
        verbose_name = u'主机'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.hostname

class BusinessUnit(models.Model):
    """业务线"""
    name = models.CharField(u'业务线', max_length=64, unique=True,error_messages={'unique':'该业务线已存在，请不要重复添加'})
    group = models.ManyToManyField('HostGroup',verbose_name='主机组',blank=True,null=True)
    desc = models.CharField(u'备注', max_length=64, blank=True, null=True)
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'创建时间')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '业务线'
        verbose_name_plural = "业务线"


class RemoteUser(models.Model):
    name = models.CharField(max_length=24,verbose_name=u'名称',unique=True,error_messages={'unique':'该名称已存在，请不要重复添加'})
    username = models.CharField(max_length=12, verbose_name=u'用户名')
    password = models.CharField(max_length=64, verbose_name=u'密码')
    businessunit = models.ForeignKey(BusinessUnit, verbose_name=u'业务线')

    class Meta:
        verbose_name = u'远程用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IDC(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'机房名',unique=True,error_messages={'unique':'该机房已存在，请不要重复添加'})
    ctime = models.DateTimeField(default=datetime.now,verbose_name=u'添加时间')
    desc = models.CharField(max_length=128, verbose_name=u'描述',blank=True, null=True)

    class Meta:
        verbose_name = u'机房'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class HostGroup(models.Model):
    name = models.CharField(max_length=32,verbose_name=u'主机组名',unique=True,error_messages={'unique':'该角色已存在，请不要重复添加'})
    ctime = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    desc = models.CharField(max_length=128,default='',verbose_name=u'描述', blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = u'主机组'
        verbose_name_plural = verbose_name