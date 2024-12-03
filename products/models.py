from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', on_delete=models.CASCADE, null=True, blank=True,
                               related_name='children')
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to="categories/")
    is_enabled = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_("description"), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to="products/")
    is_enabled = models.BooleanField(_('is enable'), default=True)
    category = models.ManyToManyField('Category', verbose_name=_('category'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=_('product'))
    title = models.CharField(_('title'), max_length=100)
    file = models.FileField(_('file'), upload_to="files/%Y/%m/%d/")
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
