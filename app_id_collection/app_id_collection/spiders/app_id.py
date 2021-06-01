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
tag=['9031818776731570394', '7279798556243435118', '7355938799209808790', '5693787314794297657', '8192712707134146511', '8887039993821722444', '7599813311176635287', '8893347394193280171', '7229474961557246639', '5925205885115483939', '7966166336125166705', '7851077870484784525', '6107558838103995382', '7987620169998956304', '5187416160727254581', '6135568755288118409', '7464504255455326526', '4814624746720599325', '5026814708419718864', '8348750230111677624', '6527933805842537035', '6599776094612282168', '9222121280773083885', '5850463355256758902', '5984876879869631385', '6153734189135645507', '6598238191311236124', '7862706639021254039', '5245190277294621651', '5699017451728970123', '5621850966228775981', '5315286474575140277', '6384823163024182600', '7037665162210857539', '5440175822841957834', '8305913367930580475', '5854561130889809043', '4630520211757392173', '6541740827497430434', '6083391190092943470', '5703835969201943816', '5497953301162057133', '7857127388664943474', '5841267965126905464', '8412834193356581377', '7862493275364145460', '8934686442416260897', '7813967376335229543', '6227883177574280797', '5003984487771665928', '7762375795298619893', '6130090833820693780', '5055030444861002786', '7101417854893095072', '8676377228622027694', '6589145060805623352', '6731838628059519714', '7338777534892840680', '4937113741744054953', '8989888194448264402', '5972291026034749261', '5381276037560686861', '6917324362954126124', '4943930652416016456', '7256149331275863709', '4842574201088884578', '7919057907840027940', '8741657096153826306', '7408965178443301303', '4768443947319948692', '9080621198874405413', '5580929868548133440']
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
            



