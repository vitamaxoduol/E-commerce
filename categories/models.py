from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):
    name = models.CharField(max_length=200)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    description = models.TextField(blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = ('name', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    @property
    def is_parent(self):
        return self.parent is None
    
    @property
    def is_child(self):
        return self.parent is not None