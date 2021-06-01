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
tag=['7531084747324353001', '8024097439982948670', '7948217150960306538', '7874556652975222074', '6416759558444126759', '7963861995253820397', '6901777831763898198', '7220552623322591052', '5070049985839206168', '6933693082851133021', '7020372097442720101', '4870634195962434660', '6674685912319151468', '6130128057652620670', '4877993685777892622', '6739605084544024785', '4836053772571839291', '8759775007428330778', '4747767788586989016', '8697285833978944428', '8957257278384843308', '6817552650698512610', '8133785272481234374', '7774702382966379391', '7190700878030374188', '8902764485054928294', '6759105438312971240', '6025867385768713346', '8013309201265156122', '8366355937984342588', '7140467268444677534', '6655682252822012643', '6174571894355444820', '6036800292703655527', '7344279369445908245', '8583927998009505911', '6720061383132466193', '7302183230909507100', '8622187086845173471', '5188252028123763881', '6598612526800813476', '5988547777633162463', '9078922434998563948', '8484112492384708617', '7258546345541077790', '4956499348948608526', '4966398933878706367', '8781866491214090054', '8647251961827166428', '6694702054422561252', '8473771265693523546', '8277080783973493132', '7998224373148680471', '7518575784939651133', '6177640638312620392', '5230170147318032032', '4612284859372265147', '6734469068130795209', '7697010883403227114', '5229044359910390996', '6599605237578061083', '7918154236259767087', '7125614350471173442', '6173162408627377904', '6401922929027811662', '7277513458183393295', '5043210317996338266', '7058847356618429150', '5219718124107141129', '4731909231644516009', '4941143222016053503', '8211852829993663736', '7280726339009808194', '7514962098676121872', '6475314061831648652', '8123512155073909949']
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
            



