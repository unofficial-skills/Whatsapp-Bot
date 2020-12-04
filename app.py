from flask import Flask, request
import requests
import json
from twilio.twiml.messaging_response import MessagingResponse
from googletrans import Translator

app = Flask (__ name__)

@ app.route ("/")
def hello ():
    return "Online Status"

@ app.route ('/ bot', methods = ['POST'])
def bot ():
    incoming_msg = request.values.get ('Body', '')
    #print (incoming_msg)
    resp = MessagingResponse ()
    msg = resp.message ()
    responded = False
    
    if 'start' in incoming_msg:
        text = f'🤖 _Hello I'm a Recsec Bot, Can I Help You? _ \ n \ n * Admin: * \ n \ n📞: 085885105039 \ n📱: _fb.me/rezzapriatna12_ \ n \ n🚀 * Features * \ n \ n✅ _Youtube Downloader_ \ n✅ _Facebook Downloader_ \ n✅ _Instagram Downloader_ \ n✅ _Google Search_ \ n✅ _Text To Speech_ \ n✅ _Stalking Instagram Profile_ \ n✅ _Translate_ \ n \ n \ n _To Show Command Type_ * Menu * '
        msg.body (text)
        responded = True
    if 'info-covid' in incoming_msg or 'Info-covid' in incoming_msg:
        import requests as r, json
        req = r.get ('https://coronavirus-19-api.herokuapp.com/countries/indonesia')
        reqq = r.get ('https://coronavirus-19-api.herokuapp.com/countries/world')
        jss = reqq.json ()
        js = req.json ()
        text = f '* Indonesian Coronavirus Info * \ n \ n \ n * Positive *: {js ["cases"]} \ n * Recovered *: {js ["recovered"]} \ n * Died *: {js [ "deaths"]} \ n \ n \ n * Global * \ n \ n \ n * Positive *: {jss ["cases"]} \ n * Cured *: {jss ["recovered"]} \ n * Died *: {jss ["deaths"]} '
        msg.body (text)
        responded = True
    
    if 'Menu' in incoming_msg or 'menu' in incoming_msg:
        text = f'⌨️ * List Of Command: * \ n \ n🔥 * info-covid * (Coronavirus Information) \ n \ n🔥 * / JS * _ <kota> _ Prayer Times \ n \ n🔥 * Schedule-Imsak * _Displays Imsak_ \ n \ n🔥 * / SY * _ <url> _: Youtube Search \ n \ n🔥 * / YT * _ <url> _: Youtube Downloader \ n \ n🔥 * / FB * _ <url > _: Facebook Downloader \ n \ n🔥 * / IG * _ <url> _: Instagram Downloader \ n \ n🔥 * / FL * _ <url> _: Download Video Fb Big Size \ n \ n🔥 * / GL * _ <query> _: Google Search \ n \ n🔥 * / SG * _ <usrname> _: Get Instagram Info \ n \ n🔥 * / TTS * <Text>: Text To Speech \ n \ n🔥 * / TR-id-en * _ <text> _: Translate ID> ENG \ n \ n🔥 * / TR-en-id * _ <text> _: Translate ENG> ID \ n \ n🔥 * / TR-id- kor * _ <text> _: Translate ID> Korean \ n \ n🔥 * / TR-kor-id * _ <text> _: Translate Korean> ID \ n \ n🔥 * help *: How to Use Command '
        msg.body (text)
        responded = True
        
    if '/ FB' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg [3:]
        html = r.get (par)
        video_url = re.search ('sd_src: "(. +?)"', html.text) .group (1)
        msg.media (video_url)
        responded = True
    
    if '/ IG' in incoming_msg:
        import requests as r
        par = incoming_msg [3:]
        a = r.get (par + '? __ a = 1')
        b = a.json ()
        c = b ['graphql'] ['shortcode_media']
        d = (c ('video_url']) 
        msg.media (d)
        responded = True  
        
    if '/ GL' in incoming_msg:
        from googlesearch import search
        query = incoming_msg [3:]
        for i in search (query, tld = "com", num = 10, stop = 10, pause = 2):
            text = f '========== Results ========== \ n \ n * Reff *:' + i
            msg.body (text)
            responded = True
            
    if '/ TR-en-id' in incoming_msg:
        par = incoming_msg [9:]
        translator = Translator ()
        result = translator.translate (par, src = 'en', dest = 'id')
        msg.body (result.text)
        responded = True

    if '/ TR-id-en' in incoming_msg:
        par = incoming_msg [9:]
        translator = Translator ()
        result = translator.translate (par, src = 'id', dest = 'en')
        msg.body (result.text)
        responded = True

    if '/ TR-id-kor' in incoming_msg:
        par = incoming_msg [10:]
        translator = Translator ()
        result = translator.translate (par, src = 'id', dest = 'ko')
        msg.body (result.text)
        responded = True

    if '/ TR-kor-id' in incoming_msg:
        par = incoming_msg [10:]
        translator = Translator ()
        result = translator.translate (par, src = 'ko', dest = 'id')
        msg.body (result.text)
        responded = True

    if '/ FL' in incoming_msg:
        import requests as r
        import re
        par = incoming_msg [3:]
        html = r.get (par)
        video_url = re.search ('sd_src: "(. +?)"', html.text) .group (1)
        reqq = r.get ('http://tinyurl.com/api-create.php?url='+video_url)
        msg.body ('* VIDEO CONVERT SUCCESSFULLY * \ n \ nLINK:' + reqq.text + '\ n \ n_ How to Download See Photo Above_')
        msg.media ('https://user-images.githubusercontent.com/58212770/78709692-47566900-793e-11ea-9b48-69c72f9bec1e.png')
        responded = True
        
    if '/ TTS' in incoming_msg:
        par = incoming_msg [5:]
        msg.media ('https://api.farzain.com/tts.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
        responded = True

    if '/ SG' in incoming_msg:
        import requests 
        import json
        par = incoming_msg [4:]
        p = requests.get ('http://api.farzain.com/ig_profile.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z')
        js = p.json () ['info']
        ms = (js ['profile_pict'])
        jp = p.json () ('count']
        text = f'Name: * {js ["full_name"]} * \ nUsername: {js ["username"]} \ nBio: * {js ["bio"]} * \ nWebsite: * {js ["url_bio "]} * \ nFollowers: * {jp [" followers "]} * \ nFollows: * {jp [" following "]} * \ nPost total: * {jp [" post "]} * '
        msg.body (text)
        msg.media (ms)
        responded = True

    if '/ YT' in incoming_msg:
        import pafy
        import requests as r
        par = incoming_msg [4:]
        audio = pafy.new (par)
        gen = audio.getbestaudio (preftype = 'm4a')
        genn = audio.getbestvideo (preftype = 'mp4')
        req = r.get ('http://tinyurl.com/api-create.php?url='+gen.url)
        popo = r.get ('http://tinyurl.com/api-create.php?url='+genn.url)
        msg.body ('_ ========================= _ \ n \ n _Video Successfully Converted_ \ n \ n _ ======= ================== _ \ n \ n '' * '+ gen.title +' * '' \ n \ n * Music Download Link *: '+ req.text + '\ n \ n * Video Download Link *:' + popo.text)
        responded = True
        
    if '/ SY' in incoming_msg:
        import requests as r
        par = incoming_msg [3:]
        req = r.get ('http://api.farzain.com/yt_search.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
        js = req.json () [1]
        text = f '* Title *: _ {js ["title"]} _ \ n \ n * Video Url *: _ {js ["url"]} _ \ n \ n * Video ID *: _ {js [ "videoId"]} \ n \ n_Note: If You Want To Download This Video Or Convert It To Music, Copy The Link Above And Use Command / YT_ '
        msg.body (text)
        msg.media ((js ['videoThumbs']))
        responded = True
  
    if '/ JS' in incoming_msg:
       import requests as r
       par = incoming_msg [3:]
       req = r.get ('http://api.farzain.com/shalat.php?id='+par+'&apikey=JsaChFteVJakyjBa0M5syf64z&')
       js = req.json () ['response']
       text = f '* Prayer Time * \ n \ n * Fajr *: {js ["Fajr"]} \ n * Dzuhur *: {js ["dzuhur"]} \ n * Asr *: {js ["ashar" ]} \ n * Maghrib *: {js ["maghrib"]} \ n * Isha *: {js ["isya"]} '
       msg.body (text)
       responded = True

    if 'schedule-imsak' in incoming_msg:
       msg.media ('https://user-images.githubusercontent.com/58212770/80048733-35c6b100-853b-11ea-8043-ec0614a40039.jpeg') 
       responded = True

    if 'help' in incoming_msg:
       text = f'💻 * Help For Instagram * \ n \ n / IG <Video Link> Example: \ n / IG https://www.instagram.com/p/BWhyIhRDBCw/\n\n\n*Note*: Link Must Be Like In Example If the Link Suffix Is There? Utm_source = ig_web_copy_link delete that part \ n \ n 💻 * Help For Facebook * \ n \ n / FB _link video_ Example: \ n \ n / FB https: //www.facebook com / 100010246050928 / posts / 1143182719366586 /? app = fbl \ n \ n💻 * Help For Google Search * \ n \ n / GL <Query> Example: \ n \ n / GL rezzaapr \ n \ n💻 * Help For Instagram Stalking \ n \ n / SG <username> Example:\ n \ n / SG rzapr \ n \ n💻 * Help For Translate * \ n \ nTR-id-en Translate Indonesian To English \ n \ n / TR-en-id Translate English To Indonesian \ n \ n / TR- id-kor Translate Indonesian to Korean \ n \ n / TR-kor-id Translate Korean to Indonesian \ n \ n💻 * Help For Text To Speech * \ n \ n / TTS WhatsappBotRezzaapr \ n \ nIf you want to use space, replace it with% 20 \ n \ nExample: / TTS Whatsapp% 20Bot% Rezzaapr '
       msg.body (text)
       responded = True
    
    if '!' in incoming_msg:
       import requests as r
       us = incoming_msg [2:]
       import requests
       import json
       url = 'https://wsapi.simsimi.com/190410/talk/'
       body = (
         'utext': us, 
         'lang': 'id',
         'country': ['ID'],
         'atext_bad_prob_max': '0.7'

        }
       headers = {
         'content-type': 'application / json', 
         'x-api-key': 'LKgWy5I-HoG8K0CmpWl.SNncus1UOpwBiA1XAZzA'
         }
       r = requests.post (url, data = json.dumps (body), headers = headers)
       js = r.json ()
       msg.body (js ('atext'])
       responded = True


    if responded == False:
        msg.body ('Sorry I'm Just Bots Don't Know That Command :), Please Send Start To Go To Menu')

    return str (resp)

if __name__ == "__main__":
    app.run (host = "localhost", port = 8080, debug = True)
