from django.contrib import admin
from receive.models import SoundOrigin, ImageOrigin, CurrentOrigin, VoltageOrigin, RobotOrigin, UpdataTime
# Register your models here.

admin.site.register(UpdataTime)
admin.site.register(SoundOrigin)
admin.site.register(CurrentOrigin)
admin.site.register(VoltageOrigin)
admin.site.register(ImageOrigin)
admin.site.register(RobotOrigin)
