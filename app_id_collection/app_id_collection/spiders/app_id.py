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
tag=['5160899586903813846', '8569397767267766679', '8313900728629751734', '7121423040440098994', '8712235444717060923', '5314510570557841723', '5130478763673922847', '6402872462943328965', '8803953251907703442', '7125905948370822404', '8854514398812106624', '4912641259576208799', '6926567800493090979', '4785607293066661405', '5423817450217822942', '7480345927448694220', '4991183460036792864', '5719330088225658220', '4682133209309451286', '5414467887696876060', '5924276755067077485', '5881955048424652239', '5754770980343355905', '7696481491336789705', '4809315800513846039', '9070567566630920410', '4692939627370696571', '4768956459475971575', '7745335211880646610', '5772978568043722476', '5580023962412385785', '8009883480758736776', '8395808788683680868', '5813231041486850002', '6749878482763291640', '5908431321195575511', '5059705100845463179', '6083144898669077445', '6481128671102190879', '8989890462332273741', '6986232799308915603', '8694790994047827555', '8763341110127370172', '7645363529897380070', '5163804290318597579', '9140904282676701590', '7086536426626576352', '6520474897235504859', '6074199782938699624', '5495864475226449957', '8636646689144896528', '8839625562176880506', '8725577069456832832', '4882730928718676421', '6776730634580452069', '7876793123497362906', '7420003048839261828', '4727096749923549653', '7196506958380246144', '6151875896199354545', '4789580448935973346', '7756774364328601565', '8564261004541103416', '5495904443791099577']
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
            



