from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from .models import *

@admin.register(MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'keywords_preview')
    list_filter = ('is_active',)
    search_fields = ('title', 'description', 'keywords')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'keywords')
        }),
        ('Logo & Status', {
            'fields': ('svg_logo', 'is_active')
        }),
    )
    
    def keywords_preview(self, obj):
        if obj.keywords:
            return obj.keywords[:50] + '...' if len(obj.keywords) > 50 else obj.keywords
        return '-'
    keywords_preview.short_description = 'Keywords Preview'

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'greeting', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('full_name', 'title', 'greeting')
    fieldsets = (
        ('Personal Information', {
            'fields': ('greeting', 'full_name', 'title')
        }),
        ('Biography', {
            'fields': ('bio',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if obj.is_active:
            # Ensure only one Hero is active
            Hero.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_preview', 'has_avatar', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('about',)
    fieldsets = (
        ('Content', {
            'fields': ('about', 'avatar')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def about_preview(self, obj):
        if obj.about:
            return obj.about[:75] + '...' if len(obj.about) > 75 else obj.about
        return '-'
    about_preview.short_description = 'About Preview'
    
    def has_avatar(self, obj):
        return '✅' if obj.avatar else '❌'
    has_avatar.short_description = 'Avatar'
    
    def save_model(self, request, obj, form, change):
        if obj.is_active:
            # Ensure only one About is active
            About.objects.exclude(pk=obj.pk).update(is_active=False)
        super().save_model(request, obj, form, change)

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('title', 'icon', 'is_active')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'has_image', 'has_url', 'is_active')
    list_filter = ('is_active', 'is_major')
    search_fields = ('title', 'description')
    filter_horizontal = ('skill',)
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description')
        }),
        ('Media & Links', {
            'fields': ('image', 'url')
        }),
        ('Technologies', {
            'fields': ('skill',)
        }),
        ('Status', {
            'fields': ('is_major','is_active',)
        }),
    )
    
    def has_image(self, obj):
        return '✅' if obj.image else '❌'
    has_image.short_description = 'Image'
    
    def has_url(self, obj):
        if obj.url:
            return format_html('<a href="{}" target="_blank">🔗 View</a>', obj.url)
        return '❌'
    has_url.short_description = 'Project URL'


@admin.register(SlkillGroup)
class SkillGroupAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill_count', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = [SkillInline]
    
    def skill_count(self, obj):
        return obj.skill_set.filter(is_active=True).count()
    skill_count.short_description = 'Active Skills'

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'has_icon', 'is_active')
    list_filter = ('is_active', 'group')
    search_fields = ('title',)
    fieldsets = (
        ('Skill Information', {
            'fields': ('title', 'group')
        }),
        ('Display', {
            'fields': ('icon',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def has_icon(self, obj):
        return '✅' if obj.icon else '❌'
    has_icon.short_description = 'Icon'

class StepInline(admin.TabularInline):
    model = Step
    extra = 1
    fields = ('title','description', 'is_active')

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('description', 'step_count', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('description',)
    inlines = [StepInline]
    
    def step_count(self, obj):
        return obj.steps.filter(is_active=True).count()
    step_count.short_description = 'Active Steps'

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_display = ('title', 'process', 'is_active')
    list_filter = ('is_active', 'process')
    search_fields = ('title',)

class InfoItemInline(admin.StackedInline):
    model = InfoItem
    extra = 1
    fields = ('key', 'value', 'link', 'icon', 'is_active')

class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1
    fields = ('title', 'link', 'icon', 'is_active')

@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('title', 'info_count', 'social_count', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    fieldsets = (
        ('Content', {
            'fields': ('title', 'description')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    inlines = [InfoItemInline, SocialLinkInline]
    
    def info_count(self, obj):
        return obj.info_items.filter(is_active=True).count()
    info_count.short_description = 'Info Items'
    
    def social_count(self, obj):
        return obj.social_links.filter(is_active=True).count()
    social_count.short_description = 'Social Links'

@admin.register(InfoItem)
class InfoItemAdmin(admin.ModelAdmin):
    list_display = ('key', 'value_preview', 'has_link', 'get_in_touch', 'is_active')
    list_filter = ('is_active', 'get_in_touch')
    search_fields = ('key', 'value')
    fieldsets = (
        ('Information', {
            'fields': ('key', 'value', 'get_in_touch')
        }),
        ('Display', {
            'fields': ('link', 'icon')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def value_preview(self, obj):
        if obj.value:
            return obj.value[:50] + '...' if len(obj.value) > 50 else obj.value
        return '-'
    value_preview.short_description = 'Value Preview'
    
    def has_link(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank">🔗 View</a>', obj.link)
        return '❌'
    has_link.short_description = 'Link'

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link_preview', 'has_icon', 'get_in_touch', 'is_active')
    list_filter = ('is_active', 'get_in_touch')
    search_fields = ('title',)
    fieldsets = (
        ('Social Information', {
            'fields': ('title', 'link', 'get_in_touch')
        }),
        ('Display', {
            'fields': ('icon',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )
    
    def link_preview(self, obj):
        if obj.link:
            return format_html('<a href="{}" target="_blank">🔗 {}</a>', obj.link, obj.link[:30] + '...' if len(obj.link) > 30 else obj.link)
        return '-'
    link_preview.short_description = 'Social Link'
    
    def has_icon(self, obj):
        return '✅' if obj.icon else '❌'
    has_icon.short_description = 'Icon'

# Customize admin site headers
admin.site.site_header = "Portfolio Admin Dashboard"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"