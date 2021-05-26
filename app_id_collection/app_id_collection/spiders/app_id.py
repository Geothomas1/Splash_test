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
tag=['8288949974336145664', '5242863849928091749', '5322463166645328794', '8686777883246727435', '8017025094833058699', '9181995351721820592', '9028760286659820591', '7075752448717209787', '8458169143809274686', '7214518522526960605', '5598678925880105743', '8055814644136743640', '5092744002560627651', '7056043696111377865', '7131715622223676843', '6828277570333741638', '7589629149738134627', '6179333599422118026', '7284572583251564593', '6814080382659389431', '8349219663172884500', '6315264515513936978', '6551329998890107072', '5665675718967672371', '8394741187094884031', '5661652391126682414', '8322183708233004746', '6496935689472436896', '6565196309894410553', '6769545696572660584', '6207033481735398826', '8970937353451670817', '6761717421830713329', '5291215316579422236', '4817624589145649671', '6936092317793415248', '8028027276029539706', '7657539983437808287', '6135734902289257526', '7752478169622360555', '8443127364568012247', '6440232003459573263', '9075470128297220918', '7758047611342796052', '5428079163366109716', '8787222523277575805', '8790466136719013234', '4792376898532889435', '5685011199410133893', '9210988449501471119', '6818006975402134890', '6520891992350137733', '5494023164643318363', '8094365027314611194', '6109687296174910707', '5949213677827314444', '5288801691345817860', '5983106780541788929', '5640921916490189608', '8621356515711813199', '8811072186156870345', '5987576212729536959', '5137006670632982516', '6250598781248816207']
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
            



