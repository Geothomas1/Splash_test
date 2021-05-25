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
tag=['6589330114077866598', '6404048689499437348', '7356612201194638709', '8743270357816422914', '9097185005134886243', '9046213330860348168', '5843561545363681755', '5138138287939442282', '6757571688351793338', '6043653125834539377', '9056550580313191506', '4857484411335878422', '7765579257322188475', '6330568615215698969', '8515565779373476058', '9191322092562914854', '6893444052027149569', '7120475932404018999', '8928454834131413443', '9118255108510394264', '4976810630224147634', '6047857537672558362', '8732144781506234231', '8564642020189934355', '6799096435514686842', '6811892225506797446', '8207510022289388043', '6970882501038702174', '4898984495339363497', '5038390922181378911', '5754818789549425530', '8924361998776276182', '4756446509547816042', '6174537357799251457', '5882795394967225969', '5699737157188509318', '8870645852774521278', '7787336080129871986', '8003151776251143029', '7222758388224646697', '8025485344059282267', '8466242297860822673', '5564280905307453336', '4856542238913104134', '5967659971461769688', '7102806663778142225', '7436991333930211719', '7422095102799956143', '6826593763481321730', '7830845280092528776', '6781665837662189368', '6583394277454644725', '5831429129243669592', '6010915426727576403', '4790070667931982806', '8276782186753319777', '7566304266577611559', '8299934534671342055', '7596564142859272811', '5665813558106562136']
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
            



