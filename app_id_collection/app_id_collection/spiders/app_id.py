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
tag=['8995720070395009785', '9170429172928691967', '7291594440295421683', '7141422999851925781', '4615294904370855658', '9078867188205035581', '6822219618520028060', '8893416524524614289', '5233977513008149898', '7743147652174683943', '8143693647320677203', '6587763128761242837', '6366887713955877952', '5783349908488911518', '4938252670488978604', '5456580002557810569', '8479499838535781328', '5803646126051297915', '5156069794537632563', '8154549429077556053', '5106840250277424230', '6994451850844677193', '5364549886656237707', '8641419559025429772', '4929784621333901651', '6371814045883058685', '5340549118715827796', '6386880847407346207', '4956329742578536047', '7485607439357104608', '6551395740583304095', '8561672040185135699', '8515798927792807765', '7771402521187096313', '7536219039467846430', '7649690726517942064', '8802462833480602617', '8270010790606670648', '6273502731415291542', '4704522535910848947', '8602102065353239288', '6396186003964798851', '5235045831004596227', '7337209548754262466', '5246300199446996632', '5665699913819223256', '6749293384429867265', '6505108302608729574', '4943639365061897836', '7977642132858801607', '9210967624282537513', '9141303443900639327', '7916994666721493585', '6128395532148358537', '4901855505095443664', '7540835702534334702']
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
            



