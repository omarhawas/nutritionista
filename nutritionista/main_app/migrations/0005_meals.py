# Generated by Django 3.2.9 on 2021-12-15 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner'), ('S', 'Snack')], default='B', max_length=1)),
                ('food', models.CharField(max_length=100)),
                ('portion', models.CharField(max_length=100)),
                ('calories', models.CharField(max_length=100)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.day')),
            ],
        ),
    ]