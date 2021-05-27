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
tag=['6632046057295121100', '5211419353860185811', '6819654565248869617', '6770439684300351402', '6996046977144317565', '5920036514190750919', '6248216266549777396', '8277905985312709252', '7957491063079800258', '5728705364850267409', '8991979831681376339', '5248659264590867199', '7819452549986659054', '8660724501636054837', '4745571797399582003', '4891922000589235260', '5662817079237437564', '8341214155208153442', '9047471407494935429', '6750106454780197167', '8985504773112840595', '5710907499575355982', '6846956077520704483', '8880660591673247437', '8241896846132456431', '8257071117460165535', '4940155859285710272', '6658377582224809289', '4691440346476525220', '5225971226587463463', '9135614843063660425', '4866103282115197311', '9196764815382298234', '4742095072404850869', '6178743093915147879', '8784463096143376556', '7622646465021850003', '8489742716968530809', '6546124504537060798', '8096795766095911280', '7733799211532857905', '8850556472980561385', '6370239917262997433', '4798609469445000566', '5897860699031736718', '7587795560439620073', '6356826102828277953', '8236807858217839547', '8131694007614789578', '8681483838991403748', '6319326918832682148', '7097861795919254743', '4722697971071741237', '8952833688383707595', '6195698050539911097', '4998705711869411552', '5555489635025374283', '9155906865521818549', '4639350513970225632', '6892686590053991051', '6102885782491781397', '8224734524221497701', '5121262848534432588', '6016784737908398954', '8766215303839513186', '4616900955212418104', '7212266901048795302', '5575975975545021341']
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
            



