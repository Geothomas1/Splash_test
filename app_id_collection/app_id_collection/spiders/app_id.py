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
tag=['6994237474336929510', '6419352554480006664', '4864037690553719578', '6804702081411529158', '5931792201700083878', '6594978785031145359', '9116350352558563044', '8259467583332772770', '4800205900516778603', '6110508102937518693', '7800090769896328227', '6633461731213662329', '8005709018943412483', '7528594653673606487', '7656238375150472140', '5233585477558273402', '4894750979625045388', '4898265788680179569', '8068472682277748287', '4695814668791488298', '8151714364706180316', '8340958837118547534', '5742045330455424642', '7374009547575980156', '5598470257480868046', '7595706856829253413', '7177071910722457262', '8279381984980231905', '5279914916490008578', '6413863438581819642', '9195168978619841710', '7431236028349741429', '6803987321728563101', '8374519851156423153', '8851957014768181113', '8896307884223972047', '5747179795292428520', '8301949780902772042', '5576800478161388561', '6616796235966760502', '7305504417775326558', '7707290664643393875', '8131489338446059357', '8626478290048214467', '5314540873889556590', '7630417586978766880', '4896417924738532354', '7326408935158367257', '7944893141468785505', '8411462421671077389', '7657119288011883339', '6642088067087023953', '4668226700677188770', '5157030401489319087', '6992756981286957006', '4696883960110913449', '5857916457436312218', '4688342648896878197', '7364486778066000988', '8060070379647575393', '8012608662340237747', '7671784676165865073', '8751979198937049408', '5332047421112476196', '8501791997005980105', '4748536211035721851', '8761853422447815428', '6688144865368856539']
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
            



