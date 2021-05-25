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
tag=['7305210486871450980', '4805884985608989499', '6256957238399457401', '6748875426166368349', '8039368935911664106', '5316610743259106143', '6321876234276229665', '6984990503561426151', '9059341596773093752', '7683901994572836753', '5490486164378705417', '6743292178541453844', '7549363007021201792', '7456293756408686489', '6070907700106943165', '4702794943380501526', '5382527952680233471', '4693936234162619490', '7381197804903525049', '6053150983036564591', '7636427315709631344', '6206780273587548214', '4759829941193986085', '6832245288161131025', '9097565841874543878', '8977755906639913397', '7736344181372479493', '8553631389525754264', '6543290517860473133', '6767791598301934903', '4894409108106773285', '4651793770153150180', '5674140384910417997', '7332029809197431597', '6768242171313189210', '6893988486004345914', '4685636909317788836', '5922835840816105067', '9109389198204070282', '6840092866082107151']
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
            



