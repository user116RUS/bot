# Generated by Django 4.0.4 on 2022-06-20 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_license_remove_docs_licens'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='license',
            options={'ordering': ['datetime'], 'verbose_name': 'Лист лицензии', 'verbose_name_plural': 'Лицензия'},
        ),
        migrations.AddField(
            model_name='docs',
            name='students',
            field=models.FileField(default='DEFAULT VALUE', upload_to='files/pupil/%Y/%m/%d/', verbose_name='Список учащихся'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='studyProgram',
            field=models.FileField(upload_to='files/studyProgram/%Y/%m/%d/', verbose_name='Образовательная программа'),
        ),
    ]
