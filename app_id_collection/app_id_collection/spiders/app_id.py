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
tag=['5681309260802660607', '8169992394970364814', '6440640153129088567', '7248861673690346499', '5018861183462079107', '8647948650156862687', '7034504012442081262', '9179986977006721720', '6021733211868093062', '5613883772935301869', '9118645386850642216', '6259296036517709904', '6690084240022947117', '5593742411081325203', '7416121312052657724', '5079879671770467624', '5459821658392629674', '5775126601326764051', '5845435445921421526', '6457984355316309163', '7339060940571055726', '4663825856658809405', '8665898397344814536', '7019463006329470284', '8582883487351489169', '6433186696134669046', '6366475870255836323', '6923849131495999487', '6303539455662711029', '8553604063140530513', '5526536669105149839', '6969046288940707915', '5802605632459861431', '5102417434663962205', '4928371885887997015', '9162449851721187410', '5286206192427159956', '6461586478901817196', '7039436990877971174', '5977932993528614692', '7252937353610279252', '4643081912363742693', '4878288473199138535', '8514767996446036537', '8872586535781183034', '8984289006386788277', '8117858972293004390', '4960074997999815302', '8032984696228729680', '5528527430495600696', '7818153565931608221', '6742916321229950495', '5396284765156554281', '5556692352192188475', '7906431379753405755', '6616730544515493089', '9132140172328504264', '8959949386239199587', '7707061455892040680', '7538952452461717375']
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
            



