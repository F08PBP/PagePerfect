# Generated by Django 4.2.6 on 2023-10-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0002_auto_20231026_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('authors', models.TextField(blank=True, null=True)),
                ('average_rating', models.FloatField(blank=True, null=True)),
                ('isbn', models.BigIntegerField(blank=True, null=True)),
                ('isbn13', models.BigIntegerField(blank=True, null=True)),
                ('language_code', models.TextField(blank=True, null=True)),
                ('num_pages', models.IntegerField(blank=True, null=True)),
                ('ratings_count', models.IntegerField(blank=True, null=True)),
                ('text_reviews_count', models.IntegerField(blank=True, null=True)),
                ('publication_date', models.TextField(blank=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
            ],
        ),
    ]