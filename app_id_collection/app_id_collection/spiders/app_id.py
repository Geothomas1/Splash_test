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
tag=['6676001340275284961', '5757038794568794023', '7021205023465684710', '6487689772561878828', '6503764014870293044', '8184993319291905595', '8119263162444142789', '6123493724770640455', '5002428323152594803', '4636466165295097739', '8778413552898986115', '6629093694365479787', '4781996526852406074', '7743523398974345834', '6672921781032716848', '6091570391059194180', '5539363955453887430', '5626971605932107672', '5169510668335069233', '7765200844885855767', '8181764314216450686', '7260294656034663302', '7029051445673606009', '9160497529131421678', '9032372473657853216', '4654753383520250991', '9035520425490104161', '6985827489623568348', '8574863128204794100', '9194944734855926750', '5225686539177475766', '8233558019727996517', '6645343366751741850', '8931183995393865664', '6708329222716326347', '8912539727452863409', '7268133896443468185', '7101198350604198151', '8730638310686371922', '8936675775786016807', '5713672414955811747', '8015457502327162344', '4982052723439694366', '8187576823516042721', '6565193366731079728', '8479267655076247830', '7438382921539624603', '7269320099127076493', '5862968951379291051', '6586909731543699461', '7755925740455363409', '5234477750779571185', '8397733516227038173', '8082331994159443706', '9089226060913774153', '7253118641640283145', '8804038102642891757', '7127995917101210292', '7756206816373556031', '5541571172507099096', '4619257993392020708', '4861596213586493602', '5586991216286353544', '5059501922506870829']
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
            



