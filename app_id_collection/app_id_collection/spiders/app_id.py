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
tag=['8963505046208124552', '6234384250151089247', '5019227939569474527', '8861516167568141314', '5057158803409119116', '8220709209344071020', '6696884048369103258', '7483889618076875128', '7712582785598064684', '7797209574326486135', '9200952197196338626', '9201214811880313324', '8947635130653131789', '6289421402968163029', '5485674675041700461', '7906675825742087969', '8355317828905497231', '6624032394863046201', '6781047090952075162', '5397404940587910601', '6577204690045492686', '4698020563885400861', '8992197787187790047', '4845317959578407531', '8810793461269970613', '4935989486813626412', '6456804357929516378', '7767058403001139720', '6178218153041164662', '9144907755440817486', '6473478508001100229', '6837340316160309504', '6513253884633807862', '5236264801021889214', '6548364044790973914', '5259442751908621352', '5109527294243675565', '8548892154578245906', '6867505837657091793', '6833765329689499967', '5137364340371948270', '8154918239958650103', '7830868662152106484', '7673112796234466939', '5425851731630649862', '5014688380385987684', '7180923903829173750', '8088934845636600471', '8824497490851177169', '7095191932242917478', '7473634688510685864', '7461875482624565371', '7950231840193319235', '4661863381205708375', '7765342014181269125', '6504588202064231646']
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
            



