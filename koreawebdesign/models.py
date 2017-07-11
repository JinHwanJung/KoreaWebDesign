from django.db import models
from tagging.fields import TagField
from django.core.urlresolvers import reverse
from .fields import ThumbnailImageField

class Category(models.Model):
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length = 50, unique=True)

    def __str__(self):
        return self.name

class KWD(models.Model):
    title = models.CharField('제목',max_length=100, blank=False, null=False)
    url = models.URLField('URL',unique=True)
    content = models.TextField('간략한 소개', blank=True) # 내용 기록
    create_date = models.DateTimeField('생성 날짜', auto_now_add=True) # 생성 날짜
    modify_date = models.DateTimeField('수정 날짜', auto_now=True) # 수정 날짜
    category = models.ManyToManyField(Category, blank=True, null=True)
    color = models.ManyToManyField(Color,blank=True, null=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m') # 이미지
    tag = TagField()

    class Meta:
        verbose_name = 'KWD'
        verbose_name_plural = 'KWDs'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('koreawebdesign:kwd_detail', args=(self.id,))
