# Generated by Django 3.1.6 on 2021-03-14 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user_followers',
            options={'ordering': ['date_creating'], 'verbose_name': 'Follower', 'verbose_name_plural': 'Followers'},
        ),
        migrations.AlterModelOptions(
            name='userpostcomments',
            options={'ordering': ['date_creating'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='userpostlikes',
            options={'ordering': ['-date_creating'], 'verbose_name': 'Like', 'verbose_name_plural': 'Likes'},
        ),
        migrations.AlterModelOptions(
            name='userposts',
            options={'ordering': ['-date_creating'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
