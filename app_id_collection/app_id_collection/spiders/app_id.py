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
tag=['5347733799205311152', '5660637440735548738', '7540747588324462452', '5701224935704459046', '5651326047098726145', '6888883772727115227', '6831347196585294074', '6184878364975065085', '7838247957022832873', '5650553869146361851', '7378319622504015006', '9151678898068886681', '4969377702592576999', '9034566954108581696', '7175795338936881781', '6518762287416221469', '7989905498280239391', '6874944073576660873', '4798224139646665805', '5961222610488028736', '8164059240719591693', '6487624215990916581', '7572829954502647873', '5987677423373453667', '8903977957094635760', '8974365380916985185', '4763426919751091250', '6889974088280524745', '7716127734668680988', '8322441501718790975', '5661189054964685858', '6569170275648214235', '5824450851143252772', '8118560402834447734', '8130227103677012383', '7134204144878147170', '6037306624302905962', '5955504303710293531', '4711210169029662064', '5212784702680211570', '5153970434677900725', '8478719966376769106', '8230711967949052425', '5061184589870170986', '4854859328254660686', '6873242585468978410', '8137584258433407371', '5000924930502885531', '7071430644205651346', '6133644072791585622', '7936592673408969848', '7586816541499054395', '8119201735490945823', '5256952142629301807', '8612219469474238403', '7195717269126894240', '6921944108755438401', '7395587223920577986', '4745945509034989253', '5557918495408778722', '5641733706469510654', '7618782448745223948', '8628505356701281729', '5896211539745406657', '6388379580000600295', '6534348997123710607', '7408316580069139914', '6748103485371623104']
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
            



