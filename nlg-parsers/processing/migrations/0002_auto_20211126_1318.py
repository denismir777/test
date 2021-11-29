# Generated by Django 3.2.9 on 2021-11-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='other_data',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='build',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='corpus',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_entry',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_ogrn',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_post',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_reg',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='date_vyp',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='foreignorg',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='inn',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='invalid',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_protch_przd',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kod_no',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kod_okved',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kod_region',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kod_ro',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kpp',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='kpprafp',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='main_okved_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='namec',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='namep',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ogrn',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='okopf12',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='okved2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='okved2name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='periodcode',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='post_index',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pr_otch',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pr_otch_zd_date',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pr_rafp',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pr_zd',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='region_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='regionname',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='rsmpcategory',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='street_type',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tax_dept_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tax_dept_name_main',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='token',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ul_reg_method',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ul_street',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='yearcode',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
