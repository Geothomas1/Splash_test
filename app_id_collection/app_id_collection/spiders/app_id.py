import scrapy
from scrapy.http.request import Request
from ..items import AppIdCollectionItem
from scrapy_splash import SplashRequest
main_list=[]

script = """
                        function main(splash,args)
                            splash:set_viewport_size(1028, 10000)
                            splash:go(args.url)
                            local scroll_to = splash:jsfunc("window.scrollTo")
                            scroll_to(0, 2900)
                            splash:wait(8)
                            return {
                                html = splash:html()
                            }
                        end
                    """
tag=['5085823144773442962', '6039364087858800745', '5701186570030180647', '8227659278446954551', '9138875341513456260', '6282085300854828346', '5022485643112186824', '9013887703433662830', '8638205339963097356', '8369547020914796683', '7490630152268137471', '7429519885017730758', '8251585912892725023', '8530369363752063791', '8296561073389255546', '5095269876812936301', '7220471815630703407', '5587120000600918044', '6168990212684665571', '6442968869360209848', '6811979368685561616', '8858789528811041419', '8434939990812891588', '8812080606760179078', '5330073137281448763', '4693506808769795289', '5968040913369553104', '6513890076925025162', '8321696171123618246', '9059031076674808747', '7318129576372072658', '7340001391442011060', '6378315861450040881', '6941062707350185168', '6399541521943653846', '8428961162124483774', '7470546359549086062', '8737102155398054550', '7491582187663013870', '5605516914369427951', '6498932506822480126', '6640298162366748848', '8589343388929342039', '5106187273774761663', '6262333202706287552', '7392390343537623321', '7642513241968800472', '7745268094426388671', '6486706157220091820', '5302637243641590012', '9183662361966484245', '8969118793609603861', '7252949884150518022', '7108292717914554935', '5801820606911592090', '5271749465422950962', '8967234124354529478', '4741928495834891555', '5622872903536904776', '5827577065094822174', '8508050297195526091', '8121951429947449278', '8086910861624532667', '6321967593291050104', '7162702525712431458', '8367752935101364368', '4929793251675564296', '8857615524735539474', '8919019654843284695', '5428525173187661789', '5843788422909712485', '7300020765194314153', '6898760406631171989', '7887547651896089900', '4898481793717084307', '4620348867919520429']
url=['https://play.google.com/store/apps/dev?id='+i
for i in tag]

class AppidSpider(scrapy.Spider):
    name='app_id'
    allowed_domain=["play.google.com"]

    def start_requests(self):
        for u in url:
            yield SplashRequest(url=u, callback=self.parse)            

    def parse(self,response):
        app_id_list=[]
        app_id=response.css('.b8cIId.ReQCgd.Q9MA7b a::attr(href)').extract() 
        for link in app_id:
            app_id_list.append(link.split('=')[-1])
        for x in app_id_list:
            main_list.append(x)
        #print(main_list)
        temp_list = []
        for i in main_list:
            if i not in temp_list:
                temp_list.append(i)
        print(len(temp_list))
        print(temp_list)
        more=response.css('div.W9yFB a::attr(href)').get()
        if more is not None:
            more=response.urljoin(more) 
            yield SplashRequest(more, self.parse,  endpoint='execute', args={'lua_source': script, 'url': more})   
            



