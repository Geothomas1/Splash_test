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
tag=['9123812491921008688', '5728097603089723340', '5153024576800872517', '6782269664019970797', '6282684731005843697', '8174372288533118681', '6731683807831275369', '6577302870648328592', '5822213096021717078', '5853333145150653533', '7468053200786837292', '5971429899216613189', '4695876244147379929', '8240488481922277658', '5398206857754541528', '5299041341628503401', '8328429316342761165', '5154485573269866463', '8840295583612529864', '7305641321335910867', '6980587204754238046', '6623728016170574720', '7494428933908811726', '9013551797314132310', '4959636182114255376', '5071311690607119015', '8857752720402747582', '6498108890532922281', '8932756542093591306', '8596508094246991999', '8795438844017678131', '6320495026050646932', '7153234987225353501', '8187114035224036573', '4976229070857862159', '6984226324744477705', '5882317487803319254', '5379887007272023196', '5864193682754016926', '7571784535425389164', '5114071491282084031', '6235556904639743520', '7942493322084635848', '5136464053274088488', '7850864666261995262', '5054942435747955692', '8898414013277898839', '6511628244718441624', '7250144763348176786', '8284515621226739514', '7517762192686949403', '6592603558263828430', '6462054103300984753', '7329449789920614417', '6214957384838046712', '5917924469598617107', '7954891124376186534', '8204796524755183978', '5818736323775397221', '6151183678534693502']
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
            



