# Generated by Django 4.1.4 on 2024-03-20 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_alter_tag_group'),
        ('common', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tag',
            field=models.ManyToManyField(through='common.UserAbility', to='question.tag'),
        ),
        migrations.AlterField(
            model_name='userability',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.tag'),
        ),
        migrations.AlterField(
            model_name='userability',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
