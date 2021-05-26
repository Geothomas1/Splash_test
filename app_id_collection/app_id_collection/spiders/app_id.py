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
tag=['4669203327042887176', '8136315382378132545', '4828871200628157557', '8942875603608518152', '6806649725022489465', '7916812924905508715', '4915434484296018008', '5488297168089884496', '8410661207844436775', '5475782052407933096', '4838224152832929224', '8147063640046341191', '6438442304380180518', '9016163668484085428', '8838874714125706714', '7944203679284985174', '7759178744316573886', '6197861290923488301', '7565019296387192906', '5862380440996769720', '8307420272411202010', '7407062282386417046', '9043190045821353536', '8163551612602112384', '7859787325617472705', '7919646284408469138', '9183174111592264811', '8914147685041410514', '6105430406818437429', '4994353849798235531', '8771317545470736450', '6601938328412444916', '8740850083931285856', '4854583837351730459', '5421152409492718785', '5177683690558207300', '7044232667654327190', '4956617900255040919', '8197481440010939571', '9064372708831390888', '9139591148216932298', '6121159968009666314', '5708747287967740086', '4726002488992363846', '7513456145392400531', '8760828275962064353', '7258376585183782826', '8259628758341847463', '8661878014763668864', '5372691576160298916', '9037849294063453883', '8277350895851998609', '8402746430568695040', '5060840925611644631', '7280077382840797600', '4841727983476251342', '5562657470327318152', '6768791293255053713', '5057044415701931841', '6250014561675017680', '9171086302492070426', '8416207043447482925', '5155355245681412304', '5319681001345076714', '6778078650826374100', '7123979710493100289', '5240682207932283431', '7175498397695458440', '6453961411676689504', '6977631555049169707', '7693324638603225223', '6791386075528920949']
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
            



