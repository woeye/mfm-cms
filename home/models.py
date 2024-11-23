from django.db import models
from wagtail import blocks
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField

import home.blocks as home_blocks
from home.tools import APIImageChooserBlock, ImageSerializer

class BlogPostsIndexPage(Page):
    subpage_types = ["home.BlogPostPage"]

    class Meta:
        verbose_name = "Blog Posts Index"

class BlogPostPage(Page):
    parent_page_types = ["home.BlogPostsIndexPage"]

    # hero_image = models.ForeignKey(
    #     'wagtailimages.Image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.PROTECT,
    #     related_name='+',
    # )
    # headline = models.CharField(blank=True, null=False)
    abstract = RichTextField(blank=True, null=False)
    link_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name='+',
    )
    body = StreamField([
        ("sub_headline", home_blocks.SubHeadline()),
        ("single_image", home_blocks.SingleImage()),
        ("multi_image", home_blocks.MultiImage()),
        ("text_content", home_blocks.TextContent()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel("abstract"),
        FieldPanel("body"),
    ]

    promote_panels = Page.promote_panels + [
        MultiFieldPanel([
            FieldPanel('link_image', help_text='The following image should be used when linking to this page'),
        ], "For linking to this page")
    ]

    api_fields = [
        APIField("body"),
        # APIField("headline"),
        APIField("abstract"),
        APIField("link_image", serializer=ImageSerializer()),
    ]

    class Meta:
        verbose_name = "Blog Post"

class FlexPagesIndexPage(Page):
    subpage_types = ["home.FlexPage"]

    class Meta:
        verbose_name = "Flex Pages Index"

class FlexPage(Page):
    parent_page_types = ["home.FlexPagesIndexPage"]
    # hide_title = models.BooleanField(default=False, blank=False, null=False, help_text="Hide page title?")
    body = StreamField([
        ("sub_headline", home_blocks.SubHeadline()),
        ("single_image", home_blocks.SingleImage()),
        ("multi_image", home_blocks.MultiImage()),
        ("text_content", home_blocks.TextContent()),
        # ("children_list", home_blocks.ChildrenList()),
    ])

    content_panels = Page.content_panels + [
        # FieldPanel("hide_title"),
        FieldPanel("body"),
    ]

    api_fields = [
        # APIField("hide_title"),
        APIField("body"),
    ]

    class Meta:
        verbose_name = "Flex Page"
