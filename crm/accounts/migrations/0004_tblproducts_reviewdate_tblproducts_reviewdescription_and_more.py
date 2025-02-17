# Generated by Django 5.1.4 on 2025-01-25 09:19

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bestseller'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblproducts',
            name='ReviewDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tblproducts',
            name='ReviewDescription',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
        migrations.AddField(
            model_name='tblproducts',
            name='ReviewerName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
