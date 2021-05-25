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
tag=['8341295587556280210', '5429249212031858727', '6633314147344022637', '8584971442385397136', '5048532150596012283', '8610349311358980200', '5682943721509667016', '7074140651804190975', '8774006878916418441', '6980574128975500079', '8608138020966237848', '8883108023081147418', '8072920757501581410', '7570702376328862724', '8367993383594198385', '7078460479379942235', '7513339257056000006', '5175034726026785550', '5301769715417111462', '7242995029088679351', '4772512400666501557', '8067839265176034878', '6771860378678046210', '8579599424503757896', '6686424413374698640', '7644387093276857560', '9075094497846624546', '8627516346577475999', '7912775645587970218', '5034689648241182754', '8081844526865475753', '9065957855812469611', '4854175791087078210', '5371059930985624698', '9031411564082327996', '8735975024322090044', '5135458044423779524', '7190762125889760695', '7398489966853368517', '7836792589762695832', '4711073422203599095', '4807306331782880036', '5100936197614422396', '5431706989284553803', '6285823837284469509', '6983644334134553049', '5650438527501624970', '4805513035096771686', '7934639158061846812', '8657580071141824844', '7059051889280635539', '6300946638858166807', '6711226057014817788', '6334810424099396744', '6883674820441526627', '9157380475696850528', '6106180824546957503', '7263567703412225966', '6239163454935587997', '6760281395581839421', '8404037525842458149', '7782813224586092450', '4729032526933537472', '4792419793423552505', '8557110081719892084', '5618261276071487160', '4803243400814519754', '7422410734200700826', '5232907847451610937', '9047556097149013853', '8024664609873365929', '5479904976228897610']
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
            



