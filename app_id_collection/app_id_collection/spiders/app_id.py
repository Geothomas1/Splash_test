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
tag=['5136543320753118674', '8642255748025584273', '8803649875453688809', '6172927760485730448', '4726753958050205533', '8945844126005651843', '5175773111161706925', '5411197856396249326', '9179252062030750928', '8818713594159624159', '7679901833019830117', '4899482611442623062', '6475592716711595123', '7353531618167861904', '8878226773705616200', '5810481673801929430', '6178897722035297930', '7248962679677644679', '5184757019930588185', '8635532423115474166', '6677587029913822659', '8406847222930440767', '5979378273899273025', '5439095407074530054', '8052968968169081947', '4725112966377296748', '5348200011046889120', '7814173953436358554', '6305460409854300324', '8419052485035179336', '4908564362879243734', '8237430299917465563', '9185323314694461649', '5723502633915819194', '6083226804231060524', '9048730481312549573', '8809528584139955129', '6505101184499011021', '4863280409170893318', '6830778606524529739', '5118979098837587733', '8626215351142204812', '7157716937512121378', '4813878430564579954', '5130448887408336541', '5841338539930209563', '6214507680680154683', '5723292543470816278', '7437982941245696477', '8674790179345561515', '6323083665621589806', '8152824449857593821', '9141689316320317188', '6698899737769238815', '5886168880552753787', '8775564277361931397', '8121640583957355843', '7674000106511436633', '8563454086476274853', '5766398946986983808', '8033888071580986516', '7795423201551339648', '7853993420021879635', '7238119791064829927', '4974289929229591404', '4946664282663235578', '6673954147869746539', '8442910174173427613']
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
            



