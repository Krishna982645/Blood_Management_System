# Generated by Django 4.2.5 on 2023-10-24 10:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipe", "0009_alter_receipe_receipe_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="blood",
            name="blood_status",
            field=models.CharField(
                blank=True, default="pending", max_length=100, null=True
            ),
        ),
    ]