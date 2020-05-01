# Generated by Django 2.2.12 on 2020-05-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_portfolio_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='major',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='role',
            field=models.CharField(default='', max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='address',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='facebook_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='github_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='linkedin_link',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='mobile',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='twitter_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='highlights',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='achievement',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='certification',
            name='about',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='certification',
            name='certificate',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AlterField(
            model_name='certification',
            name='certificate_url',
            field=models.URLField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='college',
            name='college_address',
            field=models.CharField(default='', max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='company',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='interest',
            name='interest',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='email',
            field=models.EmailField(default='xyz@abc.com', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='feature',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tech_stack',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
