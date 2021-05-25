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
tag=['9047955209232337754', '6572061599624528195', '5588870628169652656', '7285971080838653664', '5262965758920067639', '9159627101207394472', '6923881983932747154', '4664135371915970519', '8126850924539441584', '5047556030621742681', '6235980914865408642', '5227289336744315478', '7890815263026316158', '8306746265574850984', '8234984404232555089', '7174351842942600674', '6017450279639602481', '7113793892978047717', '5252755467802352350', '4961435193446764316', '8885446239748236816', '8236174922785878158', '5820359406133218754', '7782567441705616427', '5937310765377092640', '6624686630989508199', '8671438376186117264', '7915422969144627026', '6367742281199325365', '5889733127608327964', '5818161256315799802', '4888355033324625739', '4695483193568185840', '9041173938750138664', '4963023349025449518', '7740231638494650750', '5599788780811258072', '5667641639682181100', '8414933519395863296', '8179630876663812461', '8379529676062547238', '8209511922826548264', '4628073667365740196', '4615586749318634758', '7338691998508963776', '7943216214497720570', '6619739843995118777', '4753128145277262392', '4630408895556693233', '5518921386883974425', '7445660872318648439', '8048141916608733596', '4616666496320324735', '6962628713989675863', '5711197770637011525', '7745018371282386614']
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
            



