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
tag=['4911312717289839616', '6032178649964261345', '5096356162272529092', '4915702185297351730', '6064359523563380714', '5164963106052936461', '7661836377177593238', '5594021571438221151', '4869921288501347163', '7039345260022499934', '8349798590125374140', '6420739401233998234', '8600652201159507184', '5547685874484567364', '7190698173876843750', '7893590330107472272', '8127159644506330408', '5954000503963715603', '5361878739574519927', '7049154795792026113', '6792351999090943649', '6514106212743123384', '6497782843196184321', '5751334202061188634', '9078556757389773043', '5850181006732629270', '6315734796643552485', '8082119572774308433', '5741876864318742178', '8884162523064094408', '6685688714202323780', '6537806482436483645', '4771214428333929607', '5526956466461981871', '6452360995766818217', '9058084813150205407', '8837392004885584174', '6327210263715349537', '4957791000915385264', '8265962990537231400', '6631306221067322858', '8391399837847298042', '8793721087079950406', '6392742162254594963', '7731094146166052335', '4659082976708096479', '7881499228560463099', '4860167222171354414', '6583501042031174942', '5274074620920676712', '7566523216199263724', '7280571841518590348', '8435819325238057093', '7490198112227947016', '5473594436317061792', '7201035621214180880', '7422107160040204486', '8987229804294774064', '6428779602223632299', '6100031401874417498', '7504902881189405051', '7920497098148865906', '9124508402171129231', '4948817339406701524']
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
            



