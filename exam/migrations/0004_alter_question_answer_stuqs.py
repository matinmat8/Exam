# Generated by Django 4.0.1 on 2022-02-07 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(choices=[('o_1', 1), ('o_2', 2), ('o_3', 3), ('o_4', 4)], max_length=25),
        ),
        migrations.CreateModel(
            name='StuQs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(blank=True, choices=[('o_1', 1), ('o_2', 2), ('o_3', 3), ('o_4', 4)], max_length=15, null=True)),
                ('correct_or_not', models.BooleanField(default=False)),
                ('qs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.question')),
                ('stu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.student')),
            ],
        ),
    ]
