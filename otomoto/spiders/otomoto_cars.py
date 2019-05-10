# -*- coding: utf-8 -*-
import scrapy


class OtomotoCarsSpider(scrapy.Spider):
    name = 'my_parser'
    # allowed_domains = ['(https://www.otomoto.pl/osobowe/)']
    start_urls = ['https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on']

    def parse(self, response):

        for car in response.css('div.offer-item__content'):

            yield {
                'title': car.css('.offer-title__link::text').get(default=" "),
                "subtitle": car.css('.offer-item__subtitle::text').get(default=" "),
                "year": car.css("ul.offer-item__params").xpath('li[@data-code="year"]/span/text()').get(default=" "),
                "mileage":  car.css("ul.offer-item__params").xpath('li[@data-code="mileage"]/span/text()').get(default=" "),
                "capacity": car.css("ul.offer-item__params").xpath('li[@data-code="engine_capacity"]/span/text()').get(default=" "),
                "fuel": car.css("ul.offer-item__params").xpath('li[@data-code="fuel_type"]/span/text()').get(default=" "),
                "price": car.css('span.offer-price__number::text').get(default=" ").split("/n")[0],
                "currency": car.css('span.offer-price__currency::text').get(default=" "),
                "price_details": car.css('span.offer-price__details::text').get(default=" "),
                "city": car.css('span.offer-item__location h4::text').get(default=" ").split("/n")[0],
                "region": car.css('span.offer-item__location h4 em::text').get(default=" ")
            }

        next_page = response.css('li.next.abs a::attr(href)').get()
        print(next_page)

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)



