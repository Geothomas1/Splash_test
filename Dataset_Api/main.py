import time
import urllib
import google_play_scraper
import play_scraper

from google_play_scraper import app
from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'key.json'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID a sample spreadsheet.
SPREADSHEET_ID = '1r1ifW642gcbAxDN6NbktgFhxUMhqRCKJx3CK8E82UsA'
service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

mylist=['com.generagames.deathtycoon', 'com.generamobile.bubblewords', 'com.generagames.idle.fish.inc.tycoon', 'air.com.generamobile.kingcraft', 'com.generagames.golf.legends', 'bubble.shooter.gummy.bear.pop', 'com.generagames.cafe.restaurant.management.decorating.design.story.match3', 'com.vivastudios.merge.witch.td.idle', 'com.digitalartsgames.epic.heroes.superheroes.war.action.rpg.battle', 'com.besoccergames.fantasymanager', 'com.generagames.pixvirtualpet', 'com.generagames.merge.plague.idle.tycoon', 'com.generagames.tap.pirates.idle', 'com.gi.talkinggummybearpremium', 'com.privatesolver.tiktok', 'com.alk.downloader.tiktok', 'com.alk.wordsearch', 'com.alk.wordsearch.polski', 'com.alk.wordsearch.turkce', 'com.alk.minesweeper', 'com.alk.game2048', 'com.alk.catcheggs', 'com.blogspot.santmostardacatchupdevgames.braziliancitieswordsearch', 'com.blogspot.santmostardacatchupdevgames.catswordsearch', 'com.blogspot.santmostardacatchupdevgames.memorizenumbers', 'com.Gttro.Billiards_Club', 'com.Gttro.Word_Search', 'com.ludo.snake', 'com.Gttro.Town_Running', 'com.Gttro.Unblock_Woody_puzzle', 'com.Gttro.Wood_Block_Puzzle', 'com.Gttro.Fast_Plumber', 'com.Gttro.Fruit_Farm_Garden_Smash', 'com.gttro.full.speed.drift.racing', 'com.Gttro.Zumba', 'com.havos.g.compactcrossword', 'com.havos.g.jigsaw', 'com.havos.g.jigsawplus', 'com.havos.crosswordplus', 'com.havos.numberpuzzleplus', 'com.havos.wordpuzzleplus', 'com.havos.crosswordsolverplus', 'com.havos.wordsearchplus', 'com.havos.famouspeopleplus', 'com.havos.codewordunlimitedplus', 'com.randomsaladgames.wordtwist', 'com.randomsaladgames.simpledominoes', 'com.randomsaladgames.sudoku', 'com.randomsaladgames.simpleminesweeper', 'com.randomsaladgames.simplefreecell', 'com.randomsaladgames.spider', 'com.randomsaladgames.bubblepopstar', 'com.randomsaladgames.bubblestar', 'com.randomsaladgames.crazycasino', 'com.quelaba.quelman', 'com.astraware.mahjongotd', 'com.astraware.solitaire',
'com.com.pixe.pipegame', 'com.pixe.wordsearch', 'com.pixe.connectwords', 'com.histudiogames.wordserenityg', 'com.histudiogames.wordtilepuzzleg', 'com.puzzlegamelab.wordsearchpopg', 'com.histudiogames.wordtowng', 'com.histudiogames.games.wordshop', 'com.histudiogames.wonderwordg', 'com.histudiogames.wordblastg', 'com.histudiogames.games.wordspace', 'com.monkeyrobber.games.guessmovie2015', 'com.cammaxapp.games.popcelebquiz', 'com.neptunemobilegames.wordsearch', 'com.wordgames.crossword.crossword500.game', 'com.wordgames.crossword.crossword100.game', 'com.wordgame.ws.game.wordsearch', 'com.snapartphotoeditor.fastcharger.quick.fast.battery.charging.fastcharging.batterysaver.batterymaster.superbatterycharger', 'com.snapartphotoeditor.timestampcamerafree.autotime', 'com.snapartphotoeditor.multicolorflashlight.color.flashlight.colorlight.colorflash.led', 'com.snapartphotoeditor.call.flash.color.phone.callerscreen.flashlight.ledlight.changertheme.phoneflash', 'com.snapartphotoeditor.Word_Search.wordgames.wordchallenge.word.search', 'com.snapartphotoeditor.vintage.camera.kojicam.camerafilter.retrocamera.vintagefilter.filtercam.retrofilter.vhscam', 'com.snapartphotoeditor.vider.cutter.videocutter.audiocutter.ringtonecutter.trimmercutter.allvideocutter.mp4cutter.videotools', 'com.snapartphotoeditor.anyvideoaudio.cutter.totalvideoconverter.allmediaconverter.videoeditor.video_converter.moviemaker', 'com.snapartphotoeditor.palm.astrology.soular.star.daily.horoscope.solarsmash.fortunescope', 'com.snapartphotoeditor.curriculumvitae.resume.maker.cvmaker.resumeformat.cv.builder', 'com.puzzle1studio.go.bubblepoporiginpuzzlegame', 'com.puzzle1studio.go.brickoutshoottheball', 'com.bitmango.go.wordcookies', 'com.bitmango.go.blocktrianglepuzzletangram', 'com.bitmango.go.bubblepop', 'com.bitmango.go.mahjongsolitaireclassic', 'com.bitmango.go.blockhexapuzzle', 'com.bitmango.go.jewelmatchking', 'com.bitmango.go.jewelsmagicmysterymatch3', 'com.bitmango.go.linepuzzlepipeart', 'find.image.difference.game.com', 'games.urmobi.tap.tile.mahjong', 'find.image.difference.game.com.ver.two', 'com.urmobi.BloomingFlowers', 'co.urmobi.four.photos.one.word', 'games.urmobi.findandtap.hidden.objects', 'co.urmobi.casual.larrysfishing', 'games.urmobi.word.dices', 'find.image.difference.game.com.ver.three.red', 'co.urmobi.casual.guessthepictures', 'com.akiwy.wordsearchpictures', 'com.akiwy.free.brain.training.sudoku.iq', 'com.wordblocksfun.wordblocksaquamarine', 'com.unicostudio.braintest', 'com.unicostudio.whois', 'com.unicostudio.braintest2new', 'com.unicostudio.braintest3', 'com.unicostudio.wordpirates', 'com.unicostudio.whois2', 'com.oakgames.wordgame', 'com.unicostudio.trickywords', 'com.Magnistart.medievalio', 'com.unicostudio.sudoku', 'com.blacklightsw.ludo', 'com.blacklight.carrom.multiplayer', 'com.blacklight.callbreak', 'com.blacklight.spidersolitaire', 'com.blacklight.solitaire', 'com.blacklight.wordament', 'com.blacklight.solitaire.zen', 'com.blacklight.word.alchemy', 'com.blacklight.freecell.solitaire', 'com.blacklight.klondike.patience.solitaire', 'com.digitalfunmedia.easycrosswords', 'com.digitalfunmedia.ldsgames', 'com.digitalfunmedia.photopuzzle', 'com.digitalfunmedia.wordsearchlibrary', 'com.digitalfunmedia.ldswordsearch', 'com.digitalfunmedia.cmyk', 'com.digitalfunmedia.christmascrosswords', 'com.digitalfunmedia.wordgamescrosswordwordsearchquotepuzzles', 'com.digitalfunmedia.ldstemplepuzzles', 'com.digitalfunmedia.holidaywordsearchpuzzles', 'com.photon.shake2safety', 'com.photonapps.wordsearch', 'com.photonapps.carpediem', 'photonapps.com.selfiewallpaper', 'com.photonapps.yobucket.android', 'com.photon.mydiary', 'com.photon.lifereboot', 'com.photon.travelmania', 'com.photon.shitmaster', 'com.officedocument.word.docx.document.viewer', 'com.wordoffice.docx.docs.docxreader.freeword', 'com.wordpz.word.blocken', 'com.type.race.word.puzzles', 'com.wordpz.guesswords.braingame', 'com.wordpz.cross.linkwords', 'com.wordpz.link.search', 'com.xdev.docxreader.docx.docxviewer.document.doc.office.viewer.reader.word', 'com.xsdev.xls.xlsx.excelviwer.excelreader.spread.sheets', 'com.email.fast.secure.mail', 'com.rpdev.document.manager.reader.allfiles', 'com.rpdev.docx.doc.ppt.pptx.xls.xlsx.pdf.pro', 'helium.wordoftheday.learnenglish.vocab', 'helium.idioms.phrases.learnenglish', 'helium.wordoftheday.learnspanish.vocab', 'helium.wordoftheday.learnfrench.bonjour.vocab']

