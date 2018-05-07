# Generated by Django 2.0.3 on 2018-05-07 20:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField((('blogroll', wagtail.core.blocks.StructBlock((('block_title', wagtail.core.blocks.CharBlock(max_length=80, required=True)), ('blog_page', wagtail.core.blocks.PageChooserBlock(target_model=['blog.BlogIndexPage'])), ('post_count', wagtail.core.blocks.IntegerBlock(help_text='Number of post shown in this block. Default is 5. Max is 10.', max_value=10, min_value=1, required=False))))),)),
        ),
    ]
