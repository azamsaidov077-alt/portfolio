# # app1/admin.py
# from django.contrib import admin
# from django.utils.html import format_html
# from django.urls import reverse
# from .models import *
#
#
# class SkillInline(admin.TabularInline):
#     model = Skill
#     extra = 1
#     fields = ['name', 'percentage', 'order']
#
#
# class ServiceInline(admin.TabularInline):
#     model = Service
#     extra = 1
#     fields = ['title', 'description', 'icon', 'order']
#
#
# class ProjectInline(admin.TabularInline):
#     model = Project
#     extra = 1
#     fields = ['title', 'description', 'technologies', 'github_url', 'image', 'order']
#     readonly_fields = ['created_at']
#
#
# class ExperienceInline(admin.TabularInline):
#     model = Experience
#     extra = 1
#     fields = ['position', 'company', 'start_date', 'end_date', 'description', 'order']
#
#
# class EducationInline(admin.TabularInline):
#     model = Education
#     extra = 1
#     fields = ['degree', 'institution', 'period', 'field_of_study', 'description', 'order']
#
#
# class SocialLinkInline(admin.TabularInline):
#     model = SocialLink
#     extra = 1
#     fields = ['platform', 'url', 'icon_class', 'order']
#
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['name', 'title', 'email', 'phone', 'freelance_status', 'projects_completed']
#     list_editable = ['freelance_status', 'projects_completed']
#     search_fields = ['name', 'title', 'email', 'phone']
#     list_filter = ['freelance_status', 'created_at']
#
#     # Inlines - bu yerda barcha bog'langan ma'lumotlarni bitta joyda ko'rish
#     inlines = [
#         SkillInline,
#         ServiceInline,
#         ProjectInline,
#         ExperienceInline,
#         EducationInline,
#         SocialLinkInline,
#     ]
#
#     # Fieldsets - tashkil etilgan ko'rinish
#     fieldsets = (
#         ('Basic Information', {
#             'fields': ('name', 'title', 'description', 'bio')
#         }),
#         ('Personal Details', {
#             'fields': ('birth_date', 'address', 'email', 'phone', 'freelance_status')
#         }),
#         ('Media Files', {
#             'fields': ('photo', 'cv_file'),
#             'description': 'Upload profile photo and CV file'
#         }),
#         ('Statistics', {
#             'fields': ('projects_completed',)
#         }),
#     )
#
#     # Fayllarni ko'rish uchun readonly maydonlar
#     readonly_fields = ['created_at', 'updated_at']
#
#     # Admin panelda profil rasmini ko'rsatish
#     def photo_preview(self, obj):
#         if obj.photo:
#             return format_html('<img src="{}" width="100" height="100" style="border-radius:50%;" />', obj.photo.url)
#         return "No Photo"
#
#     photo_preview.short_description = 'Profile Photo Preview'
#
#
# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ['name', 'percentage', 'profile', 'order']
#     list_editable = ['percentage', 'order']
#     list_filter = ['profile']
#     search_fields = ['name']
#     ordering = ['order', 'name']
#
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['title', 'profile', 'icon', 'order']
#     list_editable = ['icon', 'order']
#     list_filter = ['profile']
#     search_fields = ['title', 'description']
#     ordering = ['order', 'title']
#
#
# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['title', 'profile', 'technologies_preview', 'created_at', 'order']
#     list_editable = ['order']
#     list_filter = ['profile', 'created_at']
#     search_fields = ['title', 'description', 'technologies']
#     ordering = ['order', '-created_at']
#
#     # Technologies ni qisqartirib ko'rsatish
#     def technologies_preview(self, obj):
#         return obj.technologies[:50] + '...' if len(obj.technologies) > 50 else obj.technologies
#
#     technologies_preview.short_description = 'Technologies'
#
#     # Rasmni ko'rish
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html('<img src="{}" width="100" height="60" />', obj.image.url)
#         return "No Image"
#
#     image_preview.short_description = 'Image Preview'
#
#
# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ['position', 'company', 'start_date', 'end_date', 'profile', 'order']
#     list_editable = ['order']
#     list_filter = ['profile', 'company']
#     search_fields = ['position', 'company', 'description']
#     ordering = ['order', '-start_date']
#
#
# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ['degree', 'institution', 'period', 'profile', 'order']
#     list_editable = ['order']
#     list_filter = ['profile', 'institution']
#     search_fields = ['degree', 'institution', 'field_of_study']
#     ordering = ['order', '-period']
#
#
# @admin.register(SocialLink)
# class SocialLinkAdmin(admin.ModelAdmin):
#     list_display = ['platform', 'url_display', 'profile', 'order']
#     list_editable = ['order']
#     list_filter = ['profile', 'platform']
#     search_fields = ['platform', 'url']
#     ordering = ['order', 'platform']
#
#     # URL ni qisqartirib ko'rsatish
#     def url_display(self, obj):
#         return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url[:50] + '...')
#
#     url_display.short_description = 'URL'
#
#
# @admin.register(ContactMessage)
# class ContactMessageAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'subject', 'created_at', 'is_read', 'message_preview']
#     list_editable = ['is_read']
#     list_filter = ['is_read', 'created_at']
#     search_fields = ['name', 'email', 'subject', 'message']
#     readonly_fields = ['created_at']
#     ordering = ['-created_at']
#
#     # Xabarni qisqartirib ko'rsatish
#     def message_preview(self, obj):
#         return obj.message[:100] + '...' if len(obj.message) > 100 else obj.message
#
#     message_preview.short_description = 'Message Preview'
#
#     # Harakatlar
#     actions = ['mark_as_read', 'mark_as_unread']
#
#     def mark_as_read(self, request, queryset):
#         queryset.update(is_read=True)
#
#     mark_as_read.short_description = "Mark selected messages as read"
#
#     def mark_as_unread(self, request, queryset):
#         queryset.update(is_read=False)
#
#     mark_as_unread.short_description = "Mark selected messages as unread"
#
#
# # Admin panelni sozlash
# admin.site.site_header = "Azam Saidov Portfolio Admin"
# admin.site.site_title = "Portfolio Admin Panel"
# admin.site.index_title = "Welcome to Portfolio Administration"

# app1/admin.py (HECH QANDAY CUSTOM CLASSSIZ)
from django.contrib import admin
from django import forms
from .models import Profile, Skill, Service, Project, Experience, Education, SocialLink, ContactMessage

# 1. Project uchun oddiy form
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

# 2. Project uchun juda oddiy admin
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    # Hech qanday extra method yoki property

# 3. Register
admin.site.register(Project, ProjectAdmin)

# 4. Qolgan modellar uchun faqat register
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Service)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(SocialLink)
admin.site.register(ContactMessage)