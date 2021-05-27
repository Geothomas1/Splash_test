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
tag=['7647933241016359542', '7267075389259261948', '8452772772129638222', '5037714950597896723', '6262812817404876837', '5246980549396346494', '9106758490523988773', '5278903897641945065', '8892764716159975659', '7898759309854541037', '7105200409895889828', '5414959987214434865', '5179765370063620113', '7202365030569592249', '5962088966115847613', '4864285760956847806', '5353916181353127800', '6970603645678425781', '5799461072556333927', '8720131614050867248', '8617440722285293223', '8679637095746408238', '7048834394702371491', '5783272441830311513', '4825320820838665630', '5237363801818615793', '6991741000796606469', '6655474495561072403', '7454240174933505685', '6706066913713106038', '7556601175049306180', '6422179013972642713', '5708691272840102536', '4814213920717703607', '8149889050225717786', '6998715931460417166', '6924494703517680501', '8763644842987277979', '6596113907192743727', '8581256388378980336', '5829718036967743658', '8929232438554100687', '8591752306381892167', '5590977968121198550', '5927569208595665249', '7806098187455465808', '5678488252362133472', '6012398973134605735', '4677953362929332120', '8752211643742452474', '8760295387755897783', '6740247568804415675', '9180560700750542955', '8449310898275657078', '8400987755330967875', '7512092198153492490', '7247922097304959115', '4727464007512189673', '7174538640657931673', '5566670332605072018', '5706722618658247457', '6857271707536754212', '4835355749321943317', '5547028207423682415', '7011172617740475255', '7866435846854047670', '8521165470504393412', '8599003009485541859', '7862413485745535783', '8183526573474774186', '6243101972887716167', '4817050550527711851', '6265120101873306180', '7225001653074713498', '6220218182673435524', '6610974596760999275']
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
            



