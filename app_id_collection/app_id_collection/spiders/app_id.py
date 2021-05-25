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
tag=['5812304909436304248', '7580367693519200934', '4657818956665110678', '8225320434216531571', '8462280035499786077', '5306523707855018927', '6760904213150515779', '5834583615698523000', '5599336656845958877', '6987781922487171857', '7747018980996676706', '8704058154134341886', '5436821140300332202', '9100987229490594552', '6770967800961821170', '6752757042013862878', '7383254505715845190', '9015975277777351194', '5376181793611066520', '5456521343096501615', '7163778225628250850', '5506261269823501188', '4682443305447149344', '5690698323397418036', '6431277203231892503', '6588838318902263047', '6974524234102514996', '7885874865225044707', '8152171058994793947', '7989284771704206032', '6158777224797397349', '8218130893574223407', '9128933030342617433', '7799382962647887987', '8683645393038129621', '6705012243732083162', '4833631721401556405', '6012290395663344494', '8172762396014699833', '8651613073428201644', '6094813900600393832', '5108171472318498686', '5658978653146000308', '5570778333475699533', '5561511723961851647', '7616488647059196043', '6485284117575443039', '4812478238527206575', '4614371506383368969', '7944454766776755626', '8237892545547280535', '4815662748970110421', '7705235751403622974', '8738346728819202913', '6760866994059232123', '7403841880510689459', '6191256211400115270', '7097437340895268905', '7011194008224618203', '5180801233567417991', '6061344400664075363', '5173595168264520357', '7183498239996378832', '4694676801443792357', '5359671468025257681', '6643283248276837084', '5355684462625859526', '7544996683581780264', '4758149885100649433', '4980032927948956913', '5768024681920229537', '4869789726021163035']
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
            



