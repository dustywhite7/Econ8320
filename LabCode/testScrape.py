import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = [
            'http://brickset.com/sets/year-2016'
            ]
    with open('myresults.csv', 'w') as f:
        f.write("name, pieces, minifigs, image\n")
    
    def parse(self, response):
        with open('myresults.csv', 'a') as f:
            SET_SELECTOR = ".set"
            for brickset in response.css(SET_SELECTOR):
                
                NAME_SELECTOR = 'h1 ::text'
                PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
                MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
                IMAGE_SELECTOR = 'img ::attr(src)'
                result = str(brickset.css(NAME_SELECTOR).extract_first()) + ","
                result += str(brickset.xpath(PIECES_SELECTOR).extract_first()) + ","
                result += str(brickset.xpath(MINIFIGS_SELECTOR).extract_first()) + ","
                result += str(brickset.css(IMAGE_SELECTOR).extract_first()) + "\n"
                        
                f.write(result)
                
                NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
                next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
                if next_page:
                    yield scrapy.Request(
                        response.urljoin(next_page),
                        callback=self.parse
                    )