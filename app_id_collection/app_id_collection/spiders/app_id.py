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
tag=['8479978250801894968', '6350812843384425259', '8087690677787104388', '5940442730526150740', '7754299051310736648', '5842794946655439599', '5938698410549635800', '8560896980200974117', '6617684267668392827', '6198604186555911148', '7933276303649799710', '5736644632265196448', '6885971572534429389', '5153115824697509604', '5014379196186913274', '7848714631248647807', '6058954942472166484', '8325086679931393934', '6791448562470274683', '4864184490959972033', '9073046712873571174', '4685222685142872740', '6862449449406721637', '8909710381170719662', '4783625756997706919', '6205505168536850943', '6135842628785949465', '8844135140200071971', '5785738374867324679', '7438122852069561690', '8032778238786004978', '9127085344518131769', '5847630470409183604', '6004234844335424634', '7599990871584420202', '5852388392569144192', '4753653211211777038', '7114241916351776334', '8309682325887107680', '8590322625183687218', '8118276161891520360', '8944107188762457888', '8199098231732854944', '6226295913146423475', '7580975671594212757', '4971933654775461718', '7849918240195917512', '6894428587671688023', '5204367238873578728', '7795486920149316148', '5254965014282035484', '8585116827791002609', '4651878149263795817', '9150013904104793373', '4617059902311600876', '6837976706052090398', '7686535145001463802', '9029420000904417556', '6827864225755481778', '5800265888256212444']
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
            



