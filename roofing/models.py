from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Service(models.Model):
    """Roofing services offered by the company"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    icon = models.CharField(max_length=50, default='🏗️')  # Emoji or icon name
    duration_days = models.IntegerField(help_text="Estimated duration in days")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price']
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.name} - ${self.price}"


class TeamMember(models.Model):
    """Company team members/employees"""
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)  # e.g., "Lead Roofer", "Project Manager"
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    experience_years = models.IntegerField(validators=[MinValueValidator(0)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.position}"


class Booking(models.Model):
    """Customer service bookings/quotes"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='bookings')
    address = models.CharField(max_length=200)
    description = models.TextField()
    requested_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    quote_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.service.name} ({self.status})"


class ContactMessage(models.Model):
    """Messages from contact form"""
    SERVICE_CHOICES = [
        ('installation', 'Roof Installation'),
        ('repair', 'Roof Repair'),
        ('maintenance', 'Roof Maintenance'),
        ('inspection', 'Roof Inspection'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.service}"


class Testimonial(models.Model):
    """Customer testimonials/reviews"""
    customer_name = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='testimonials')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-rating', '-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.rating}⭐"


class Project(models.Model):
    """Completed projects/portfolio"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='projects')
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    before_image = models.ImageField(upload_to='projects/before/', null=True, blank=True)
    after_image = models.ImageField(upload_to='projects/after/', null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-end_date']

    def __str__(self):
        return self.title
