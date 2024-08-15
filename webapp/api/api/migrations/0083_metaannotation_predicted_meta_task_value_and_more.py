# Generated by Django 5.0.6 on 2024-08-23 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0082_remove_metacatmodel_meta_task_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='metaannotation',
            name='predicted_meta_task_value',
            field=models.ForeignKey(blank=True, help_text='meta annotation predicted by a MetaAnnotationModel', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predicted_value', to='api.metataskvalue'),
        ),
        migrations.AlterField(
            model_name='metaannotation',
            name='validated',
            field=models.BooleanField(default=False, help_text='If an annotation is not '),
        ),
    ]
