import scrapy

class BasketballSpider(scrapy.Spider):
    name = "basketball_spider"
    start_urls = [
            'https://www.basketball-reference.com/leagues/NBA_2017_totals.html'
            ]
    with open('mybballresults.csv', 'w') as f:
        f.write("name, team, AST, FG3, PTS, REB, BLK, STL")
    
    def parse(self, response):
        with open('mybballresults.csv', 'a') as f:

            names = response.xpath('//tr[@class="full_table"]/td[@data-stat="player"]/a/text()').extract()
            teams = response.xpath('//tr[@class="full_table"]/td[@data-stat="team_id"]/text() | //tr[@class="full_table"]/td[@data-stat="team_id"]/a/text()').extract()
            ast = response.xpath('//tr[@class="full_table"]/td[@data-stat="ast"]/text()').extract()
            fg3 = response.xpath('//tr[@class="full_table"]/td[@data-stat="fg3"]/text()').extract()
            pts = response.xpath('//tr[@class="full_table"]/td[@data-stat="pts"]/text()').extract()
            reb = response.xpath('//tr[@class="full_table"]/td[@data-stat="trb"]/text()').extract()
            blk = response.xpath('//tr[@class="full_table"]/td[@data-stat="blk"]/text()').extract()
            stl = response.xpath('//tr[@class="full_table"]/td[@data-stat="stl"]/text()').extract()
            
            print("\n\n\n" + str(len(names)) + "\n\n\n")
            for i in range(len(names)):
                result = ""
                result += str(names[i] + ",")
                result += str(teams[i] + ",")
                result += str(ast[i] + ",")
                result += str(fg3[i] + ",")
                result += str(pts[i] + ",")
                result += str(reb[i] + ",")
                result += str(blk[i] + ",")
                result += str(stl[i] + "\n")
                
                f.write(result)
            