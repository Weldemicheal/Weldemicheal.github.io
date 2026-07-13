from django.contrib import admin
from .models import Service, TeamMember, Booking, ContactMessage, Testimonial, Project

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_days', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    fieldsets = (
        ('Service Info', {'fields': ('name', 'description', 'icon', 'price')}),
        ('Details', {'fields': ('duration_days', 'is_active')}),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'experience_years', 'is_active')
    list_filter = ('position', 'is_active')
    search_fields = ('name', 'position', 'email')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'requested_date', 'status', 'quote_amount')
    list_filter = ('status', 'service', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'address')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Customer Info', {'fields': ('customer_name', 'customer_email', 'customer_phone')}),
        ('Booking Details', {'fields': ('service', 'address', 'description', 'requested_date')}),
        ('Status', {'fields': ('status', 'quote_amount', 'notes')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'email', 'is_read', 'created_at')
    list_filter = ('service', 'is_read', 'created_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('created_at',)
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected as read"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'service', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'service')
    search_fields = ('customer_name', 'comment')
    readonly_fields = ('created_at',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'service', 'location', 'end_date', 'is_featured')
    list_filter = ('service', 'is_featured', 'end_date')
    search_fields = ('title', 'location', 'description')
    fieldsets = (
        ('Project Info', {'fields': ('title', 'description', 'service', 'location')}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
        ('Images', {'fields': ('before_image', 'after_image')}),
        ('Status', {'fields': ('is_featured',)}),
    )
