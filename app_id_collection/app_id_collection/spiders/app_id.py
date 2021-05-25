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
tag=['6526975909208527105', '6833224340303003178', '7712724056634878128', '6532660932403306662', '8368973448605152230', '7983952054802654250', '6787096161989365588', '5817857922276202992', '5791903491666456034', '6016224474518534712', '8824262887893727611', '6666524307484575308', '8610113547573092712', '8921679401133028741', '5339439688526437110', '6799544949365149582', '9014234262441242973', '5341269538359321555', '7938912700534515651', '8262138552063341066', '5507389985988608571', '7417460622172421349', '6506787135959915650', '6624515179786341065', '8638540542568115043', '9016304814663436049', '5241963629192893673', '6740459156468048015', '6838625006200449684', '5376961979615302774', '7377306658254094476', '9078315394529202806', '7164100284507696614', '8943152214811032204', '5757990971892163685', '4801668133387754859', '4762404732498328419', '5137029057877904101', '8856191954927521414', '7732032170429161774', '4979963923081317865', '7171321821456523658', '7569828723999179880', '5273609641822895185', '5252617253544088767', '6741253497478773735', '7707563051243025362', '8712288503469383242', '7741060143752467300', '5174015823301200023', '7346138505399201088', '7384551975305749866', '6903732618939055734', '8478872630440600985', '8383543423823353834', '5431990212408910925', '9218744961945094984', '9017504053419299868', '4904859999126777012', '5650803663569412371']
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
            



