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
tag=['7716228230748897036', '6048330731809851416', '7164296146373920412', '7945334852914508868', '6942142552289745812', '8629170655792059666', '9006258696511891543', '8698265302439067602', '7966239223691991284', '5809016173677942793', '4641937996896073511', '7375514989634348096', '8876954281282300674', '8687901223383578886', '8440808609725903215', '9015203819023888785', '5147131516416340156', '7553056616786487578', '5646202169218337194', '5170801367022247403', '8090693633056325737', '8267250715864627356', '8130748137413633357', '7796957681325884294', '9008512916294064689', '8681371055621450770', '8204995230349243611', '6593072047782423623', '8742581992708980360', '5919225198905298285', '5440031783419136609', '8251968111831204960', '4747054059053689901', '7446766479361865219', '8782024942264996557', '8025251125525325507', '6406605262562397659', '5838203466544335658', '9167077441939905288', '8689413348144510726', '4961251417626717975', '5249745257304775233', '6139151936887469325', '8994823555535947297', '5307561133207059406', '8886227900314245851', '4939856088512395434', '5141453741202312821', '7363132536650115149', '8125273617126905693', '7938327705608016460', '5299533013263834085', '7468104821505211326', '8017166847249459940', '6818705512348345526', '6653381554552608114', '9110790061066510409', '5449938194077868600', '5211052597291903962', '8800358950603441552', '5720201508488935683', '8295232434355568244', '6704106470901776285', '8200079647088148107', '8718099592606828786', '8027944223645528789', '5334667546901985345', '8915860611905441330']
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
            



