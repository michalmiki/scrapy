# -*- coding: utf-8 -*-
import scrapy


class OtomotoCarsSpider(scrapy.Spider):
    name = 'friendly_parser'
    start_urls = ['https://www.otomoto.pl/osobowe/?search%5Bnew_used%5D=on']

    def parse(self, response):

        for car in response.css('div.offer-item__content'):

            yield {
                'title': car.css('.offer-title__link::text').get(default=" ").strip(),
                "subtitle": car.css('.offer-item__subtitle::text').get(default=" ").strip(),
                "year": car.css('.ds-param[data-code="year"]').css('span::text').get(default=" ").strip(),
                "mileage":  car.css('.ds-param[data-code="mileage"]').css('span::text').get(default=" ").strip,
                "capacity": car.css('.ds-param[data-code="engine_capacity"]').css('span::text').get(default=" ").strip(),
                "fuel_type": car.css('.ds-param[data-code="fuel_type"]').css('span::text').get(default=" ").strip(),
                "price": car.css('.offer-price__number.ds-price-number').xpath('span/text()').get(default=" ").strip(),
                "currency": car.css('.offer-price__currency.ds-price-currency::text').get(default=" ").strip(),
                "price_details": car.css('.offer-price__details.ds-price-complement::text').get().strip(),
                "city": car.css('.ds-location-city::text').get(default=' '),
                "region": car.css('.ds-location-region::text').get(default=' '),
            }

        next_page = response.css('li.next.abs a::attr(href)').get()
        print(next_page)

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)



