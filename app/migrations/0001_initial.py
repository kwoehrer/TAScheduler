# Generated by Django 4.1.2 on 2022-12-21 22:45

import django.core.validators
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
                ('course_ID', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('semester', models.CharField(choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter'), ('Special', 'Special')], db_index=True, default='Spring', max_length=10)),
                ('year', models.IntegerField(default=2022, validators=[django.core.validators.MinValueValidator(2012, message='Course.year cannot be more than 10 years into  the past.'), django.core.validators.MaxValueValidator(2032, message='Course.year cannot be more than 10 years into  the future.')])),
                ('description', models.CharField(max_length=70)),
                ('credits', models.IntegerField(default=3, validators=[django.core.validators.MaxValueValidator(9, message='Course.credit field must be less than 10.'), django.core.validators.MinValueValidator(1, message='Course.credit field must be greater than 1.')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('account_ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('username', models.CharField(db_index=True, max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('first_name', models.CharField(db_index=True, max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('home_address', models.CharField(blank=True, max_length=70, null=True)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Instructor', 'Instructor'), ('TA', 'Ta')], db_index=True, default='TA', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='TA',
            fields=[
                ('account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='TACourseAssignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ta')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_num', models.IntegerField()),
                ('MeetingTimes', models.CharField(max_length=50)),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('ta_account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ta')),
            ],
        ),
        migrations.CreateModel(
            name='InstructorAssignments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('account_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instructor')),
            ],
        ),
    ]