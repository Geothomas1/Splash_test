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
tag=['8239756191650284197', '8275965303018699572', '9150797235455042117', '6469905677578050913', '8586972655871445071', '6332795247814868794', '7331133115474991791', '5674121407737265103', '5014287650272012074', '7947961505176709798', '6031852891987104213', '7018349861892896519', '5735909854193040295', '9119797059737882959', '6859510611266901148', '6034501392493679748', '6712508869400983474', '8297463101500330997', '7125208715478885726', '5938965124213916586', '5855536323120230239', '8433682105452773216', '5658487042934933187', '5337085449729943630', '5076703042154466763', '4887849233598939093', '9140891030599783573', '6219116073460792341', '6812023808073375462', '5105018118798378984', '4668137433251011654', '6266259325837450446', '5719972785273795815', '5682092345947134061', '8820029808323517015', '6289963163291423344', '6763735467206988116', '9031934542678943841', '4955942127185572612', '6218290117784571180', '6924427178916888797', '7883797435983636106', '5249600725214038377', '9136901015336626363', '6959131348818971678', '8021234394233554810', '8129971753348889959', '5864540979910006866', '5266393312181689607', '8047064488135277009', '8052634537736937646', '4713694906040742845', '5458280395971957816', '9145978338019495213', '6201001580493786609', '6768186915999045022', '5373477450656230530', '6667393564176393731', '8240974659502655461', '6440204902466821155', '5004362291850449195', '7946143807833670199', '7565557142221656126', '6752338617690791833', '9071981731314566656', '5343199424914104502', '7872895454960342219', '5433282864668909178', '7203351113096085884', '5565400440751704204', '5953058807848933229', '5556885535751560196']
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
            



