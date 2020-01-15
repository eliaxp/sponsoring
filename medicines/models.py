from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Medicines(models.Model):

    name = models.CharField(max_length=100, db_index=True,
                            verbose_name=_(u'Name'))
    laboratory = models.CharField(max_length=100, db_index=True,
                            verbose_name=_(u'Laboratory'))

    description = models.TextField(blank=True, default='',
                               verbose_name=_(u'Description'),
                               help_text=u'Write some descriptive words about this medicine.',
                               max_length=2000)
    image = models.ImageField(_('Medicine image'), upload_to='Medicines/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, verbose_name=_(u'Date Created'))

    class Meta:
        ordering = ['-created_at']
        verbose_name = _(u'Medicine')
        verbose_name_plural = _(u'Medicines')
    
    def __str__(self):
        return u'{0}'.format(self.name)

    def __unicode__(self):
        return self.__str__()


    def RemoveMedicine(self):
        pass

    
