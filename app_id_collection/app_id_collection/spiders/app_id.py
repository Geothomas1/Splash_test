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
tag=['6351556080768282049', '8349537386007934963', '7892913269075721495', '8648233457299793814', '7596303408537342978', '8607588335742983102', '7058403369393424140', '5414042990480295322', '5382307214726356149', '9011167706118796529', '8498677424567158784', '6749335729462274356', '6292220268872263051', '5907959700633013093', '6943435756825055171', '7837293298332745600', '7778424881749508148', '5773773301592341983', '4937770363404832295', '5895154481057786925', '5305026108244091967', '7968111907099928679', '7590122007901836561', '4743899525130538648', '4620106522741541245', '5505192057614621869', '9138878327109540079', '8114105855888506023', '6925866022909389177', '4720232341395859466', '4640416121259590545', '5632955594478089878', '8526482327141844924', '9040442305630224740', '4809175298020157199', '8613651141413645662', '5083050651445629904', '5779761635682790559', '5559148754152872963', '8668701477622914032', '6366271130969631091', '5455415969745901109', '6481577571535301345', '6355416089864166823', '7891240193247683246', '8976382606253195480', '6875401605969588379', '4700119306053276107', '6833104566008953893', '5311443402104399925', '6290904209461302610', '9181202348949223715', '4859185133130683012', '9195601732079626431', '7239934063023390171', '5891257649112739684', '6800756349887572109', '7336110971143070464', '9008288684686026414', '5306959159021237210', '7472856873836800989', '7855395559351189819', '8193579874696401279', '8077907506297039591', '7738048749662331558', '5172229181413918638', '6364851808230428105', '7605759772428498531', '8668726573424113752', '7474859060217576035', '8694514459334845507', '7423035326597352255']
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
            



