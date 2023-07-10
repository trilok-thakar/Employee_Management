# Generated by Django 4.1.6 on 2023-07-03 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=4, null=True, unique=True)),
                ('role', models.CharField(choices=[('ceo', 'CEO'), ('cto', 'CTO'), ('team leader', 'Team Leader'), ('jr.developer', 'Jr. Developer'), ('sr.developer', 'Sr.Developer'), ('hr executive', 'HR Executive'), ('hr head', 'HR Head')], max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]