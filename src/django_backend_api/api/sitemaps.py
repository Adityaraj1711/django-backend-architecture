from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from .models import Portfolio

class StaticSitemap(Sitemap):
    """ Sitemap for static website pages """
    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        """ Add the static pages views in the list """
        return []

    def location(self, item):
        return reverse(item)


class PortfolioSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Portfolio.objects.all()

    def location(self, obj):
        return obj.note_full_path

    def lastmod(self, obj):
        return obj.date_modified
