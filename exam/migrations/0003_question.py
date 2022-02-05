# Generated by Django 4.0.1 on 2022-02-02 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=450)),
                ('option_1', models.CharField(max_length=250)),
                ('option_2', models.CharField(max_length=250)),
                ('option_3', models.CharField(max_length=250)),
                ('option_4', models.CharField(max_length=250)),
                ('answer', models.CharField(choices=[('o_1', models.CharField(max_length=250)), ('o_2', models.CharField(max_length=250)), ('o_3', models.CharField(max_length=250)), ('o_4', models.CharField(max_length=250))], max_length=25)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.exam')),
            ],
        ),
    ]