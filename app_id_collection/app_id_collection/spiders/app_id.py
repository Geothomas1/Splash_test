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
tag=['5996711245499992497', '8918374116967463371', '5866914318181942783', '7791671420540665835', '8155782941676464587', '5864539238246533483', '8387870093971699850', '6664340540826989862', '7410968480957919859', '7369480950802087837', '8367275780225923841', '4904364455782296418', '9030152718371580429', '7397562155355331493', '9146675773925868642', '6354966239220109675', '6715068722362591614', '7105570778309057093', '4771189779292462122', '4956473889226630159', '4802470587402701357', '7132661048838194005', '6749200927371422588', '6594218762273717791', '5813590554155311893', '6766307165505483198', '7701369843255288775', '4888229681964971463', '7818340835884209915', '5572194350430429482', '7928368666903738813', '6463577576624575366', '4747420335489067284', '6854696854726300374', '8443232511621177982', '6747148087067225034', '5192948484400722837', '6444927099218755529', '8033139318322835951', '8687429887343007478', '6331453960572772433', '7369752099829866637', '8958743870138324955', '9138215253764912810', '6687860767257210158', '8828719902965931407', '5906639845894002990', '6404162505989379870', '5797532665488948348', '8008183637485425549', '6122967924302926726', '7012256112823938651', '7741067125244845113', '7811401516228517069', '8345575079974663402', '4973348737834747034']
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
            



