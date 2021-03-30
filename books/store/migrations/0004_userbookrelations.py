# Generated by Django 3.1.7 on 2021-03-28 21:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0003_book_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserBookRelations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True)),
                ('bookmarks', models.BooleanField(default=True)),
                ('ratte', models.PositiveIntegerField(choices=[(1, 'ok'), (2, 'fine'), (3, 'good'), (4, 'amazing'), (5, 'incredible')])),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_book', to='store.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]