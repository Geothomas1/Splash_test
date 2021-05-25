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
tag=['5580265499093584060', '8716604562581366167', '7327287903043649696', '8696276183729924235', '9101988231994178387', '6962861495672339359', '7599199463643867003', '8345096457009857332', '8137773525157158372', '6704519974453634512', '6787993505421712279', '5541525902474530364', '5459335153872794828', '6435902680740421122', '7905181527617608631', '6300092002804376236', '6323952794952291364', '5747026445180336760', '8415912659298348819', '6112780680526671052', '5021075249363107291', '7103362745338454523', '4821575300925720191', '8882354990832190109', '6105131169615764315', '7358172678286648464', '7883011244252107870', '4918673841966471606', '5578076551596578494', '8496570499954859898', '8517875328951538273', '6563849290382059195', '6764465375971697130', '7546301337522361795', '4933067143148015449', '6340910406589900605', '7261278776325192080', '7319743226419474571', '7081306527254237283', '4704243534032952165', '4674110393064144189', '6985949626675868665', '8161347633803180968', '8149813369190878382', '4822382670314547439', '7150538202108340916', '7438645831812204795', '6098008304156073288', '5519787071394550960', '5712886815911212474', '9194867855389584881', '5142155412638519962', '7641674511729339808', '6351423160467886303', '8387136731868908968', '8275375362039736860', '7675178358842568877', '8009229946060736142', '9173704920238080377', '7918041667791735060']
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
            



