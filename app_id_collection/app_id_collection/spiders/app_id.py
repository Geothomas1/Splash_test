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
tag=['8070166968320699506', '5884062829898474398', '6810146070790225259', '8105838278857162314', '7744106960263623416', '5679077225552137504', '6095365681616454816', '5378592275674212723', '8093916685244706914', '4878871734928263649', '6983664378165836486', '5118391565434634824', '5582869145102839922', '8515300218845360014', '5920339924959681787', '7446565317689230946', '7486814720100409246', '8557196703999379347', '7688704125257838505', '8169270262982486256', '6227996429603231641', '7369207756592543346', '4703954163400419847', '9206094520614544422', '7987651293561166324', '8043622996677747164', '7907926591538633924', '5583962440297060124', '6845408760024948703', '6082125841596152469', '4858510520373910438', '7707298551664801993', '6588937134633728832', '7668809837630806889', '5803218577346174765', '7084417675545725839', '7999162361340273909', '5512538528442914410', '5053257229678434629', '7546622999862319448', '7014126635513374746', '7716355454666155502', '8383239630699290773', '6628323800893993901', '5713727536673416374', '4815491230070864904', '6774700840389073826', '6128664332146425559', '5379820201564386154', '4917099907875268427', '5590636310985533994', '8678617251330820258', '5389319229074110740', '8473371536576321210', '5618292221166291373', '6879214608629978989', '7000128209404754832', '8749107975378029550', '7510105348019504811', '6499549001497295588']
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
            



