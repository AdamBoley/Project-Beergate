# Generated by Django 3.2.15 on 2022-08-18 12:16

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import reviews.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brewery', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=50)),
                ('colour', models.CharField(max_length=50)),
                ('alcohol', models.DecimalField(decimal_places=1, max_digits=3)),
                ('hops', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('keywords', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('aroma', models.IntegerField(validators=[reviews.models.validate_within_limits])),
                ('appearance', models.IntegerField(validators=[reviews.models.validate_within_limits])),
                ('taste', models.IntegerField(validators=[reviews.models.validate_within_limits])),
                ('aftertaste', models.IntegerField(validators=[reviews.models.validate_within_limits])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beer_review', to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(blank=True, related_name='review_downvotes', to=settings.AUTH_USER_MODEL)),
                ('upvotes', models.ManyToManyField(blank=True, related_name='review_upvotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'beer review',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('downvotes', models.ManyToManyField(blank=True, related_name='comment_downvotes', to=settings.AUTH_USER_MODEL)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.review')),
                ('upvotes', models.ManyToManyField(blank=True, related_name='comment_upvotes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'review comment',
                'ordering': ['timestamp'],
            },
        ),
    ]
