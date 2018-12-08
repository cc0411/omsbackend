from django.db import models
from django.contrib.auth import get_user_model
from assets.models import Assets
import uuid
# Create your models here.

User = get_user_model()
class SshLog(models.Model):
    asset = models.ForeignKey(Assets,verbose_name='主机')
    channel = models.CharField(max_length=100,blank=False,unique=True,editable=False)
    log = models.UUIDField(max_length=100,default=uuid.uuid4,blank=False,unique=True,editable=False)
    start_time = models.DateTimeField(auto_now_add=True,verbose_name='开始时间')
    end_time = models.DateTimeField(auto_created=True,auto_now=True,verbose_name='结束时间')
    is_finished = models.BooleanField(default=False,verbose_name='是否完成')
    user = models.ForeignKey(User,verbose_name='用户')
    width = models.PositiveIntegerField(default=90,verbose_name='宽度')
    height = models.PositiveIntegerField(default=40,verbose_name='高度')
    def __str__(self):
        return self.asset.wip
