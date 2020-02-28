from django.db import models
from django.contrib import admin
from kb.models import Problem, Solution, Category, Tag
from martor.widgets import AdminMartorWidget

class ProblemAdmin(admin.ModelAdmin):
    
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

class SolutionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(Category)
admin.site.register(Tag)
