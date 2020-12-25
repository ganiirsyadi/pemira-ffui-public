from django.contrib import admin
from .models import Voter
from django.forms import ModelForm

# Register your models here.

class AddVoter(ModelForm):

    class Meta:
        model = Voter
        fields = ('email', 'npm' , 'name', 'prodi', 'bukti_foto')

def verify(modeladmin, request, queryset):
    queryset.update(is_verified = True)
    queryset.update(is_active = True)
    queryset.update(is_registered = True)
verify.short_description = "Verifikasi"

def cancel(modeladmin, request, queryset):
    queryset.update(is_verified = False)
    queryset.update(is_active = False)
    queryset.update(is_registered = False)
cancel.short_description = "Batalkan Registrasi"

class VoterAdmin(admin.ModelAdmin):
    form = AddVoter
    list_display = ('name', 'email', 'npm', 'is_registered','is_verified', 'prodi', 'bukti_foto')
    search_fields = ('prodi', 'name', 'npm')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('prodi','-is_registered', '-is_verified', 'name', 'npm')
    actions = [verify, cancel]
    def has_add_permission(self, request, obj=None):
        return True


admin.site.register(Voter, VoterAdmin)