import scrapy
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

#url=['https://play.google.com/store/apps/developer?id='+i for i in tag]
class DeveloperSpider(scrapy.Spider):
    name = 'developer'
    allowed_domains = ['x']
    def start_requests(self):
        tag=['Tototomato', 'HLAPPS', 'Appnotize+UG', 'portmixapps', 'Madeeha+sales+Corporation', 'Marcos+Lynch', 'BizChat', 'Deaf+Tech+Corp', 'BkiT+Software+%7C+T%E1%BB%AB+%C4%91i%E1%BB%83n+-+Ngo%E1%BA%A1i+ng%E1%BB%AF', 'SpotCues', 'Binary+Tuts', 'SaNDS+Lab+Pvt+Ltd', 'Sena+Technologies,+Inc.', 'Apps+Free+Inc.', 'Eduction+Notes', 'Investment+Tips', 'RC%27S+Developers', 'app4daily', 'TonyJet', 'Misty+Web', 'Sana+Edutech', 'psychic+power+reading', 'DhadbadatiApps', 'English+Talk+IT+Solution', 'Think-Grow', 'AppsNas+Studio', 'TechnoSoft+Inovation', '10tecs.com', 'Deep+Learn+Studio+App', 'TalkEnglish', 'NAVA+Apps', 'AppsPool', 'MixLabPro', 'BEAM+Education+Foundation', 'EDVL', 'ChillSeekers', 'Mishori', 'SuperSimpleVideo', 'Cyber+Solution+%28S%29+Pte+Ltd', 'GK+Training', 'Aspasia+Apps', 'Masanori+Kubota', 'Didactic+Labs,+S.L.', 'Datagain+Inc.', 'VNC+-+Virtual+Network+Consult+AG', 'Scrat', 'Omni+JD', 'Dinatale', 'Crait+Technology+Inc.', 'FieldChat', 'mobilize.io', 'YQP', 'Knowledge+Project', 'Ngan+Hoang+Nguyen', 'Education+Alicia+Media', 'Saurabh+Dhariwal', 'Redroide', 'Galaxy+Studio+Digital', 'teachoo', 'PERC+Learning+Portal', 'Dmitry+Nikolskiy', 'achraf96', 'AppsGurus24', 'AppInAll,+Inc.', 'Candex+Technologies+Ltd.', 'Apilogic', 'TechNew+App', 'JOSE+MUNOZ', 'Docapps+LLC', 'CVDN', 'vasques.andromo', 'AppsBond', 'Kencil', '9D+Techno', 'COACH+A+Co.,+Ltd.', 'Brightson+Learners+Inc.', 'WordsMaya+EduTech+Private+Limited', 'SKYRAS+Private+Limited', 'AcademiaApps', 'DotConnect,+Inc.', 'KVENTURES', 'Modest+Tree+Media+Inc', 'Ablion', 'Shael', 'The+Ring+Ring+Company+SA/NV', 'application+manager', 'RueBaRue', 'Spider50n3t', 'Neesa+Apps+Studio', 'Ignitho+Technologies+Limited', 'TuanEnglish', 'Naba+Sansar+Developers', 'Clandestine+Insights', 'venkatperumal', 'ChatPoint+Technologies+Limited', 'Bright+Office+Systems', 'NSDSK', 'Educational+Appz', 'Netbhet', 'AL+HADI', 'SCMC+Private+Limited', 'Prasanna+Patra', 'X-SYSTEMS', 'Omni+Services', 'PhonePe', 'WhatsApp+LLC', 'Oriflame', 'Reliance+Retail+Ltd', 'Facebook', 'Bloomberg+LP+CM', 'Bada+Business+Pvt.+Ltd.', 'Sulekha', 'nearbuy+India+Private+Limited', 'Business+Insider,+Inc.', 'Real+Monk+Games', 'epaylater.in', 'Indian+Oil+Corporation+Ltd', 'Amazon+Mobile+LLC', 'Redmil+Business+Mall+Pvt.+Ltd.', 'JBB+Parchisi+Ludo+Game+Studio', 'Earth+and+Space+Games', 'PayPal+Mobile', 'Magzter+Inc.', 'SEGB', 'Udemy', 'Ooma', 'Kutir+Soft', 'Iris+Studios+and+Services', 'gameworld.zone', 'Bada+Business+Consultant', 'Golden-Accounting', 'ISED-ISDE', 'SHOPX', 'RAKBANK', 'RCSTUDIOAPPS', 'State+Bank+of+India', 'Biztree+Inc.', 'Centro+Mobile', 'Kasturi+and+Sons+Ltd.', 'Flexiloans.com', 'GSW+Connect', 'Freecharge', 'Van+Ons+BV', 'HT+Media+Ltd', 'ZEE+MEDIA+CORPORATION+LTD', 'Lendingkart+Technologies', 'Language+Success+Press', 'MINDBODY+Inc', 'Photo+Studio+%26+Picture+Editor+Lab', 'MobiKwik', 'Academy+IT+Ltd.', 'Kei3N+Apps', 'Kewlieo+Games', 'Bikayi+-+Setup+online+Shop,+Take+Payments,+orders.', 'Pedago,+LLC', 'Digital+Attitude+Games', 'E-Startup+India', 'Mob+Business', 'Rodan+mobile+Kft', 'Kumar+Savar+Malhotra+%28KSMSOFTTECH%29', 'Elvira+Parpalac', 'WFI', 'Elite+Business+Plans', 'NeatHippo', 'Pro+Data+Doctor+Pvt.+Ltd.', 'Business+Standard', 'Dogmaz+Mobile', 'Puzzle+and+Ludo+Games+for+Kids', 'Alex+Genadinik', 'postermakerflyerdesigner.com', 'MWB+Games', 'Omkarti+Studio', 'Rangus', 'Thomsen+Business+Information', 'Gaming+Solution+Studio', 'SoloSoft', 'Monre+Mobile', 'Fame+App', 'Basic+App+Lab', 'APPS+4+ALL', '1C-Rarus+Ltd.', 'Investor%27s+Business+Daily,+Inc', 'Aspire+FT', 'Sim+Companies+s.r.o.', 'Joygame+Mobile', 'GoSite', 'stylish+app+world', 'Open+Appliances', 'Shoopy+-+Online+Store,+Digital+Shop+%26+Invoicing', 'bijnis.com', 'Startup+Space,+LLC', 'CREDAPP+SOFTWARE+PRIVATE+LIMITED', 'ZenConix', 'NeoGrowth+Credit+Pvt.+Ltd.', 'Harvard+Business+Review', 'Open+Financial+Technologies', 'Reflex+developers', 'Brandon+Stecklein', 'Mike+Silver', 'Dis+Cam+Fun+Foto+Sticker', 'Linq,+an+IIT+Delhi+Company', 'Pro+Learning+Apps', 'Crazy+Turtle', 'Math+Apps', 'andreyam', 'banner+design+%26+poster+maker+studio', 'Tradeindia.com', 'Store+My+Store', 'CO.,+LTD.+TAS', 'MangaK+Team', 'Saena+App', 'Business+Card+Maker', 'E-Dictionary', 'Hightech+Solution', 'RABS+Net+Solutions', 'book+app+developer', 'MY+BUSINESS+BAZAR', 'ArabSBA', 'NAM+India', 'Likhwa+Launchpad+Technologies+Ltd.', 'ICICI+Bank+Ltd.', 'Chanakya+Uge', 'Bcreative+Solutions', 'Mohanbakriapp', 'SuarezFun', 'theBusinesSoft', 'Blueduck', 'Innovative+Bangla+Apps', 'Digital+Smart+Apps', 'SNS+Lab', 'Vimoo+Softs', 'Digital+Books+Corp.', 'Horne+Tech', 'Livros', 'Free+Mobile+Apps+Online', 'DANIIL+PERFILIEV', 'Bloser117', 'Rain+King', 'Plausible+Quotes+Status', 'TELUGU+EKALAVYA+APPS', 'All+Bangla+App+71', 'Apps+Katta', 'Azadeasy+Advertising+and+Marketing+Pvt.+Ltd', 'Biz+Tech', 'Kulfi+Production', 'Sunkanmi+Vaughan', 'DEVET', 'Fun+With+Brain', 'Excel+Devers', 'vjgamestech', 'Mahadev+Bhel', 'Paago', 'Mitra+Ringtones', 'SHRIKANT+PRASAD', 'paytmonline', 'Mynarski', 'All+India+App', 'Warriors+Apps', 'Rowan+Saturnin', 'Jiom+Business+Loan', 'MadCodes', 'Discom', 'Robot+App+Developer', 'Helpful+Books', 'Biblias+gratis', 'Hurix+Systems+Private+Limited.', 'League+of+Success', 'Screech+Studios', 'SimpleBrands', 'Deepak+Pratap+Seth', 'MyLang+Books', 'KiVii', 'Mobilityappz', 'IndiaFin+Technologies', 'FastResult', 'Sushmush+Technologies+Private+Limited', 'World+Book+Inc.', 'Inkers+App', 'Naarayan+chaudhary', 'Muhammad+Hasnat+Agha', 'Christian+Bible+Reference+Site', 'Kevin+Ilondo', 'SQL+Uniform+Kft.', 'Eclat+Engineering']
        for i in tag:
            url='https://play.google.com/store/apps/developer?id='+i
            yield SplashRequest(url, self.parse,  endpoint='execute', args={'lua_source': script, 'url': url})
        

    def parse(self, response):
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
        yield{'id':temp_list}  

        
