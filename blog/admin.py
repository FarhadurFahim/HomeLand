from django.contrib import admin
from .models import Post
#from blog.models import UserProfile
from .models import UserProfile

# Register your models here.
admin.site.register(UserProfile)

admin.site.register(Post)
