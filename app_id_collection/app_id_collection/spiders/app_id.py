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
tag=['7225419037366761778', '7884684637904001011', '7634437907063973615', '8114888203748187226', '5016918305791861269', '7343284885223654592', '7269915499496069884', '6569110533638036464', '8843539719384593374', '5454605613558431145', '5351259395079291892', '6880858771982695462', '9044904221386407565', '8695201372452786994', '5280097052491026413', '4725454891928019326', '5719373617281830668', '7494950923388983781', '8956853162329581394', '8439789399652354514', '6745162102186784723', '5429167019741031441', '4906872397175052868', '4879175666660195913', '8936174067130382554', '9127342944273942513', '5617098246323724912', '7820002186650737645', '6961108267036219781', '5724470991251012704', '5455341227926102985', '7200268128693839234', '6579634082620729026', '6655576812419778166', '7694676306905303919', '5280984369230066583', '6440323383219498837', '5589498204393340028', '7495131674787494593', '5583694883010438697', '5592103664205862569', '5266226966020985892', '8258372766334888066', '5104455609865370625', '7883692210457067105', '8381686851933341019', '7138966833964019182', '9016996286719724217', '7604541924565019039', '8667934823445931970', '8493757629514860414', '6047511356613110442', '6164496056853964495', '5411182694344329868', '8367584015930109517', '7458767851385119531', '5870342803356720074', '6852303298085025625', '7893179540932333425', '5928261775441355361', '7595551584955017087', '6295567347339808082', '7373346074773014663', '5139481848474131134', '6745296608235017834', '5794781744720991244', '8482319502856870467', '6879592731970760008', '7915608832562607433', '6872418927942834607', '6114645165194384223', '8940926481201736827']
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
            



