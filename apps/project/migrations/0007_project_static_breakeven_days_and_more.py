# Generated by Django 4.0.3 on 2022-03-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_faq_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='static_breakeven_days',
            field=models.ImageField(default='1', upload_to='breakeven_days'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='static_revenue_rate',
            field=models.ImageField(upload_to='revenue_rate'),
        ),
    ]