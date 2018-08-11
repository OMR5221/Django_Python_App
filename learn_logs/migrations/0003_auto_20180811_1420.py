# Generated by Django 2.1 on 2018-08-11 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn_logs', '0002_auto_20180811_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
        migrations.RemoveField(
            model_name='topic',
            name='date_updated',
        ),
        migrations.AddField(
            model_name='entry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn_logs.Topic'),
        ),
    ]
