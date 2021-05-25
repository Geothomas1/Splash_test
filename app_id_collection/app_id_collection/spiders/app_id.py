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
tag=['4848788122945089526', '5310742854655271320', '7025519502488333876', '8982799235103865411', '7454502298634909546', '6957745135653735703', '8309146882578249641', '4893743113093089662', '8547576113257302063', '8899583960078983734', '8004586049009189904', '6368386690335483828', '8380557627951144015', '5908609300356018342', '7795478953882202256', '5329447380439161247', '5111496211534561091', '6982489146966632015', '7901097079588152202', '7566952504036800808', '5026919159031791420', '5670444702132009080', '6524083705137336957', '7934971460118152383', '8407138120600624617', '6743654905159978333', '5793312722032060751', '5888094142938776857', '7309478564074899011', '8942551490923126815', '7576641291950878920', '4668885814250098342', '6007079758762978222', '8292310196333409178', '7134680454111625298', '6353302165753628591', '7861054856589068635', '8584055574805329687', '7732667010712280570', '7932817826050175353', '8448179079033178875', '8451752379033790777', '7673696448598840803', '7660942597560993041', '4734457844217425802', '5480252975671094041', '6584671067229771508', '5311368636062249857']
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
            



