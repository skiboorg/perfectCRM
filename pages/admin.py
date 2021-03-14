from django.contrib import admin
from .models import *

class Block2FeaturesInline(admin.TabularInline):
    model = Block2Features
    extra = 0


class Block2Admin(admin.ModelAdmin):
    inlines = [Block2FeaturesInline]

    class Meta:
        model = Block2

class Block4FeaturesInline(admin.TabularInline):
    model = Block4Features
    extra = 0


class Block4Admin(admin.ModelAdmin):
    inlines = [Block4FeaturesInline]

    class Meta:
        model = Block2


class PageFeaturesInline(admin.TabularInline):
    model = PageFeatures
    extra = 0

class PageBlocksInline(admin.TabularInline):
    model = PageBlocks
    extra = 0

class PageAdmin(admin.ModelAdmin):
    inlines = [PageFeaturesInline,PageBlocksInline]

    class Meta:
        model = Page

class HeaderServiceInline(admin.TabularInline):
    model = HeaderService
    extra = 0

class HeaderAdmin(admin.ModelAdmin):
    inlines = [HeaderServiceInline]

    class Meta:
        model = Header

admin.site.register(Settings)
admin.site.register(Header,HeaderAdmin)
admin.site.register(Block1)
admin.site.register(Block2,Block2Admin)
# admin.site.register(Block2Features)
admin.site.register(Block3)
admin.site.register(Block4,Block4Admin)
admin.site.register(Block5)
admin.site.register(Block6)
admin.site.register(Block7)
admin.site.register(Feedback)
admin.site.register(Page,PageAdmin)