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
tag=['8116929863552368528', '6386064194858110552', '8357215197056212871', '5159476328166152547', '8983144291202700318', '4714251290290029198', '9110943781235158770', '5182579873928128375', '7483256094537911230', '4998454608726028489', '7182270106089827653', '5099730587118896498', '6617207406144923362', '7149891497244951725', '8524844809417490477', '5200379633052405703', '8546574316005690870', '8739136657890888333', '7137133722391185509', '9057099465402833906', '5961211893873529920', '6776354245234746269', '6709487986774988367', '8184648133727486492', '8542576829345815866', '7712858277598805690', '7557967758400334031', '8530342249973296088', '5103167663896846281', '6661385988680019965', '4684792103319344425', '7151975205711790237', '4686007665185340811', '6208323469296928440', '7633114092336105891', '9070296388022589266', '7951580776444829281', '9223354510663937925', '8774174416231479457', '6154096491835065032']
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
            



