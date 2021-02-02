import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from fibabanka.items import Article


class FibaSpider(scrapy.Spider):
    name = 'fiba'
    allowed_domains = ['fibabanka.com.tr']
    start_urls = ['https://www.fibabanka.com.tr/hakkimizda/duyuru-ve-haberler/']

    def parse(self, response):
        years = response.xpath('//div[@class="fiba-news-announcements__year"]/a/@href').getall()
        print(years)
        yield from response.follow_all(years, self.parse_year)

    def parse_year(self, response):
        articles = response.xpath('//div[@class="fb__accordion"]')
        for article in articles:
            item = ItemLoader(Article())
            item.default_output_processor = TakeFirst()

            title = " ".join(article.xpath('.//h3/text()').getall()).strip()
            content = " ".join(article.xpath('.//div[@class="accordion__content"]//text()').getall()).strip()

            year = response.url.split('/')[-1]
            print(title, year)

            item.add_value('title', title)
            item.add_value('content', content)
            item.add_value('year', year)

            yield item.load_item()
