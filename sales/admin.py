from django.contrib import admin
from .models import Customer, CustomerProfile, Order, OrderItem, Tag

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "is_active", "created_at")
    search_fields = ("full_name", "email")
    list_filter = ("is_active",)
    readonly_fields = ("created_at",)

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ("customer", "document_id", "phone")
    search_fields = ("customer__full_name", "document_id")

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "created_at", "total_amount")
    date_hierarchy = "created_at"
    inlines = [OrderItemInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
