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
tag=['6076188880959659308', '6107564267464061471', '7966969587636132610', '5602679406184809201', '8168561060247435718', '7583386581857184292', '8925009808495872655', '5933605888688671162', '5280484755927888506', '7458581181600475903', '6373819058374763586', '7631851640617919584', '5553369361111688446', '8181308818889252563', '8835967580610526515', '8524754743526094896', '9141750618695922452', '7571604236382841052', '8467541272657530879', '7150486654513960098', '5165250205043770908', '6730650800716462347', '7936715504330996234', '5983984683838008065', '6715615326865035153', '4615366350299647550', '8819978999231673817', '7493277743125943288', '4891269337133308814', '4688897177178240761', '6819891215745783080', '4662933143335921712', '7264588745818026095', '6126642677288670771', '7775567806010537459', '6356916929632717108', '9057929446534689331', '5488559295346239930', '7055277608580021456', '8332567249337938895', '7629590933343014189', '7103108342678811520', '6846498614571436049', '7222790494269188756', '5222150418450808309', '5430471338578689800', '5010243897601135075', '7800624242700470111', '8371115221571785228', '6936259992566916576', '5707909975755622163', '8604769386404859599', '4755024113024098779', '5581592534810978243', '9005207387328486775', '6748661820728732000', '8724315754104842249', '8359132343347183802', '6091806103548495292', '7576147073264850735', '5241993506133000712', '7148047194848561719', '7530472701092303938', '6861887946029614399']
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
            



