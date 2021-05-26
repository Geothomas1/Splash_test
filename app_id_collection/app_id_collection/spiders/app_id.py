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
tag=['8380470199899417697', '6582390767433501974', '7675344623603565765', '5652667578208171950', '5427160200036080377', '4776981290922417898', '8932007797296814332', '5522734199413528853', '9158136791003968176', '4735332361278858629', '6226578379913768853', '7278677227391352388', '5857051835670297644', '8557663908115257455', '8699091863914594470', '7045916445723921739', '8849558708667380674', '7106397920817952056', '5863340256934780627', '8135450305244092732', '5877779642774905506', '6168495537212917027', '8026626984524329663', '8807776165917405571', '7864341087698885709', '5854296851384590428', '4733712356377609550', '5139937123317090348', '6942868991117147695', '5095485660946297779', '6536165328366526192', '8850688897727506884', '7755806177820766361', '5053419609952754733', '7957760354032996428', '4971215016306014222', '6718691337344232502', '6447526686415699485', '7116232723736125231', '6724611194209488488', '6200699041249741037', '4947164804079472463', '4965522548888268835', '5371863574050311237', '8694952062561571678', '5182960695633864714', '4821115570221044110', '6384099504492697499', '8310417384362712900', '7116097667837466463', '5631376253411320738', '8709197346220972333', '8030842704688726777', '6356225441181448806', '7350004246480558648', '6945190962187515039', '9018923847416797870', '5794986670423728237', '6514398275227441467', '7580346547645826570', '5585358480202910007', '8722840249183358081', '5477562049350283357', '8102918818633480134', '8766043678304054984', '4989415515923054647', '7369633454303299128', '4676919139121964344']
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
            



