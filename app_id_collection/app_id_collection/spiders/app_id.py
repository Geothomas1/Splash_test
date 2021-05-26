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
tag=['7949046646500376065', '5239210946171555116', '8885327658615984766', '8182428067939507564', '6052556201526376333', '8345551627619974531', '5391748901058115192', '7848837016058883513', '7221985231348909772', '4755312835438463546', '8664736627701106364', '6795394807191026092', '6241199844326640937', '8691401709562918488', '8006201440649250946', '4660009256913780809', '7026171220521029572', '7565352153940947938', '6959162256766858229', '5176424536227611426', '5666922350507328685', '6587591866455194134', '6866421752347138556', '4784455511465829531', '5266857262535790588', '6672469902116695786', '6340832613439337512', '6216613693949994568', '4675666895721708194', '6885562361278675020', '7673039342930938016', '4741116895513990521', '5211291270179740668', '4707001329437482885', '5029996228958823960', '7409902364448539840', '5186036541371069782', '5836447849648444945', '5410054524323906567', '4853611454722679108', '7727017089264403666', '6895909638649087541', '7130400708315066676', '5769316720205135998', '4747939615681183184', '9067163997993645846', '6925672714464962353', '5514799690887844072', '8426036374624640337', '4934965157818997189', '5841763473616280218', '6560494154946582604', '5961329008298145666', '8077531523695446125', '7592225962463573576', '8645346994844388714', '5500764603618407609', '7783510149703811815', '9199557590468440684', '7145533335215549002', '5147126645053306716', '7044091869574429442', '9201210272811934140', '7625948163163708474']
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
            



