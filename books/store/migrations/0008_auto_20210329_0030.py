# Generated by Django 3.1.7 on 2021-03-28 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0007_auto_20210329_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_books', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='readers',
            field=models.ManyToManyField(related_name='books', through='store.UserBookRelations', to=settings.AUTH_USER_MODEL),
        ),
    ]
