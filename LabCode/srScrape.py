import scrapy

class BasketballSpider(scrapy.Spider):
    name = "basketball_spider"
    start_urls = [
            'https://www.baseball-reference.com/teams/ARI/2017.shtml',
            'https://www.baseball-reference.com/teams/ATL/2017.shtml',
            'https://www.baseball-reference.com/teams/BAL/2017.shtml',
            'https://www.baseball-reference.com/teams/BOS/2017.shtml',
            'https://www.baseball-reference.com/teams/CHC/2017.shtml',
            'https://www.baseball-reference.com/teams/CHW/2017.shtml',
            'https://www.baseball-reference.com/teams/CIN/2017.shtml',
            'https://www.baseball-reference.com/teams/CLE/2017.shtml',
            'https://www.baseball-reference.com/teams/COL/2017.shtml',
            'https://www.baseball-reference.com/teams/DET/2017.shtml',
            'https://www.baseball-reference.com/teams/HOU/2017.shtml',
            'https://www.baseball-reference.com/teams/KCR/2017.shtml',
            'https://www.baseball-reference.com/teams/LAA/2017.shtml',
            'https://www.baseball-reference.com/teams/LAD/2017.shtml',
            'https://www.baseball-reference.com/teams/MIA/2017.shtml',
            'https://www.baseball-reference.com/teams/MIL/2017.shtml',
            'https://www.baseball-reference.com/teams/MIN/2017.shtml',
            'https://www.baseball-reference.com/teams/NYM/2017.shtml',
            'https://www.baseball-reference.com/teams/NYY/2017.shtml',
            'https://www.baseball-reference.com/teams/OAK/2017.shtml',
            'https://www.baseball-reference.com/teams/PHI/2017.shtml',
            'https://www.baseball-reference.com/teams/PIT/2017.shtml',
            'https://www.baseball-reference.com/teams/SDP/2017.shtml',
            'https://www.baseball-reference.com/teams/SEA/2017.shtml',
            'https://www.baseball-reference.com/teams/SFG/2017.shtml',
            'https://www.baseball-reference.com/teams/STL/2017.shtml',
            'https://www.baseball-reference.com/teams/TBR/2017.shtml',
            'https://www.baseball-reference.com/teams/TEX/2017.shtml',
            'https://www.baseball-reference.com/teams/TOR/2017.shtml',
            'https://www.baseball-reference.com/teams/WSN/2017.shtml'
            ]
    with open('baseballresults.csv', 'w') as f:
        f.write("name,team,pos,age\n")
    
    def parse(self, response):
        with open('baseballresults.csv', 'a') as f:

            names = response.xpath('//table[@id="team_batting"]/tbody/tr/td[@data-stat="player"]/a/text()').extract()
            teams = [response.url[-14:-11] for i in range(len(names))]
            pos = response.xpath('//table[@id="team_batting"]/tbody/tr/td[@data-stat="pos"]/text() | //table[@id="team_batting"]/tbody/tr/td[@data-stat="pos"]/strong/text()').extract()
            age = response.xpath('//table[@id="team_batting"]/tbody/tr/td[@data-stat="age"]/text()').extract()
            
            
            print("\n\n\n" + str(len(names)) + str(len(pos)) + str(len(age)) + "\n\n\n")
            for i in range(len(names)):
                result = ""
                result += str(names[i] + ",")
                result += str(teams[i] + ",")
                result += str(pos[i] + ",")
                result += str(age[i] + "\n")
                
                print(result)
                
                f.write(result)
            