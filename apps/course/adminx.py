import xadmin

from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'add_time']
    list_filter = ['name', 'desc', 'degree', 'students']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students']


class CourseResourceAdmin(object):
    list_display = ['course', 'download', 'add_time']
    list_filter = ['course', 'download', 'add_time']
    search_fields = ['course', 'download']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
