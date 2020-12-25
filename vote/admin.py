from django.contrib import admin
from .models import Vote, Vote2

# Register your models here.

class VoteAdmin(admin.ModelAdmin):
    list_display = ('get_voter_name', 'get_voter_email', 'get_voter_prodi', 'datetime_vote')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    search_fields = ('user__prodi',)
    ordering = ('datetime_vote',)
    def get_voter_name(self, obj):
        return obj.user.name
    def get_voter_prodi(self, obj):
        return obj.user.prodi
    def get_voter_email(self, obj):
        return obj.user.email
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Vote, VoteAdmin)
admin.site.register(Vote2, VoteAdmin)