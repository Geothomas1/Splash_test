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
tag=['8003749631382970365', '7415446147207133288', '4656446977926344285', '8840924357018375805', '6530032268780288604', '8064845311515072615', '7132769464697869701', '9017602380275422612', '8562773004655986625', '7748575553860418135', '8056081270926088000', '8725049224739336888', '4975233079751375845', '7430005971129979939', '6695914693084197974', '7324901894058820362', '8363066653715655455', '5099568928192641603', '7058574609868414744', '5306026138603953025', '5716792660975413154', '9048164685815270545', '8654857146923314069', '6860682062931868151', '6797847443053504970', '8838282687698538304', '5221268878460815137', '8854046095342860840', '8917851730847369016', '7824476488888653707', '7902108998421983402', '6921603254838455166', '5796709972154726091', '4967668689100583489', '5704336914526446295', '7083359238856735278', '7563190634447240733', '8590410519543928991', '5122078557185708602', '7531036279365083829', '5035593206881993737', '7434551957840228675', '7962586262608152907', '6485391978707855430', '8627430062970759200', '7403312528799372286', '8633084113062504862', '6743112577217741255', '7312406618564292928', '6341774947172229745', '4894319256740044619', '5815729923720981222', '8050969478732289508', '6977045184726199296', '9099611275032875277', '7977170630395123485']
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
            



