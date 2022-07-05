# Generated by Django 4.0.4 on 2022-06-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_docs_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('licens', models.FileField(upload_to='files/licens/%Y/%m/%d/', verbose_name='Лицензия лист ')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Лист лицензии',
                'verbose_name_plural': 'листов',
                'ordering': ['datetime'],
            },
        ),
        migrations.RemoveField(
            model_name='docs',
            name='licens',
        ),
    ]
