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
tag=['5894511852271866200', '5436418526600285989', '8629418334751722654', '5170436684394466958', '8630762949184553155', '6350702740167040037', '5443139452879539732', '6281308422554368875', '4825906499086011191', '9159635076379979111', '8665182620209793262', '8760704574487165347', '4623286321516583956', '7847373722248999326', '5897884894800312966', '7170912588882756363', '8127418737583233594', '7292524489658310692', '6099002949709376719', '9038987167384069337', '7577705676061143756', '6153139240440992966', '7816191958241438564', '5988493234345857503', '5224889003424049307', '7633098540484858099', '8930297593731085321', '5221434113747283744', '7906671563960965829', '5615837024201601069', '7865210919269742770', '5320296801126709706', '5132182448793417956', '8466050068348543977', '5632469769016083242', '8671028793976441754', '7286006040182189336', '6150832974034049823', '5225351988857066521', '7482199796569926299', '4813727084772339873', '6277205961979326104', '7656854150232237222', '7889639434013456321', '7435619340570388319', '7283957560903084645', '7599871065409764286', '6588069463757577537', '7241866750836063639', '5228919408802005727', '6384738406445896780', '8528754628566512212', '7370074906756831979', '7438325560600385328', '5016869936143903867', '8780359271699370767']
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
            



