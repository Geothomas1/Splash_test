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
tag=['7204489549650488638', '7722690357397464940', '7539283503853912983', '6566871144750818949', '8243711149049514147', '5191761042352704030', '7754771396894325601', '9210364585215193839', '5776855233542109986', '6096521936677288627', '5049716058492154239', '6547550292463699693', '6366521550521769421', '8983915462423286733', '6338444175704906189', '6723400576142623912', '7078526582929517380', '8130874062678102635', '4945538336540984852', '5166737219553828056', '8131524560553387735', '5727175315664686749', '7582883609214407366', '8649821150617465428', '8595612636029949156', '8781860391294098960', '6469737508386097450', '5794076555993790330', '5078624827800948156', '8636572569301896616', '6839373562358507437', '7897440408299849103', '5384315439566878022', '5867479855083413358', '5793131769291455541', '7969812150912334893', '5732428430614709823', '8445965806113207721', '8865705844905669746', '5981692610893241187', '6820708676437601682', '4818827973213097682', '6049000952442383797', '5905075206034782634', '7652319184326305376', '8289061725019366919', '6566703160137367852', '7836652722214723436', '8404275911832480620', '7572280586858999266', '5414502912736144183', '5952057666589164114', '8681851836907150725', '6568222516246310104', '8865545314816622100', '7630062615108803383', '7732859531208579661', '5965345943534993786', '4825767348403401016', '5699748993706667470', '5959302594954224598', '8312672699187550923', '8211463143407204344', '8175882918942064915']
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
            



