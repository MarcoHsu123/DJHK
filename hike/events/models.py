from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class player(models.Model):
    playerId = models.AutoField(primary_key=True)
    playerName =  models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    createTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.playerId
    class Meta:
        verbose_name_plural = '玩家'

class events(models.Model):
    event_type =(
        (1,'徒步'),
        (2,'登山'),
        (3,'越野跑'),
        (4,'溯溪'),
        )
   
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,verbose_name='活动名称')
    fromCity = models.CharField(max_length=20,verbose_name='出发地')
    toCity =  models.CharField(max_length=20,verbose_name='到达')
    destination =  models.CharField(max_length=30,verbose_name='目的地')
    numbers = models.SmallIntegerField(verbose_name='人数限制')
    startDate = models.DateField(verbose_name='行程')
    endDate = models.DateField(verbose_name='至')
    departTime = models.DateTimeField(verbose_name='集合时间')
    type = models.SmallIntegerField(verbose_name='活动类型',choices=event_type)
    artPhoto = models.ImageField(verbose_name='活动图片',blank = True ,upload_to='artphoto/')
    content = RichTextUploadingField(verbose_name='活动内容')
    initiator = models.CharField(max_length=20,blank = True)
    initiatorId = models.SmallIntegerField(default = 0) #models.ForeignKey(player,on_delete=models.PROTECT)
    createTime = models.DateTimeField(auto_now_add=True)
    modifyTime = models.DateTimeField(auto_now=True)
    relesseTime = models.DateTimeField(blank=True,verbose_name='发布时间',null= True)
    status = models.SmallIntegerField(default = 0)
    
    class Meta:
        verbose_name_plural = '活动管理'
        
class joinTeam(models.Model):
    teamId = models.AutoField(primary_key=True)
    eventsId = models.ForeignKey(events,on_delete=models.PROTECT)
    playerId = models.ForeignKey(player,on_delete=models.PROTECT)
    playerName = models.CharField(max_length=30)
    isInit = models.BooleanField(blank=True)
    applicationTime = models.DateTimeField()
    auditTime = models.DateTimeField(blank=True)
    state = models.SmallIntegerField()
    
    class Meta:
        verbose_name_plural='活动组队'

class discussion(models.Model):
    messageId = models.AutoField(primary_key=True)
    eventsId = models.ForeignKey(events,on_delete=models.PROTECT)
    playerId = models.ForeignKey(player,on_delete=models.PROTECT)
    playerName = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    subTime = models.DateTimeField()
    replyWho =  models.IntegerField()
    replyMessageId =  models.IntegerField()

    class Meta:
        verbose_name_plural='讨论组'