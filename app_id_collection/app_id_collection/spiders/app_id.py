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
tag=['5083817460526327644', '7539442544745743672', '5260680627634081217', '8046595135458049064', '6178950855874912675', '5451518358825576048', '8640556426190716779', '8502109499858232110', '6234335191064488918', '9164260508818093380', '6019366032821877619', '4708466050877156964', '4643781271961833278', '5958063768914173487', '6019038134983435271', '6079966670819435054', '6861988240512426856', '5272862504016520651', '7399715291966353116', '8034086245572005202', '8115236280116603470', '8906062187607487774', '5173143032436948630', '6018598330250843605', '6449565055202168255', '5808801354978445358', '5804036934581529783', '8983754853689848514', '4744296709538939559', '9029890354094727991', '6402557770174223788', '4919269069898699747', '5208115105799200519', '5191954708930348962', '6196866172884388523', '6906629452137252349', '8905223606155014113', '8293364459570715531', '7057959691151910430', '8496315002364483410', '5251530371678806790', '5976616910996789779', '8316470523921261984', '4785450851216998211', '8230212300039227114', '4612309125060036115', '5784793758652161969', '8614916404993333903', '6695138330063996139', '8067421150984452247', '4974977204022821334', '6372918774674573544', '4614678246860437532', '5676307538795422800', '6924435167672710117', '5630538819012062144', '4912272605488077040', '7576545669001813084', '7236897623184980796', '4761128644894919241']
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
            



