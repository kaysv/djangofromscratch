from django.contrib import admin
from .models import Profile,Article
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    models = Profile
    list_display = (
            'id',
             'user',
             'image',
             'name',
             'title',
             'address',
             'email',
             'phone',
             'created_at'
             )

class ArticleAdmin(admin.ModelAdmin):
    models = Article
    list_display=(
                'id',
                'name',
                'title'
    )

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Article,ArticleAdmin)
