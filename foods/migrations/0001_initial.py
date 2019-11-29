# Generated by Django 2.2 on 2019-11-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_vegetariano', models.TextField(blank=True, null=True)),
                ('menu_carnivoro', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Comida',
                'verbose_name_plural': 'Comidas',
            },
        ),
    ]