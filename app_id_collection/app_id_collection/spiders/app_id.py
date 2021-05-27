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
tag=['7777402198283236731', '5971399807258825010', '5954341097239808974', '4630864123770839911', '8681089820555593239', '6262960890261939530', '7055567654109499514', '6653766346898794169', '5409612149817057028', '8227631573660876901', '6345388926804016214', '8371064280619966303', '5068863252527417098', '7671857013548981751', '6602063949861568568', '6608164810721237575', '5948974150151949385', '8474578281569929851', '6054645751495315842', '9132883783886906085', '5867952456574122249', '4782992479783245046', '6500208815054444953', '6776983213289151784', '5548219192328832174', '4835085925866596692', '7041859146399104166', '4736674062444797200', '9163167255623644364', '4697196672398397703', '8422370556555226723', '8457670048876829719', '8542541137869474891', '8333088624071765694', '8070500408800255726', '6331531775276453687', '4973975728455915311', '6676511199195761525', '5841334671038334689', '5702094759543650654', '7571401175169207045', '5509480022962405954', '5629287850550236444', '4649747150186918938', '6568024438841421916', '6224462492245691921', '9114847813396283588', '5921705092973127988', '5229459876242435014', '7222207789210153017', '6112360496273749853', '7532501416060060421', '5167395978533688986', '6488850794767397110', '5717091588944600266', '6662505133767612712', '6784302558730390487', '7694536340513612597', '5409164286032980019', '6382407436948056408', '7777081099054348719', '5377125201209877116', '6085250500236717307', '8718611887807763139', '5143117114644907759', '4992656828035938217', '8919949703917158130', '7991188866550939369']
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
            



