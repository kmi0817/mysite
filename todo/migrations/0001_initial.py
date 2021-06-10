# Generated by Django 3.2.4 on 2021-06-10 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(verbose_name='create published')),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=500, null=True)),
                ('done', models.BooleanField(default=False)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.course')),
            ],
        ),
    ]