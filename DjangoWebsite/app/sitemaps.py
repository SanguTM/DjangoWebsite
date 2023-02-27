from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):

    def items(self):
        return ['website-about','website-gallery','website-prenumerate']

    def location(self, item):
        return reverse(item)
