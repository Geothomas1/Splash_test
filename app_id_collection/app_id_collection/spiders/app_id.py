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
tag=['8591905817328721633', '5679417018741405952', '7565130386452493444', '6666667068815062475', '7907687617742904346', '4876975009796443506', '4670314572380601657', '6364044311490385439', '6393996444219084500', '7296703954356624571', '6556021796856748024', '5985962371661457343', '7814170705518406420', '5028826338506205899', '6385687183514999923', '7686816901578000134', '8871447300991869374', '8256206686213875429', '5697607613490561643', '6687056329919449346', '8979926012949782014', '8109834627490819650', '5865949707468929598', '7548585255908818999', '8258690393910895203', '6109021294817947547', '6639265479425046477', '5978155020598945390', '6281343570527613212', '6554348131548284525', '6400754827318260275', '7400586232523501338', '7254277922138764187', '9014290287841011355', '8557832697427584173', '6956249493208539823', '6254454820416066910', '9151929342846745598', '8230828132597071010', '6238151696356560844', '7715819387061407285', '8555451279569310337', '6116560439237972990', '4882849435957978267', '5698427872328027889', '8271310691420682403', '5971499551560813853', '8175620322721071554', '4632046326871791355', '8224188600152187006', '6969017632527521961', '9127398276887290708', '7219430539037428201', '7752812657744381883', '5162320491821408063', '4668863756752057413', '8217590837223287498', '6792318074060470506', '8090141242981319114', '8092972751820770629']
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
            



