# Generated by Django 4.1.4 on 2024-03-13 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0010_rename_type_choicequestion_stage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='group',
            field=models.CharField(default='data_structure', max_length=100),
        ),
    ]
