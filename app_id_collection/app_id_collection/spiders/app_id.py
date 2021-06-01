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
tag=['7549973420159989306', '7411577777822593693', '6624751335838954563', '7504167959029446290', '7433190886369272329', '8818570658600249412', '8362995296922581709', '8934844817417639635', '8575228985471103376', '8379352787948456724', '6898023254694664110', '8811658423008980628', '6095875190170591033', '7964341476886997370', '4797869429957581627', '6702095236133201163', '7590916797912398384', '5880951228956207670', '9077552526094869183', '7451060986947343801', '5624169070800646024', '8185455894399870312', '6678747006100997559', '8470162292005826855', '6269356150913587545', '5535019926561102412', '9086657415953279469', '4874102218850582473', '5779575383468452675', '5728369162924145444', '7309486524515020609', '8121473440812485027', '8993253642620460757', '7466443233156430359', '8581222156495904117', '6711525220589875772', '8691457771387574701', '4804313301114511746', '9077154675913081057', '6979799389566399097', '8718065524498796656', '8353442939146605749', '5486122081050178229', '8436477406500806350', '9049310609237177301', '6558548742270977952', '7307893927598530011', '6607338730335228246', '6023648979127962332', '5390714630102483222', '7738355568567943263', '7932888875375353200', '9136059489602014766', '8121441956240311957', '7429522101009857264', '5503126441247446938', '8938902551164290043', '6475577132948205198', '5794342922536174575', '4963888669521974527', '7255365202623260912', '4782332550188267506', '5401798052346676529', '6799509565022781939', '8454252303345120099', '7617774333111426494', '5247189711425325338', '4987150665919595114', '9147795173074283755', '5096340574103036603', '8015265355764080648', '5401061376614109518', '6178481237728490990', '6188194751903089253', '5286166910940102320', '5952275940526096399']
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
            



