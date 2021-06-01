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
tag=['5478848546050618594', '5424816756001973587', '8628139898926391023', '5148235322230368238', '4696999074000426000', '6834942355000828100', '7299866698750655019', '6434603791224482587', '8765836789409161783', '6098516636597594776', '6656266239810434822', '8152028759863943869', '6949430064785271236', '6456050132775261714', '7626303159442899851', '5774807047557033827', '5730918679844616741', '7783539868370147718', '8478300364534746376', '5377782980726438438', '8604623606282566860', '8904010338278258521', '5103066524699828013', '8926905336476044195', '8481308371198332762', '7403893496706961616', '4963682476192268446', '8775114594676386386', '5796538161659195789', '7759432144158600346', '8633392803594861007', '6261427570641701215', '6476271577105642194', '6996564944794590025', '5243664948663447823', '6843303190714970415', '7526999182461061594', '6468137633659651194', '5514122451786066239', '6122700077579659586', '6288930881600518628', '8086354234846923433', '8034234126700042645', '8639253070042174832', '6343164177178863473', '8675761046824387020', '4866101755486121646', '7317304513879515233', '8790730601916417312', '9007265204598304843', '5952395425393771763', '7048009844342549732', '7440266104613132046', '9167872875946171113', '5618284459432644239', '5774290205688542431', '6058063936937449020', '8450184289796383711', '7983601876281727827', '7114847176092885640']
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
            



