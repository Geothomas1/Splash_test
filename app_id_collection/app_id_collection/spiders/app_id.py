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
tag=['6230452689219414644', '8410965062343603376', '6153095365130042438', '8024654137748364415', '5421036283029867644', '5533528640221637781', '8432995497152947670', '8881746643180042782', '7850462096578336079', '8352600844228909430', '6067941781681432904', '5561908405851195225', '7548219238917941668', '6483565246107489837', '4793671465538858145', '8431905303119695928', '5813049801375420561', '8658555040771226222', '5778105783414976049', '8953622501046432104', '6542649838792314024', '4967264300398202718', '8620430069923752561', '4869540774329411947', '7530190825724564991', '8847270264295949895', '9035636806488067205', '7231527673713299321', '5737026471441797456', '6772509527661822372', '6425415236589133252', '6239805041523041263', '8913557785295944266', '7022511786056107717', '5947810954774576260', '5220942376510577902', '8278161924171508767', '8192050375078017556', '7010253229058953232', '7021070831835086877', '4830599608293698753', '7822472834202281934', '7027223966103799926', '7277893397047121395', '8590234069681065760', '4988799813197077501', '6043415906904226650', '8494931934218050816', '6476868446789226846', '8379566161670521753', '7536475409115368541', '6140182447425879795', '7909598766771724670', '8560239449675742601', '7969876082861924609', '8453527432193404134', '8605109639613934504', '5777794196455685308', '5527446017321602937', '7275960624719716062']
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
            



