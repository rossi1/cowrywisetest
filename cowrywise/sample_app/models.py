from django.db import models
from django.utils.translation import ugettext_lazy as _

class UUIDStore(models.Model):
    random_uuid = models.UUIDField(_("random_uuid"), unique=True)
    time_stamp = models.DateTimeField(_('time_stamp'), auto_now_add=True)

    class Meta:
        ordering = ('-time_stamp',)
        verbose_name = 'uuid_store'

    def __str__(self):
        return str(self.time_stamp)
