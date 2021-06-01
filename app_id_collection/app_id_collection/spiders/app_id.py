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
tag=['5620889393122279006', '8659586286000597870', '8483257072057855193', '5077639332107958113', '6468747288125316949', '5645955107050601579', '8348222772006992287', '9080608047229116554', '8313833248183680989', '8232806052778546322', '8626204177560960396', '6944586365902405642', '6364397714795344804', '4785751915536200026', '5409445206423632349', '5371016495560291838', '8602434727834605478', '6894329953913172501', '7286597361735456688', '5730143535377816599', '8980654138222059988', '8839974981132368844', '7069493000480269941', '5780295628419977480', '9050921638056332564', '9171875808693189975', '6215795712492035151', '8761402443895368282', '5419502119363831668', '6195678933971303034', '5372479030788126247', '8631053028852924176', '6601610408625971464', '6237520006569429147', '6244007539395849861', '9063331433166018918', '6793654541297836619', '7354115712461244822', '8826497315748893695', '8328809876018429993', '6785438633402301341', '8191795874647207046', '8492883584093420773', '7718604252071058610', '5836148544871025856', '7044571013168957413', '6960805561677881108', '7957422126241298606', '6040117667409201430', '5883001615466816822', '5947416190654345356', '7851230179866623746', '6689475869932174185', '7364667506647930565', '6895989570699329252', '7300929210542684200']
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
            



