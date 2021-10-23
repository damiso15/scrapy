# import scrapy
# import re
# from .items import WeatherItem
#
#
# class WeatherSpiderSpider(scrapy.Spider):
#     name = 'weather_spider'
#     allowed_domains = ['weather.com']
#
#     def start_requests(self):
#         # Weather.com URL for Lagos's weather
#         urls = [
#             'https://weather.com/weather/today/l/7d391501221842b79c58c5260dbafbe2305deffed37a075972092251243a4ad8'
#         ]
#         for url in urls:
#             y = yield scrapy.Request(url=url, callback=self.parse_url)
#             print(y)
