from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Courrier(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name=_(u'Name'))
    companyid = models.CharField(max_length=50, verbose_name=_(u'company id'))
    website = models.CharField(max_length=200, db_index=True, verbose_name=_(u'website'))

    class Meta:
        verbose_name = _(u'Courriers')
        verbose_name_plural = _(u'Courrier')
    
    def __str__(self):
        return u'{0}'.format(self.name)

    def __unicode__(self):
        return self.__str__()

    def removeCourrier(self, pk):
        pass


class Delivery(models.Model):
    deliveryDate = models.DateField(blank=True, verbose_name=_(u'delivery date'), null=True)
    invoiceData = models.CharField(max_length=200, db_index=True, verbose_name=_(u'invoice data'))
    description = models.TextField(blank=True, default='', verbose_name=_(u'description'), max_length=2000)
    address = models.CharField(max_length=200, db_index=True, verbose_name=_(u'address'))
    courrier = models.ForeignKey(Courrier,related_name="select_courrier", on_delete=models.CASCADE)
    estimateData = models.DateField(blank=True, verbose_name=_(u'estimate data'), null=True)

    class Meta:
        verbose_name = _(u'Deliverys')
        verbose_name_plural = _(u'Delivery')
    
    def __str__(self):
        return u'{0}'.format(self.courrier)

    def __unicode__(self):
        return self.__str__()

    def notifyDelivery(self):
        pass
    
