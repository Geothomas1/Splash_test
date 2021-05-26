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
tag=['5541408749121004686', '8432157725497553701', '5798623958297631734', '7908431801524300941', '5269251905645980530', '4774331296239827307', '5222869476696581213', '6685656690806346266', '5370344435636132089', '8408240927550362464', '6478769956628253913', '7120512960763679073', '7843009654320039163', '7944975122583161380', '8149393519195549544', '7099315530962804808', '7862726562648624969', '7962667046172326057', '5879617215489267207', '7163280802255245032', '8595262593771710399', '8584562305729909359', '8525108820727342538', '6841558070776444832', '7770359143639175199', '5249087823932112257', '8585699418229079024', '6556347722805488892', '8345332849287848037', '4900475936207030072', '7911476584013507569', '9060663578856029147', '6895668496978228217', '7757586599616413660', '8095515514056601763', '5487492503835248382', '7373381738832505833', '6834442563003107797', '5039055208815503491', '5216133026286948817', '7000458207758838171', '8200120026911638254', '6551806741984633621', '5950912838732563648', '8286710146041099725', '6093410505172567583', '6136326425741529614', '8752440893561220899', '5347773459128669375', '6200073630985144240', '6199321273553184138', '5425334734019988740', '7703167870114868831', '5869957277875533641', '5009723044885288313', '8885119244706604464', '8141296672016298262', '5999654760713782756', '7153806710901679728', '9113272601344012936', '7440865130139396516', '8779102866253923834', '5945644715359337352', '8846341901325704117', '8125761719131714051', '7901549371050441944', '7664608331829742488', '7279554868336139412', '8946578534449324398', '8011472442411361820', '7134567784503443979', '6810998305006272415', '7932405986399423904', '8889745005367442348', '6568180708423268112', '4750851297012217168']
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
            



