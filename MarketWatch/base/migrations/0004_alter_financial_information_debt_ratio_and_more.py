# Generated by Django 5.0.3 on 2024-04-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0003_financial_information_interest_rate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="financial_information",
            name="debt_ratio",
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
        migrations.AlterField(
            model_name="financial_information",
            name="down_payment",
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
        migrations.AlterField(
            model_name="financial_information",
            name="interest_rate",
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
        migrations.AlterField(
            model_name="financial_information",
            name="loan_amount",
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
        migrations.AlterField(
            model_name="financial_information",
            name="property_value",
            field=models.DecimalField(decimal_places=5, max_digits=6),
        ),
    ]
