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
tag=['8709778405099196610', '8590216665064766046', '7313071118166753251', '8370471549358961466', '6448767934614611181', '5059535972638766074', '8045558678393484418', '6846696547364936282', '9051148467838867440', '4866243252042612314', '5889756495815669616', '6722520191413703609', '9028172463489612589', '8057761343338570071', '7346890429246481458', '8371661988319481726', '8498546092863948251', '7147364953355925342', '6127710176424954328', '7685892437761759807', '7027922101885787742', '6589881289812568831', '8110372698572114210', '8838836793258515669', '8964047567910934623', '6598150714989455777', '7895937703172942488', '5436702375879733393', '6938482136206700895', '8492011720422545772', '8859483327046261115', '5142380748638255425', '6249474150815832810', '8104400011369756806', '7388311809084551192', '6510695609505760290', '8966031332439583310', '6481597223887452767', '5309909142399228911', '4720801821193867957', '5156305102781570481', '6994681854530134564', '5815780331357697328', '8803730092828848701', '8092475488373003589', '6684558620390788436', '8319513470668686725', '8221543379727696636', '4820963801024833785', '5047194287905225080', '8774302866580466365', '5616767694707286949', '7570386264468274868', '9038142496959137105', '8763646292673276542', '4872521940523871000', '8365380333087086858', '6648939854131219701', '7086639890153802127', '5612028046311546976', '5707135190968836386', '5030631237943867779', '7458759891417339833', '7442512093988977097', '7550045746771355552', '6284879872961307001', '6317377084266172840', '6250435481226500002']
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
            



