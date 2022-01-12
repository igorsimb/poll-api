# Generated by Django 4.0.1 on 2022-01-11 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_poll_start_date_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('text', models.TextField(blank=True, null=True)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.poll')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.question')),
            ],
        ),
    ]