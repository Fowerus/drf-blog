# Generated by Django 3.1.6 on 2021-03-10 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0002_auto_20210310_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community_admins',
            name='description',
            field=models.CharField(default='', max_length=100, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='communityposts',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='com_posts_author', to='Communities.community_admins', verbose_name='author'),
        ),
    ]
