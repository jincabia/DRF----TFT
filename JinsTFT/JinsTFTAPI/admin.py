from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(APIKey)

admin.site.register(Game)
admin.site.register(Tactician)
admin.site.register(TacticianPlacements)
admin.site.register(StaticUnitDetails)
admin.site.register(DynamicUnitDetails)
admin.site.register(StaticTraitDetails)
admin.site.register(DynamicTraitDetails)
admin.site.register(GamePlacements)