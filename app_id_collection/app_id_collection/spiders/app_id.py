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
tag=['8720904865463981276', '5111840943846744466', '5050647488420595889', '5496590613422638755', '8050017013069437269', '8685213464217636069', '8183457595522860519', '6985460711165907506', '6192113803501437085', '6941021797033448900', '7742763642754591279', '6243161491331191597', '9223028892386982079', '8959852829533420940', '7303606655835923526', '4911991338593126150', '8433569994962413599', '8879677595090094152', '8157461318054974992', '7627571908184472902', '5492388613392482470', '5322295841940053917', '6828211798475415210', '5984316752584468095', '7346668002361835178', '6247417860140381848', '8895734616362643252', '4935310397646909332', '9114966298881542436', '8602211479360775467', '6707589514981494067', '5845021936776608603', '4931745640662708567', '5891027934210113676', '6951092596279229845', '8497722228804103399', '5013636650808627276', '5079417428533993217', '6033687419806778822', '6969439763102826458', '7051940528999412452', '5985737877564925969', '6218992826757134114', '8241474957846508671', '6720828033742161213', '8948338079563288900', '6065384627601645849', '8053728788464134315', '8065244108610663587', '5679232687904840001', '4799398490328320213', '7885794227717189814', '7409658540099164499', '5928134983584727569', '8842759076731573120', '7602649451911351733', '8232174611457920989', '8999339140632122257', '5514531107087552615', '4642420255483098659']
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
            



