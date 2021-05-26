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
tag=['8933876543153055702', '7287057491391877710', '7928923945749966383', '7369169300102473469', '7936463426868051966', '5092372498980139127', '5250276179114623793', '8462683294973106019', '6973432660660398098', '6557911518949455948', '5023211659051067491', '5394893682435787418', '6752907968553896816', '8272220787821467566', '5155759136217161968', '8008961841447834345', '7566601175066898808', '5329222603443671860', '4820249098559241780', '8291381792420192187', '5167098818597160617', '5960885667345690533', '6882913406687595746', '7908612043055486674', '8289744277193635298', '8281740682985913574', '7735701715137379081', '9041057608544026119', '8182188746158323119', '5140204566472103991', '7966312506103117882', '7333375258423207891', '6165783655900087551', '8084789760165380241', '6110766059913070732', '5526066393909219647', '7926823302511859695', '9178707967336431156', '5004636489086373105', '5734958661173971483', '5043912995786959945', '9150085788113596678', '5030574576905203036', '8042716894371698213', '4634888840388092687', '9189573112783922775', '7396055048147995507', '5590551881872769793', '9162339319409494203', '6381055606312263384', '6643515005894494046', '7698096783256039256', '6930955969394399742', '6290766888925001422', '7896469254354429136', '8289385629146726672', '6848702369494171268', '8895257314178727306', '7205662904778350064', '5504954132540911611']
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
            



