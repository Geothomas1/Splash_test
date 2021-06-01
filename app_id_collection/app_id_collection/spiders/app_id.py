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
tag=['5581123954802239973', '6454239250908028798', '8390883489843643746', '6110886248504779819', '6942356768596380471', '8927078006916428513', '7923419280829934943', '4854990210404955584', '7509563337312687590', '8001922622813874659', '8560054796348178110', '7079537491170087965', '6575354698744209287', '8415708595503528522', '6353843542946015676', '7575921519859086784', '8835118355770995615', '7191921550189199597', '5443809227281343658', '6666801903382161982', '5272998733429278022', '5403449337079485419', '6149918173670468862', '5006301820184753017', '7523777595463896499', '7478495953304463308', '5350134666311877976', '8179638299679516614', '6427239506375932830', '4898190233386028474', '5369474680976506286', '8130421470774089983', '7701500134199730047', '5549291903961765018', '5665362874752137173', '8539947740957576135', '6209495530990718947', '6652866398455535880', '8183337911828341539', '4786050607730637299', '7474232975580171082', '8515034776846192019', '6823023052882270314', '8836670817379982659', '6381404990441632810', '5583089490042179688', '6129943045598653085', '8967680729040915516', '8549256716646729186', '4774975625707375824', '6294965298556577538', '7573678680915185110', '8172284292357445206', '6714612978680227564', '7758630132642385828', '7970389410111620099', '9045330119341729219', '5244689462231907609', '4846500362273904404', '7428044021911246429', '6682071853969993951', '9071875813726262153', '6395833415561861358', '8623343979151273088', '6792065108395523696', '4842587579536447227', '7636294942299745292', '7388356460048429060', '4814033096857630459', '5616873365343319540', '5083167886823142913', '6619242609433194247', '5526270419436598194', '8350123846675560286', '4878877633826139200', '8938798766651218772']
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
            



