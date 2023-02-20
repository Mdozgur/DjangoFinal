# Generated by Django 4.1.7 on 2023-02-18 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0004_alter_course_total_enrollment_alter_lesson_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='total_enrollment',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='grade',
            field=models.IntegerField(default=0),
        ),
    ]
