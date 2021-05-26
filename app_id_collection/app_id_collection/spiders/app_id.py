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
tag=['6055834150996312762', '8520190996145370040', '6899729667074181043', '8301578764933357949', '7296344104667138670', '6423307609329866848', '9146100801558351846', '4702890658323381984', '8199498574946364198', '8462557310381783729', '8642239135335264543', '6127100628629829578', '6081899297501175958', '5438432791382354326', '8229082999121728179', '8611258155162133176', '8404108509721939982', '6976489122257532702', '6331086452582662979', '5035614472476293451', '8341510148224489301', '7792879274737162740', '6073004400609392754', '6294031800284486408', '6038617429041517796', '7605423564950521997', '7121984622232438563', '9131153075004573282', '5385525233327299396', '9174421742817889039', '6897525845881145008', '5978015920867749574', '6708665649091778988', '6575108708636476478', '4979645110975956242', '8843202559323705234', '6362297435335536825', '8813666941700343524', '8382092672084885997', '7205752839668676203', '5023356162834605042', '7031698641195333452', '6064542819837033805', '5620255585947003863', '4674808498842518333', '8242698836364203435', '8379820834585857822', '8800918020304263386', '7169398121028170181', '8455142586831247434', '8620485517523509831', '4735003269789181987', '7092459852810933933', '5497425597957398195', '9056997983142311534', '6152103796630212104', '5092374325783016319', '6030032217251185213', '8007567194446650968', '5270419756542383958']
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
            



