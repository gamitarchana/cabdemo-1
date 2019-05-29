# Generated by Django 2.1.8 on 2019-05-29 08:05

from django.db import migrations
import streams.models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('outstation', '0011_auto_20190524_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outstationroutepage',
            name='tourist_places_in_destination',
            field=wagtail.core.fields.StreamField([('tourist_location', wagtail.core.blocks.StructBlock([('place', wagtail.core.blocks.CharBlock(requried=True)), ('details', wagtail.core.blocks.TextBlock(help_text='Add place details', requried=True)), ('duration_of_visit', wagtail.core.blocks.CharBlock(requried=True)), ('distance_from_start_location', wagtail.core.blocks.IntegerBlock(default=0, null=False)), ('map_icon', wagtail.core.blocks.StructBlock([('map_icon', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('trip_types', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trip_type', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.TripType))]))), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('tag', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.LocationTag))]))), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))), ('amenities', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('amenity_type', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'Lodging'), (2, 'Petrol Pump'), (3, 'Eating Place')], max_length=6, required=False)), ('location', wagtail.core.blocks.CharBlock(required=False))])))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='outstationroutepage',
            name='tourist_places_on_route',
            field=wagtail.core.fields.StreamField([('tourist_location', wagtail.core.blocks.StructBlock([('place', wagtail.core.blocks.CharBlock(requried=True)), ('details', wagtail.core.blocks.TextBlock(help_text='Add place details', requried=True)), ('duration_of_visit', wagtail.core.blocks.CharBlock(requried=True)), ('distance_from_start_location', wagtail.core.blocks.IntegerBlock(default=0, null=False)), ('map_icon', wagtail.core.blocks.StructBlock([('map_icon', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('trip_types', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('trip_type', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.TripType))]))), ('tags', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('tag', wagtail.snippets.blocks.SnippetChooserBlock(streams.models.LocationTag))]))), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True))]))), ('amenities', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('amenity_type', wagtail.core.blocks.ChoiceBlock(choices=[(1, 'Lodging'), (2, 'Petrol Pump'), (3, 'Eating Place')], max_length=6, required=False)), ('location', wagtail.core.blocks.CharBlock(required=False))])))]))], blank=True, null=True),
        ),
    ]
