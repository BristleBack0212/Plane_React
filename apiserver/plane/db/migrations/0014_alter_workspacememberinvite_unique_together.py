# Generated by Django 3.2.16 on 2023-01-07 05:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0013_auto_20230107_0041"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="workspacememberinvite",
            unique_together={("email", "workspace")},
        ),
    ]
