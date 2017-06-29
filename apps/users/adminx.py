import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "zhouxy后台管理系统"
    site_footer = "zhouxy"
    menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['username', 'nick_name', 'birthday', 'gender', 'address', 'mobile']
    list_filter = ['username', 'nick_name', 'gender', 'address', 'mobile']
    search_fields = ['username', 'nick_name', 'birthday', 'gender', 'address', 'mobile']


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type']
    search_fields = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index']
    search_fields = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
