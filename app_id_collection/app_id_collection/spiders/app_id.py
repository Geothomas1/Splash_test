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
tag=['4809332998367781515', '8610055146128716375', '6206392190301047087', '9153546688561724173', '7249250314836689793', '9022466783235517343', '5708798125950966006', '4853702680251325334', '7585333044950038155', '5974722340689441054', '7411837711429382379', '7045023834831951826', '7119933206273097648', '7045437409790753416', '5880629538785838402', '6282313367926642118', '8894823691230117917', '6246923847134136459', '8668128522827756716', '5828772007087954060', '8461837994014123612', '7892052850981050382', '5494882433544295620', '5972872470304070383', '6672344729325082727', '8765665266908108998', '7432164035056961992', '6196668964294455460', '6134637110250579588', '6641637417851010495', '9044124628495401462', '6135815754208595340', '5036945620260665529', '7588003072968191620', '7086249962478235848', '6152590903454938756', '4695777432343435217', '5146813126204719875', '8957900973328422380', '6688289229213099422', '8048024827897496435', '7857028173018734263', '7164232162970374748', '8554843920643292032', '8641257078165304051', '5984322445579089237', '6958483978829302909', '5313487036460776195', '8186519598778982782', '8661750016285974849', '8163872853062921042', '7080822091340638924', '4880626716894469522', '8613507281989566416', '5265722540836733147', '8708885014882703865', '6593416087942044587', '7744022545317079622', '5430543946607764534', '7745658091341932571']
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
            



