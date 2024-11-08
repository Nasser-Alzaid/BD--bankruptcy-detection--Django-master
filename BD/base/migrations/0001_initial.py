# Generated by Django 5.1 on 2024-08-13 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('net_profit_to_total_assets', models.FloatField(blank=True, null=True)),
                ('total_liabilities_to_total_assets', models.FloatField(blank=True, null=True)),
                ('working_capital_to_total_assets', models.FloatField(blank=True, null=True)),
                ('current_assets_to_short_term_liabilities', models.FloatField(blank=True, null=True)),
                ('retained_earnings_to_total_assets', models.FloatField(blank=True, null=True)),
                ('sales_to_total_assets', models.FloatField(blank=True, null=True)),
                ('equity_to_total_assets', models.FloatField(blank=True, null=True)),
                ('current_liabilities_to_total_assets', models.FloatField(blank=True, null=True)),
                ('book_value_of_equity_to_total_liabilities', models.FloatField(blank=True, null=True)),
                ('gross_profit_to_sales', models.FloatField(blank=True, null=True)),
                ('sales_to_inventory', models.FloatField(blank=True, null=True)),
                ('target', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Financial Data',
                'verbose_name_plural': 'Financial Data',
            },
        ),
    ]