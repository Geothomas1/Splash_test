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
tag=['7201660696623004525', '5420729891182074658', '8125327046135199055', '8685152379759484582', '5973402057352547106', '4988311280735374056', '7087451883225614829', '8232658028539982277', '8642126033812823304', '6068445124664238197', '8273710759165175723', '6441983418105616174', '8759152412137162030', '7877315826222014074', '8376670369255715306', '8043830287709235004', '8202617452388387612', '4961407402197403505', '4668793745925374037', '5701985920258259346', '7319427131484386862', '5438254612453204461', '8999623216096411687', '6457893425161276771', '5255879314806517257', '5055582843758085169', '8647987598434191843', '5128611299511667874', '7288002088305429966', '7677952856235332599', '8498586111923707193', '4937420385928605522', '6984581116187367945', '5664192367988579904', '4836671229228077715', '6723255498672026396', '5521546670680093719', '5479949147492777943', '7720725618142186320', '7760666026279023442', '7752608683054605616', '8129726961064484740', '6403305529828884331', '5240899325755691567', '8364861500166644162', '8097407929876428583', '7464551856023826606', '5459040253315324944', '6321034080882760084', '7675116541605063982', '7675825757023602395', '6416153175460279051', '5675411739335841674', '5790676279664405139', '8354052498834348215', '7605808167026993014']
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
            



