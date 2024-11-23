import wagtail
from rest_framework import serializers
from wagtail.images.blocks import ImageChooserBlock

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = wagtail.images.get_image_model()
        fields = [
            'title',
            'file',
            'width',
            'height',
            'focal_point_x',
            'focal_point_y',
            'focal_point_width',
            'focal_point_height',
        ]

class APIImageChooserBlock(ImageChooserBlock):
    def get_api_representation(self, value, context=None):
        return ImageSerializer(context=context).to_representation(value)
