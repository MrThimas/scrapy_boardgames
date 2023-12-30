import scrapy


class JogoSpider(scrapy.Spider):
    name = "jogo"
    start_urls = ["https://boardgamegeek.com/browse/boardgame/page/1"]

    def parse(self, response):
       for jogo in response.css('#row_'):
            yield{
            'Rank': jogo.css('.collection_rank a::attr(name)').get(),
            'Nome': jogo.css('.primary::text').get(),
            'Avaliacao': jogo.css('#row_ .collection_bggrating:nth-child(5)::text').get().split()[0]
            }



            prox_pag = response.xpath('//*[@id="maincontent"]/form/div/div[1]/a[5]').attrib['href']
            if prox_pag is not None:
                yield response.follow(prox_pag, callback = self.parse)
