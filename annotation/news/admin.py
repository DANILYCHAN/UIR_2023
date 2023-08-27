from django.contrib import admin
from django.db.models import QuerySet

from .models import Articles


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ["title", "anons", "full_text", "date"]
    list_editable = ["anons", "full_text"]
    ordering = ["-date", "-title"]
    list_per_page = 10
    actions = ["set_lazy_anons"]

    @admin.action(description="Поставить пустой анонс")
    def set_lazy_anons(self, request, qs: QuerySet):
        for article in qs:
            article.anons = article.title
            article.save()
