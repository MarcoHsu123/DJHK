from django.contrib import admin
import site
from events.models import events ,discussion ,player,joinTeam
# Register your models here.

class playerAdmin(admin.ModelAdmin):
    list_display = ('playerName','email')
    list_filter =  ('playerName',)
    search_fields = ['playerName']
    fields = ('playerName','email')


class eventsAdmin(admin.ModelAdmin):
    list_display = ('title','fromCity','toCity','destination','numbers','startDate','endDate','departTime','createTime','relesseTime')
    fields = ('title','fromCity','toCity','destination','numbers','startDate','endDate','departTime','type','artPhoto','content')
    ordering = ['-relesseTime']

admin.site.register(player,playerAdmin)
admin.site.register(events,eventsAdmin)
admin.site.register(discussion)
admin.site.register(joinTeam)