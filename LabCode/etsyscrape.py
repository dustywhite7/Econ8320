import scrapy
import json

class EtsySpider(scrapy.Spider):
    name = "etsy_spider"
    start_urls = [
            'https://www.etsy.com/search?q=dungeons%20and%20dragons&ref=auto1&as_prefix=dungeons%20'
            ]
    with open('etsyresults.csv', 'w') as f:
        f.write('url\t name\t image\t description\t startPrice\t rating\n')
                
    def parse(self, response):     
        # Follow all category links to find items to parse
        for href in response.xpath("//a/@href[contains(., '/search/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse)
        # Follow all product links and parse the items
        for href in response.xpath("//a/@href[contains(., '/listing/')]"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_item)
        

    def parse_item(self, response):
        with open('etsyresults.csv', 'a') as f:
            thedict = json.loads(response.xpath("//script[@type='application/ld+json']/text()").extract()[0])
            finaldict = {
                    'url' : thedict['url'],
                    'name' : thedict['name'],
                    'image' : thedict['image'],
                    'description': thedict['description'],
                    'startPrice' : float(thedict['offers']['lowPrice']),
                    'rating' : float(thedict['aggregateRating']['ratingValue']),
                    }
            finalstring = finaldict['url']
            finalstring += "\t" + finaldict['name']
            finalstring += "\t" + finaldict['image']
            finalstring += "\t" + finaldict['description'].replace('\n','').replace('\r','').replace('\t', '')
            finalstring += "\t" + str(finaldict['startPrice'])
            finalstring += "\t" + str(finaldict['rating']) + "\n"
            f.write(finalstring)
#            yield finaldict