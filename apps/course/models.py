from datetime import datetime
from django.db import models


# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(max_length=2, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级')), verbose_name='难度')
    learn_times = models.IntegerField(verbose_name='学习时长(分钟数)', default=0)
    students = models.IntegerField(verbose_name='学生人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    image = models.ImageField(max_length=100, upload_to='image/course/%Y-%m-%d', verbose_name='封面图片')
    click_nums = models.IntegerField(verbose_name='点击人数', default=0)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(verbose_name='章节名称', max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(verbose_name='视频名', max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(verbose_name='名称', max_length=100)
    download = models.FileField(verbose_name='资源文件', upload_to='course/resource/%Y-%m-%d', max_length=100)
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
