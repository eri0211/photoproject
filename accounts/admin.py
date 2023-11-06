from django.contrib import admin

# CustomUserをインポート
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス
    
    '''
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

admin.site.register(CustomUser, CustomUserAdmin)