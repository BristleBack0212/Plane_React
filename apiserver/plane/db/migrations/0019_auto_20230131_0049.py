# Generated by Django 3.2.16 on 2023-01-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0018_auto_20230130_0119"),
    ]

    operations = [
        migrations.AlterField(
            model_name="issueactivity",
            name="new_value",
            field=models.TextField(
                blank=True, null=True, verbose_name="New Value"
            ),
        ),
        migrations.AlterField(
            model_name="issueactivity",
            name="old_value",
            field=models.TextField(
                blank=True, null=True, verbose_name="Old Value"
            ),
        ),
    ]
