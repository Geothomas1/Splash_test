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
tag=['7194701061935746331', '8893210906869692403', '8199785594128882636', '7923366608034857427', '5120296861724261174', '8026010256970589886', '5872879772780128207', '6221956091264142934', '8115338304887794353', '4647998716943242763', '8029000350509758753', '7624087648909069450', '6566178840531972758', '7733741103405331411', '5974521450983625733', '6939825389946648631', '6868990598419667144', '7580247376460930437', '7217056627722461105', '5072167277340167087', '8025250087829240432', '5428398549902206966', '4970433715119406208', '6446682316861038778', '7586540184652061915', '5857653738358293115', '9071345321181278555', '5433521765293680094', '6037919443226965942', '4936412698242351052', '8090798248190202814', '8525222608937713488', '8878830896945339393', '6838434049690937885', '5501543544118454799', '8638960377238120611', '6999936915819691540', '6262318312652386413', '6991001366548054138', '8122380170265437886', '5258410538530331508', '7891627917012506149', '7464626526023378990', '8868470488288288514', '8034774621848980096', '7891990035506213180', '5443760275283054929', '9147862602579135510', '8266018840834401489', '7060820296773716703', '7448531932168845723', '4774180223730898597', '7573454388742517884', '5764342127169072665', '8539158240634698332', '8588152049236454312']
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
            



