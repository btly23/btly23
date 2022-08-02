from django.db import models
from django.db.models.base import Model


# Create your models here.


class Category(models.Model):
    cat_id = models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=255)
    url_slug=models.CharField(max_length=255)
    thumbnail=models.FileField(upload_to='media')
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse("category_list")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'

class Sub_Category(models.Model):
    sub_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url_slug = models.CharField(max_length=255,unique=True)
    thumbnail = models.FileField(upload_to='media')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("sub_category_list")
    class Meta:
        verbose_name_plural = 'sub_catagories'
    def __str__(self):
        return self.title

class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name=models.CharField(max_length=255)
    url_slug = models.CharField(max_length=255)
    thumbnail = models.FileField(upload_to='media')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)
    service_discount = models.CharField(max_length=255)
    company_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'companies'
    def __str__(self):
        return self.company_name
