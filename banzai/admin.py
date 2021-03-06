# coding: utf-8

from django.contrib import admin

from banzai.models import Package, Report, ReportFBL, Attachment


class ReportInline(admin.StackedInline):

    extra = 0
    model = Report
    verbose_name = u'Отчёт'
    readonly_fields = ('status', 'email', 'reject_code', 'reject_message',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class ReportFBLInline(admin.StackedInline):

    extra = 0
    model = ReportFBL
    verbose_name = u'Отчёт о FBL'
    readonly_fields = ('status', 'email',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class AttachmentInline(admin.StackedInline):

    extra = 0
    model = Attachment
    verbose_name = u'файл'
    readonly_fields = ('name', 'file')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PackageAdmin(admin.ModelAdmin):

    list_display = ('id', 'description', 'status', 'pack_id', 'emails_all',
                    'emails_correct', 'created_on',)
    readonly_fields = ('file', 'status', 'pack_id', 'emails_all',
                       'emails_correct', 'description', 'created_on',)
    inlines = (AttachmentInline, ReportInline, ReportFBLInline,)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Package, PackageAdmin)
