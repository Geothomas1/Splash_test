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
tag=['5420708822204949468', '5459971821118428491', '8703188444820901409', '6679372282266898778', '5425046339221233817', '5201048665477510230', '5687017629751516599', '7925546160745254623', '7405897792531241861', '7248774322001837476', '5086511738714143296', '7706157367465695391', '7678377057880115903', '4804663101248027923', '4999857258788991693', '8144537927249106648', '5215791084448596726', '7732277663169323953', '8938624429740527993', '8139740150255942830', '5286313046149717341', '6039293906417601028', '8876200567875066241', '8448657753216137898', '7453362338628742336', '8837035843345397777', '9196571540206830424', '7418205702744152374', '7783425428430319231', '7756911561028895412', '8693995815298460083', '8120985476826283671', '4689780590694617949', '8332149447945516079', '6502483039297512592', '7628981794576448351', '8891867835391229734', '6195084937397236732', '5721804372984655846', '4773270709540091084', '7607713305705920971', '6204284756430929927', '7850090303831496329', '8092083733483528004', '8614024614779361590', '6600704821286067966', '4740368439505063702', '5240153438044194413', '4688156392129107478', '4772240228547998649', '6037100722531414622', '7275803653252080195', '8319795735916109436', '5086466461784361237', '7967994347502615844', '6496719373857236664', '6611656319753085147', '7308638219049313366', '8508730787410367067', '4762924311589216917']
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
            



