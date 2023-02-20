# Generated by Django 4.1.7 on 2023-02-20 00:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Регион')),
                ('ind_hh', models.IntegerField(blank=True, default=0, null=True, verbose_name='Номер HH')),
                ('ind_zarp', models.IntegerField(blank=True, default=0, null=True, verbose_name='Номер Zarplata')),
                ('ind_super', models.IntegerField(blank=True, default=0, null=True, verbose_name='Номер SuperJob')),
            ],
            options={
                'verbose_name': 'Название региона',
                'verbose_name_plural': 'Регионы',
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ind', models.IntegerField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Навык')),
            ],
            options={
                'verbose_name': 'Название навыка',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30, verbose_name='Запрос')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('up', models.FloatField(verbose_name='Верхняя граница')),
                ('down', models.FloatField(verbose_name='Нижняя граница')),
            ],
            options={
                'verbose_name': 'Текст запроса',
                'verbose_name_plural': 'Запросы',
            },
        ),
        migrations.CreateModel(
            name='Wordskill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.FloatField()),
                ('percent', models.FloatField()),
                ('id_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.skill')),
                ('id_word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.word')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('snippet', models.TextField()),
                ('salaryFrom', models.FloatField(default=0)),
                ('salaryTo', models.FloatField(default=0)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.area')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.employer')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.schedule')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.type')),
                ('word_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parserHHapp.word')),
            ],
        ),
    ]
