# Generated by Django 4.0.1 on 2022-01-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_option_answer_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
