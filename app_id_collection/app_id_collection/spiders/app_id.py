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
tag=['7533872430110682302', '6324003795898474623', '5223666325021766421', '6249013288401661340', '6267658277504221745', '7876003438446573934', '5337549402106903769', '6121285110561874259', '6452113853405581677', '7448460448507458941', '7082921952629566940', '8526584009138042224', '8438812315220332424', '8931434831079114210', '5058303214697052423', '6638307764583238617', '6318718552866959040', '7180705310724550542', '7129773085119877408', '4691791004319566419', '7394025895611767371', '4672672872255695418', '6991477186276090959', '5614380929317640208', '7867565603098346127', '6129653303445907904', '8794931741184455920', '6120114643739657698', '5122682326576823713', '7526537251997965205', '6522093978684340597', '6558349509091194327', '8452628096482519463', '7606677356484597883', '5292743083322529285', '7444498667970408351', '7361864757773973698', '8863961233781649606', '8315630974564965855', '6335862344631479400']
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
            



