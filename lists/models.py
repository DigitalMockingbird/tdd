from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              blank=True,
                              null=True)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

    def name(self):
        first_list_item = Item.objects.filter(list_id=self.id).first().text
        return first_list_item


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
