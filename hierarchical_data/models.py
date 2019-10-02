from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class File_Class(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children', limit_choices_to={'is_folder': True})
    is_folder = models.BooleanField()
    file_link = models.CharField(max_length=400, null=True, blank=True)
    # file = forms.FileField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
