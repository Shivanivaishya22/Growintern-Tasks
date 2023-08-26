from django.contrib import admin
from .models import Category , Product , User , MyCart , WishList, Payment , Address

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id" , "categoryname", "desc" , "image")

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id" , "pname", "price" , "desc" ,"image" , "category")

class UserAdmin(admin.ModelAdmin):
    list_display = ("fullname","usernm","email","contact","address","password")

class CartAdmin(admin.ModelAdmin):
    list_display = ("user" , "prodct" , "qty")

class WishlistAdmin(admin.ModelAdmin):
    list_display = ("user" , "prodct" , "qty")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id" , "card_no","cvv","expiry","balance")

class AddressAdmin(admin.ModelAdmin):
    list_display = ("name" , "email", "contact" , "add" , "town" , "city")

admin.site.register(Category , CategoryAdmin)
admin.site.register(Product , ProductAdmin)
admin.site.register(User , UserAdmin)
admin.site.register(MyCart , CartAdmin)
admin.site.register(WishList , WishlistAdmin)
admin.site.register(Payment , PaymentAdmin)
admin.site.register(Address , AddressAdmin)