import re
import scrapy
import os
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImagesItem


class ImageSpiderSpider(CrawlSpider):
    name = 'image_spider'
    allowed_domains = ['books.toscrape.com']
    # start_urls = ['http://books.toscrape.com/']

    def start_requests(self):
        url = 'http://books.toscrape.com/'
        yield scrapy.Request(url=url)

    rules = (
        Rule(LinkExtractor(allow=r'catalogue/'), callback='parse_image', follow=True),
    )

    save_location = os.getcwd()

    custom_settings = {
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": save_location
    }

    def parse_image(self, response):
        if response.xpath('//div[@class="item active"]/img').get() is not None:
            img = response.xpath('//div[@class="item active"]/img/@src').get()
            """
            Computing the Absolute path of the image file.
            "image_urls" require absolute path, not relative path
            """
            m = re.match(r"^(?:../../)(.*)$", img).group(1)
            url = "http://books.toscrape.com/"
            img_url = "".join([url, m])
            image = ImagesItem()
            image["image_urls"] = [img_url]  # "image_urls" must be a list
            yield image
