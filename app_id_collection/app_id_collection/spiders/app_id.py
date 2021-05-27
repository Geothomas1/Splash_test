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
tag=['7104035099060517441', '8544545754862217771', '5444074011238357658', '8729910867266158618', '5227432556506137273', '8204728169200850919', '7279531464255333004', '6334899502879763463', '8439959316099053603', '5974403493506643572', '6828369836201367746', '8153123179973820934', '7081479513420377164', '5427339907370037992', '6874502409942971047', '6035727937838970967', '5782251123896011416', '6924712529344561967', '4799836742395269025', '6090445815312506322', '8723773889149131310', '7744176682382186288', '5306288432367373829', '5323486866512435062', '5841678514837917367', '8637278547002844580', '4920931300690568181', '5216961176518154327', '5420503779188212094', '4979183016957201028', '7309562714306134681', '6516560123379855735', '5946944522108601201', '6879221541792195137', '5720181744631161913', '6378733716678671923', '6534960434700097716', '5840617791374848874', '8250123030648855422', '7262490676015806498', '5742339096569885546', '7646971368109178486', '7656121416806368318', '6323058473789380568', '8869191129111921517', '6602859539147257020', '8807124630437440963', '5117872964822656951', '7508335196188076676', '5124612406666865387', '9131610332319602983', '6914332474218778235', '6154099102081212519', '7261701047427833361', '4812767679051545812', '9074522596288034779', '5576226595038130881', '6411130759822356809', '8978102437919541245', '4656963459589533587', '8582725218442214580', '8667971263066860468', '6784766297083684746', '8075940778881445040', '7599596443444002141', '5172835379079385588', '6997782378623409598', '6915089700791489673']
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
            



