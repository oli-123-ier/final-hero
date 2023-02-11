from django.contrib import admin
from .models import Product, Category, Commande


# Register your models here.
admin.site.site_header = "E-commerceProject"
admin.site.site_title = "shoes shop"
admin.site.index_title = "Project"


class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title',)
    list_editable = ('price',)


class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'email', 'addresse',
                    'ville', 'pays', 'total', 'date_commande')


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Commande,  AdminCommande)
