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
tag=['6563627291842220556', '5231576034709792290', '5087762991600477126', '7344682203984969489', '7648040954584409835', '5512309071654224688', '9008800885912804438', '8945865717066792308', '5089610771888729024', '4613782350565256059', '7551933026316655573', '8875874747270883726', '8241779035992301591', '4658626098021065387', '6879926558019835955', '4981469010291633714', '8140189918947319673', '5912775720545287750', '8047934934658087361', '8002179159227557121', '5952216370978603933', '4618617237092803226', '5305300123894740912', '6290037150334340667', '7088499213183081717', '7141522653621419645', '6282254100602096234', '5630504178677387591', '6384934976092252003', '6225016287766590654', '7052234466538329482', '7106898322842717259', '5113262089135803825', '5554956796636976183', '4874184168394627854', '5000835921295563656', '7632206278250359802', '5630855868907455314', '7119777838063241228', '5045840654985981684', '8417797919676220456', '6294124537083868984', '6984862038819329888', '8681052238174996537', '8727191236820096007', '8640398731242908888', '6141326542774915543', '7468999213917494707', '5256018731914671118', '8774015829469820728', '5544139777769171883', '7556479397580447274', '7941264154548229936', '6280830969713561964', '5495914167242893404', '5140880779675892177', '9004369121461433220', '9133195122887704469', '6826051326281650515', '7556317306194842763', '4893360944895113869', '4846751736720163468', '9083115349329261010', '6339069678403301552', '9023913378146165401', '5588694845139771165', '7457440137635152811', '5382873575159685610', '8655817853123346711', '7535973967136005200', '5624453610900889580', '6203670134314176966', '7831427047945789564', '6159444442030555179', '8413015756161120382', '8481139120772682203']
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
            



