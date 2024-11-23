from wagtail import blocks
from .tools import APIImageChooserBlock


# class PageTitle(blocks.StructBlock):
#     class Meta:
#         icon = "h1"
#         label = "Headline"

class SubHeadline(blocks.StructBlock):
    headline = blocks.CharBlock(required=True)

    class Meta:
        icon = "h2"
        label = "Subheadline"

class SingleImage(blocks.StructBlock):
    image = APIImageChooserBlock(required=True)
    description = blocks.CharBlock(required=False)

    class Meta:
        icon = "image"
        label = "Single Image"

class MultiImage(blocks.StreamBlock):
    images = blocks.ListBlock(
        APIImageChooserBlock(),
        min=1,
        max=4,
        required=True,
    )

    class Meta:
        icon = "image"
        label = "Multiple Images"

class TextContent(blocks.StructBlock):
    content = blocks.RichTextBlock(required=True)

    class Meta:
        icon = "pilcrow"
        label = "Text content"

# class ChildrenList(blocks.StructBlock):
#     folder = blocks.PageChooserBlock(required=True)
#     limit = blocks.IntegerBlock(required=True, default=10)

#     class Meta:
#         icon = "list-ul"
#         label = "Children List"
