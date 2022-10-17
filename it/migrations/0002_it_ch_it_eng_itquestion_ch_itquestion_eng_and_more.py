# Generated by Django 4.0.6 on 2022-10-17 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IT_ch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('merit', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='IT_eng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=100)),
                ('merit', models.CharField(max_length=255)),
                ('result', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ITQuestion_ch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('question', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ITQuestion_eng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('question', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='it',
            name='count',
        ),
        migrations.CreateModel(
            name='ITAnswer_eng',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.it_eng')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.itquestion_eng')),
            ],
        ),
        migrations.CreateModel(
            name='ITAnswer_ch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=255)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.it_ch')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='it.itquestion_ch')),
            ],
        ),
    ]
