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
tag=['8159178402581071310', '8673675966644472691', '8260185806738829255', '9089535463678444622', '5507600432824812776', '8283437362196577670', '7611050626161370217', '7751187092097473631', '7320488944777190395', '6860744363576313870', '5485132157030116228', '8541174606896432749', '8093300169416442762', '6114591872418649352', '5963941792160768355', '8488578893451705294', '6973112651004227491', '4954246848888253341', '8251806090683591057', '5867315612122047517', '5636651079416583942', '6187525518349627915', '7834216297642247382', '6248802720099859869', '8517637508097506218', '8762621520142878979', '5989078646951806928', '7348725256760208886', '7662905679122518100', '8934533445483851325', '6411988877564638401', '5102566737544958297', '5829238441699699340', '8007459326923961771', '8843845419110498954', '6461979934320944698', '8544364518910119267', '7855021431719674982', '5643076774129410606', '5914057434208552564', '4701377273968073520', '4988742475061945692', '5441715344114404890', '7101346334273770676', '6385886611375220995', '7460216158497312684', '6229071233859325421', '6467766338302134183', '6486871127645782580', '5664996009599347989', '5778842892157655761', '4859546956540542742', '4969907597570144758', '8193852548395651690', '7344257759439574997', '5035510253884815172', '8101150351553161901', '6855209885350372567', '5701380460594325565', '5961998412254737679']
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
            



