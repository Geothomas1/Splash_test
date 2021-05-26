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
tag=['7179287243060993718', '5114272715147548429', '5744250744683923237', '7218328123763758749', '6643936787377554632', '6719152071321097359', '8619811736478976394', '6697529350874157183', '5934994852392189366', '7600909379734246875', '8778828358166779458', '7077591484544142954', '7407905776305386231', '7139012116696182477', '6223213904772552833', '8371123051854123457', '8171504892132977098', '7685912509108787823', '4635895265759661402', '5462133752033155697', '7931325864631690597', '8184525445249067682', '4941219769716798064', '7407415213470377078', '6461795323068484449', '6595065013093086644', '5678518337334097657', '8546806469441795370', '8188798347215348950', '5374669284624616881', '9028863849753291686', '7207353240617278297', '9066613695492663007', '6793214589909398933', '5552345965823317962', '5249691552143293486', '4686109854392923925', '6104674748755953824', '6825781058424810632', '7358029168600018814', '4696719130256827908', '6079613061713099607', '7245842284730140401', '8717100886643009180', '7876233969967658979', '5555075365418201058', '6058049164786115726', '5218274661492440725', '7394037668683303647', '6562987040286469753', '5353856078152944274', '7285537130844976361', '7750722112742960096', '9009189213474216404', '8130218093376969933', '4750253941717902097', '6312383737768576194', '6708486207015661566', '6628136550093428886', '4890058582469040544', '6231792414055713984', '8808650414829319413', '8821071893519012582', '7135742860624398604', '7727452840879829185', '5060105986449116988', '5947448231978062060', '9185389251891875863']
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
            



