from django.contrib import admin
from newapp.models import UserProfileInfo,User,DonorProfileInfo



# Register your models here.





class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display=['user','slug']
    prepopulated_fields={'slug':('user',)}

class DonorProfileInfoAdmin(admin.ModelAdmin):
    list_display=['username','slug']
    prepopulated_fields={'slug':('username',)}


admin.site.register(UserProfileInfo,UserProfileInfoAdmin)
admin.site.register(DonorProfileInfo,DonorProfileInfoAdmin)
