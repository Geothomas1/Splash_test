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
tag=['9119222623696906209', '7031555095766920906', '5232714945229704595', '6263143737265545368', '7956555417936606571', '5009705785755847056', '8323704044814502176', '7974710796837853049', '6886509610932566808', '8472999065862497295', '8956852777831767004', '7036574957367180067', '8368948448089379580', '7170925585663768231', '7814682647826426932', '5459111286458483176', '7109150129408994403', '5866197235370143851', '5918886822299407940', '8288140978486338370', '6511610823141170799', '5542664862554987351', '5792524492136728856', '7841010143909250658', '6508423435255662057', '7461930086559429192', '5358911346707070350', '5666787983522927691', '8959129914401712991', '8161688226144696744', '6702080955149358932', '4906643743900885055', '8768538226086432388', '8701434722272589112', '8468154191454176983', '8042966847243148679', '6391144859077210240', '5058925095315741358', '5214322517935772344', '8243224984215793974', '7956305059448648741', '6289768667756396269', '4655902803546920441', '7094010574148448555', '5436652398406306309', '4765888376621762587', '6713685079303217879', '6288319105998999095', '6944833119776527742', '9008217183799788919', '4793060926428937798', '6385361585165096550', '9070930878453486775', '5237026479680983773', '5631277054416555288', '5971439940212909794', '6927733606147326559', '4702448513736386944', '6687843170219791821', '5355255690323608004', '8924614755826120836', '8803941688499250073', '5778053025552629219', '4919418188528526811', '4715688337977670481', '5790243058703504531', '8513870476895988968', '6644418245755743952']
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
            



