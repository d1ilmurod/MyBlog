from django.contrib import admin
from .models import Blog,MyBooks,AboutMe,Contact

# Register your models here.
admin.site.register(Blog)
admin.site.register(MyBooks)
admin.site.register(AboutMe)
admin.site.register(Contact)