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
tag=['6665437308511209117', '6809109784060370658', '7389782970976802822', '5645706041873155457', '8271287927671368256', '5194581199033109142', '8915169143422561625', '6976318052361578107', '6189401587933183852', '6810769518504152980', '6277956700908348398', '7025388007828200575', '7368988254706245557', '8196086933510381552', '8635681670702514962', '7608143481226674529', '7865470206882283925', '7166843452361034237', '8727443074244309938', '9168631552110730118', '7458747896390318519', '6176309463181884402', '5295002497598445111', '7786462691999255230', '6747941147379481287', '5871470615150672879', '6766774226102287868', '7292326358667125256', '8454145829299001834', '7472817515927741875', '5969814034965445224', '6499658613323608433', '8766416179170060096', '6906442166653679063', '5837919682648806204', '6640495756547439787', '7117445492023250763', '8108739239237418559', '5300483087872269403', '5082124330936703177', '4922869612836698448', '5615419703628842500', '4952413072724821519', '5817124511140113980', '8873176051008372808', '4682932724915294631', '6399517168361664751', '4746331013781094236', '7550572979310204381', '6814879947646523419', '4728843905962363624', '4694038870815726797', '7435053323051255724', '7364936052853047621', '8777948289678918747', '6323677105409942417', '7274979146896532847', '7583994809266935914', '8425488737663622816', '4718066791287942502']
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
            