c=1
data = []
for i in mylist:
    try:
        result = app(i, lang='en', country='us')
        res=play_scraper.details(i)
        data.append([
            result['title'] if result['title'] != None else  'N/A' if 'title' in result.keys() else  'N/A',
            result['appId'] if result['appId'] != None else  'N/A' if 'appId' in result.keys() else  'N/A',
            result['genre'] if result['genre'] != None else  'N/A' if 'genre' in result.keys() else  'N/A',
            result['score'] if result['score'] != None else  'N/A' if 'score' in result.keys() else  'N/A',
            result['ratings'] if result['ratings'] != None else  'N/A' if 'ratings' in result.keys() else  'N/A',
            result['installs'] if result['installs'] != None else  'N/A' if 'installs' in result.keys() else  'N/A',
            result['minInstalls'] if result['minInstalls'] != None else  'N/A' if 'minInstalls' in result.keys() else  'N/A',
            result['free'] if result['free'] != None else  'N/A' if 'free' in result.keys() else  'N/A',
            result['price'] if result['price'] != None else  'N/A' if 'price' in result.keys() else  'N/A',
            result['currency'] if result['currency'] != None else  'N/A' if 'currency' in result.keys() else  'N/A',
            result['size'] if result['size'] != None else  'N/A' if 'size' in result.keys() else  'N/A',
            result['androidVersion'] if result['androidVersion'] != None else  'N/A' if 'androidVersion' in result.keys() else  'N/A',
            result['developerId'] if result['developerId'] != None else  'N/A' if 'developerId' in result.keys() else  'N/A',
            result['developerWebsite'] if result['developerWebsite'] != None else  'N/A' if 'developerWebsite' in result.keys() else  'N/A',
            result['developerEmail'] if result['developerEmail'] != None else  'N/A' if 'developerEmail' in result.keys() else  'N/A',
            result['released'] if result['released'] != None else  'N/A' if 'released' in result.keys() else  'N/A',
            res['updated'] if res['updated'] != None else  'N/A' if 'updated' in res.keys() else  'N/A',
            result['privacyPolicy'] if result['privacyPolicy'] != None else  'N/A' if 'privacyPolicy' in result.keys() else  'N/A',
            result['contentRating'] if result['contentRating'] != None else  'N/A' if 'contentRating' in result.keys() else  'N/A',
            result['adSupported'] if result['adSupported'] != None else  'N/A' if 'adSupported' in result.keys() else  'N/A',
            result['offersIAP'] if result['offersIAP'] != None else  'N/A' if 'offersIAP' in result.keys() else  'N/A',
            result['editorsChoice'] if result['editorsChoice'] != None else  'N/A' if 'editorsChoice' in result.keys() else  'N/A',
            result['summary'] if result['summary'] != None else  'N/A' if 'summary' in result.keys() else  'N/A',
            result['reviews'] if result['reviews'] != None else  'N/A' if 'reviews' in result.keys() else  'N/A',
            result['androidVersionText'] if result['androidVersionText'] != None else  'N/A' if 'androidVersionText' in result.keys() else  'N/A',
            result['developer'] if result['developer'] != None else  'N/A' if 'developer' in result.keys() else  'N/A',
            result['developerAddress'] if result['developerAddress'] != None else  'N/A' if 'developerAddress' in result.keys() else  'N/A',
            result['developerInternalID'] if result['developerInternalID'] != None else  'N/A' if 'developerInternalID' in result.keys() else  'N/A',
            result['version'] if result['version'] != None else  'N/A' if 'version' in result.keys() else  'N/A'])
        print(c)
        print(result['appId'])
        c=c+1
        # if 40 and (c % 40) == 0:
        #     print("On Sleep 62 sec")
        #     time.sleep(62)
        # print(data)
    except urllib.error.HTTPError:
        print('Exception 1 skip')
        continue
    except google_play_scraper.exceptions.NotFoundError:
        print('Exception 2 skip')
        continue
result1 = sheet.values().append(spreadsheetId=SPREADSHEET_ID,range="Sheet2!A1:AC1", valueInputOption="USER_ENTERED",insertDataOption="INSERT_ROWS",body={"values":data}).execute()

    