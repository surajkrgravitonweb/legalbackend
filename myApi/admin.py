from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(UserForm)
admin.site.register(Document)
admin.site.register(UserOutput)
admin.site.register(AllPagesApi)
admin.site.register(AllPAgesByAgentControl)
admin.site.register(UserFormDocument)





