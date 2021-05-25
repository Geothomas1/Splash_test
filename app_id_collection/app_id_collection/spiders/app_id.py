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
tag=['4640401199548744772', '5020092286245870451', '4618299317894944523', '8071851612280915015', '7828735334976575534', '8449320986506255032', '7198890484602639021', '6307489286608030184', '7558919219691849721', '7959522972443383118', '7253438881335133058', '4856516214612723835', '9206950613010387631', '9193429956760353061', '4714558552966780687', '8132383357994499261', '6088094547063262755', '5323278912033706908', '5705900526093677963', '7257634960166805659', '8187687771506178697', '7366348063862915140', '5006432901103817063', '7522328388587088193', '6610594209914417287', '8748142514407006043', '5061395391976404409', '6724745810438085366', '8679407518644667948', '6520469912296734314', '8793265363803124581', '8337653092294893138', '8159804866767022045', '5963962050850113808', '8961380020761803090', '7666119599081250383', '8084103358193572717', '4684894861933048299', '6412429928707538217', '7823350489606562895', '5922441238220413835', '6362652511910138366', '8014114209733198016', '5445301590224115188', '5886045250381103493', '7842967378393202403', '7720396540331346600', '9003234386754843067', '5980476022275230542', '5266927340586114854', '8048063765192621320', '8516492132878022976', '7920435114857967276', '6497144426355796305', '6354038548244347849', '5591582057039488902', '7086625162070475911', '5982154398978833775', '5540290489194101262', '8519489247064820573', '7403387473101614243', '6665667980632641858', '7640858962257368102', '8146335055757625306']
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
            



