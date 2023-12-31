# Generated by Django 4.2.3 on 2023-07-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['name'], 'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
        migrations.AddField(
            model_name='courses',
            name='about',
            field=models.TextField(blank=True, verbose_name='Sobre o curso'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição Simples'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/images', verbose_name='Imagem'),
        ),
    ]
