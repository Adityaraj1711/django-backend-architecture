from django.contrib import admin
from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Portfolio)
admin.site.register(models.Skill)
admin.site.register(models.College)
admin.site.register(models.Certification)
admin.site.register(models.Achievement)
admin.site.register(models.Interest)
admin.site.register(models.Project)
admin.site.register(models.Company)
admin.site.register(models.About)

