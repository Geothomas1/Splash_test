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
tag=['8097327295782224972', '5651069208159274068', '5720102320725722842', '5047261445646523282', '8453439161326246298', '8110782665597662297', '7083255100475503732', '4948736446489210813', '6685471243368670361', '7725592651191690915', '7296978368666863754', '5955376842394100503', '6687412157194667067', '5214498355809316066', '6819090905476051203', '5828096259591527003', '6435117250881400843', '4624407529085083879', '8021478635974897340', '7549168917298180505', '5817296310528543711', '7932272859618649644', '7965993558834456828', '6720812189273386984', '8217643019561956443', '6619297667756939318', '9082460539100844090', '6349110563570293929', '7718870297437705482', '6205683605591638523', '7087110576666817791', '8596908932345219128', '9209245489607429707', '9017749172020909225', '7982928769647789263', '8041079586306851398', '7121464574612024266', '8622359179213986693', '8967076844047270618', '7778572113732649001', '5226833943438219806', '6086323418252460413', '5848238051303471844', '6899714513196690550', '8633881548135114821', '7320924825020775402', '8765496568993320175', '4746663409845829820', '7203367807104461181', '7766904486143973471', '7657937062358536243', '4959956475386551351', '8721972929753733129', '5537580980494152656', '6410686151642848556', '5479101074498112663', '6973337697917873077', '7916723593668409540', '6403281814395805505', '6950644879345437271', '9049036626684911004', '8925208105863549596', '6250856145409416433', '8805652293480037056', '5199423706230535674', '8410402890679871094', '7264264592291536829', '8054002835105712663', '6758611429379891066', '5921818219878461311', '5636975168449518957', '6373331911168469074', '4720842708020789561', '6622872842616575702', '7693005235803889003', '5481396588085487908']
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
            



