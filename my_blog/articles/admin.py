from django.contrib import admin

# Register your models here.
from articles.models import Article, Author

admin.site.register(Article)
