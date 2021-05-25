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
tag=['4618433724123513014', '7864625291948215189', '7349188584754176815', '5154817260234588740', '6939834408286503375', '8766811091380713707', '6675166732386446811', '7696735658928707700', '8967418906238242913', '5811986234270008923', '8857296246924027783', '6753970950335136792', '7392398332984990345', '6984446909759708183', '4614040639053382794', '6275348189975287058', '5948317449185134444', '7180033570035226508', '4817145500369279490', '9075209049379685614', '8598374527935459967', '8124753258668687446', '8682089108917139195', '5023941495835037940', '5748240921424352731', '5632310902070285339', '6895396026209445143', '5338428685228768256', '5555280587639828558', '6551166613327279246', '4981263827753217616', '6526849192653249949', '8289872589429861020', '9098555508440962357', '8587552636018665690', '8066945518679886923', '8755468586744228847', '8056968195025459913', '4898227705286580329', '7718290318162278044', '5189864798551549844', '5451980547453242281', '9066270068204080150', '7335928239238505843', '8592465479784391771', '8846176578305829899', '6268342791696297501', '8416251428846808081', '8870698872969523840', '9097879719032268880', '7385186559083055414', '4774750981480425362', '6752781324834040533', '7428207504675713975', '8722561714604702600', '9089690226068755140', '5001928365463484246', '4999319615802742376', '5476708431553329188', '8779481520239583136', '6367716090246694310', '6503367801703463686', '8797606602150852799', '5690554679184343378', '8133481498602721190', '9115536253910812195', '5416791149139425641', '8952936659892967594', '7564565688121054318', '8058057367803240478', '6459841574814640605', '8892353057985107644']
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
            



