from django.contrib import admin

# Register your models here.
from.models import Guest,Guest_ProfilePermission,Language,Categories,Course,Lesson,VideoModel,UserCourses,CourseResource,What_u_learn,Requirements,VideoModels,Quiz
from .models import Levels as GuestLevels 
admin.site.register(Guest_ProfilePermission) 
admin.site.register(Guest) 


admin.site.register(GuestLevels )
admin.site.register(Course)
admin.site.register(VideoModels)
admin.site.register(UserCourses)
admin.site.register(Categories)
admin.site.register(CourseResource)
admin.site.register(Language)
admin.site.register(VideoModel)
admin.site.register(What_u_learn)
admin.site.register(Requirements)
admin.site.register(Quiz)