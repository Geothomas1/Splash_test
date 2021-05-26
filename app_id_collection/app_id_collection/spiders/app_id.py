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
tag=['4670723780649918393', '7476118101838430837', '8154890898988443204', '8675064805624595223', '6552292797797350547', '7399617346466789039', '5920436235616724093', '6515294028940474703', '8538780467778760623', '6074150467465879632', '9056201477378752336', '6421926470091904561', '7975727898002738227', '5554817563841450306', '8898272033741379577', '8971269726951586156', '6123045985072964169', '6365105958166788996', '8953454543428300392', '8662370508378165173', '7036987662108625953', '9029489026925534504', '7573841578600866566', '7341132395115273192', '8217276847831656300', '6605177127598613526', '8259563491158815907', '9106503430443697227', '7685610634539575262', '9020630781856452806', '5635094786271580047', '8100907766243743423', '6321863655809133116', '6534515373655701527', '8458932010894797678', '4978685861148140298', '6928858958961308099', '6918995591328992981', '8895676778494735375', '7481325896989786351', '9069622359441379157', '5163358177880458075', '6492603374763106047', '7122494752371077085', '5504358693530516676', '8433779544529623933', '8565181914239008089', '7337695826739966257', '9038809124293846666', '8905016740614814386', '6602470455848506235', '8074165813253809062', '6995329935326680728', '9040606661544991090', '8627319443195744896', '5073006109241615942', '4946092157052757127', '6953873961894982344', '6728209054982313870', '4929115468943945630', '8953926015114043588', '8373648077701842312', '6551475355164573089', '5125225846300595396', '6157596436859634904', '5226385880360646467', '5458925964857615889', '6632390354737798151']
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
            



