from datetime import datetime
from django.db import models


# Create your models here.

class CityDict(models.Model):
    name = models.CharField(verbose_name='城市', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(verbose_name='机构名称', max_length=20)
    desc = models.TextField(verbose_name='机构描述')
    click_nums = models.IntegerField(verbose_name='点击数量', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    image = models.ImageField(verbose_name='封面照片', upload_to='image/org/%Y-%m-%d', max_length=100)
    address = models.CharField(verbose_name='机构地址', max_length=150)
    city = models.ForeignKey(CityDict, verbose_name='城市')

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name='所属机构')
    name = models.CharField(verbose_name='教师名称', max_length=20)
    work_years = models.IntegerField(verbose_name='工作年限', default=0)
    work_company = models.CharField(max_length=50, verbose_name="就职公司")
    work_position = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name
