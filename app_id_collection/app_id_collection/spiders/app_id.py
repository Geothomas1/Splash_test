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
tag=['9062373634757535704', '8965518120413294072', '6092816945030180871', '5471290003183242567', '5994370072246354421', '7561059162720889689', '6626759196141533670', '8062596982371202616', '6420145279007142413', '7402205310806914743', '9139624331946177494', '5712016488736409992', '5834183806485251593', '8059671941697619614', '5028009183835971054', '7765296441514615057', '4969959464485167865', '7434497599961026942', '7825356281923662273', '5185356276685331700', '7537054356995809071', '5954486049666324780', '8329378891524819854', '7874931121514501344', '7723403455955044226', '5394641308774431003', '8436953532788264581', '5927299089830578754', '7355636074771034380', '5713307978272069189', '6522249070263097981', '7866557077467988202', '8256621082589296199', '5476140356962722989', '5677246410246307336', '5670112241176159317', '8677357260198958526', '6520130637621273347', '6428531868400881874', '6838038566629563073', '4789709621696725034', '7362764666064620065', '6410060562294360136', '5569003723018944144', '5520453745371923361', '5064460190768781910', '8478995642436907344', '6159733194410382324', '8593700934225477275', '5515928204473260056', '8463082059817782937', '7004042506516766832']
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
            



