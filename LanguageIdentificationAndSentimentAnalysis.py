from polyglot.detect import Detector
from polyglot.text import Text
from polyglot.downloader import downloader
import csv
import tweepy
from flask import Flask, request


app = Flask(__name__)

@app.route('/query-example')
def query_example():
    print('receiving incoming request...')
    value = request.args.get('language')
    return '''<h1> The language value is : {}<h1>'''.format(value)

@app.route('/form-example', methods = ['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''<h1> The language value is : {}<h1>
                  <h1> The frameworkvalue is : {}<h1>'''.format(language,framework)
    return '''<form method='POST'>
                Language: <input type="text" name="language"/><br/>
                Framework: <input type="text" name="framework"/><br/>
                <input type="submit" value="Submit"><br/>
                </form>'''

@app.route('/json-example', methods=['POST'])
def json_example():
    req_data = request.get_json()

    language = None
    if 'language' in req_data:
        language = req_data['language']
    framework = req_data['framework']
    website = req_data['website']
    python_version = req_data['version_info']['python']
    flask_version = req_data['version_info']['flask']
    example_three = req_data['examples'][2]
    status = req_data['boolean_test']
    return '''
            language:{},
            framework:{},
            website:{},
            python version:{},
            flask version:{},
            example number 3:{},
            status:{}
            '''.format(language,framework,website,python_version,flask_version,example_three,status)

if __name__ == '__main__':
    app.run(debug = True, port = 6001)



























written_text= u"""Kọmiṣọna fun ajọ INEC nipinlẹ Ekiti ni INEC ṣetan láti fẹ̀sùn ìbanilórúkọjẹ́ kan ẹnikẹ́ni to ba n sọ ohun tójú rẹ̀ kò tó nípa ìdìbò Ekiti.
Gbágbáàgbá ni àwọn òṣìṣẹ́ ètò àábò dúró ní ibi tí wan ti n pín òhun èlò ìdìbà nàá
Saraki ninu ọrọ kan to fi si oju opo Twitter rẹ ni, ileeṣẹ ọlọpa ti fi ọwọ́ oṣelu mu ọrọ idigunjale naa.
Theresa May sọkalẹ ni Naijiria
Ile-išẹ olopa ti balẹ si nipasẹ Fọto ti Awọn Times.
Onye nchịkwa Super Eagles Super Eagles, Gernot Rohr, na-ekwu na Nigeria na-enwe obi ụtọ imeri Poland maka egwuregwu enyi ha na-egwu na Stadium Municipal, Wroclaw na Friday.
Ninu lẹta kan ti ọlọpa ọlọpa ti Saraki lọ si Sisiko ni Ojobo, o ko le ṣe alaabo ninu ibasepọ rẹ pẹlu awọn iparun ti a ko mọ tẹlẹ.
Awọn ọdọmọkunrin lu 'eja' ti o pa ọdọmọkunrin kan pẹlu ọkọ ayọkẹlẹ kan
Juan Martin del Potro emeriwo aha BNP Paribas Open maka ebe ndị India.
Iyaafin Adebayor: Ile-iṣẹ iṣowo Yorùbá ko le gba owo diẹ sii ju fifuyẹ
Ile-iwe giga ti OAU ni aabo fun gbogbo ọmọ ile-iwe ti awọn alakoso ti ta ọ ni ibajẹ ti ina
Bishop David Oyedepo ti pe Ijoba orile-ede Naijiria, Muhammadu Buhari, lati kọwe lori awọn ẹsun ti awọn ọlọpa Fulani ti o fa awọn eniyan.
Dr Ugochukwu Eze, wey dey work for National Eye Centre Kaduna, say, glaucoma na disease wey dey kill small-small wire dem wey connect our eyes with our brain. Once di wires die, di eye don go be dat.
Wọn ti wa ni ẹtọ pe o lodi si awọn esi ti idibo, eyiti Ogbeni Ademola Adeleke ti gba
Federal Government don carry case go Federal High Court to seize 22 property wey belong to Deputy Senate President Ike Ekweremadu.
Agbegbe Akin Ogunbiyi, ti o ba jẹ pe alakoso naa tẹsiwaju lati gba Ademola Adeleke gẹgẹbi oludibo PDP ti o wa ninu idibo igbimọ ti yoo waye ni osu to koja, nigbana ni ẹgbẹ yoo padanu ipo ti bãlẹ.
Sôugboôn ni Akin Ogunbiyi, eôgbeô naa ti kopa si ibesile iwa-ipa ti inu ti o waye ni ipari ose ni olu-ilu.
Pope Francis amachibidoro ịṅụ sịga n'ime Vatican, site na mmalite nke afọ ọzọ.
Mẹnu mẹwa ti a ti fura pe wọn ti ku ni ọna ilu Abuja lọ si Kaduna ni ọjọ Sunday, nibiti a ti pa olugbala kan ti ologun ati pe ọpọlọpọ awọn eniyan ti jade kuro.
Arinrinajo miran jẹri wipe, ọlọpa kan naa wa lara awọn ti wọn padanu ẹmi wọn ninu iṣẹlẹ ọhun.
Ile-iṣẹ aladugbo ti o wa nitosi ni orile-ede Naijiria kan ti o wa nitosi ti sọ pe o le wa awọn eniyan meji ti o` ku ni awọn ijiyan laarin awọn oluso-aguntan ati awọn agbe ni ọdun 17th ni Nigeria-oorun.
ọpọlọpọ nọmba ti awọn eniyan ni won pa ni kan bombu kolu ni ilu Benue
Wọn fi kun pe awọn iṣẹlẹ ti o tun waye ni iṣẹlẹ naa, nipa pipinka ohun-ini ti awọn eniyan ti o ni inira.
Open-angle glaucoma worry pass for West Africa and every Nigeria person fit turn blind sake of am.
Gbajugbaja olorin takasufe ni, Simi ti ke gbajare sita pe ohun ko lọwọ ninu eto awọn ọdọ kan ti wọn ni wọn n fi igba miliọnu fun oun atawọn olorin miiran lati polongo idibo lẹẹkeji fun aarẹ Buhari.
Leah Shafik bụ nanị nwa akwụkwọ nke Ọchịchị Ụmụ agbọghọ Na-ahụ Maka Ọchịchị na Ụlọ Ọrụ Nkà na Ụzụ, Dapchi, na steeti Yobe, nke ndị Boko Haram ka na-ebubo.
Juan Martin del Potro don knack world number one Roger Federer to win di BNP Paribas Open title for Indian Wells.
Simi fesi si ọrọ yii nigba ti awọn ololufẹ rẹ kan sọrọ sita lori iroyin naa ti pupọ wọn si n fi aidunnu wọn han lori rẹ.
Gọọmentị Federal adawo ikpe ahụ n'ụlọikpe nnukwu ụlọikpe Federal iji kpochapụ ikike 22 nke na-anọchite anya Onye isi Omeiwu President Ike Ekweremadu.
Akọringbayi naa to ṣẹṣẹ pari ode orin kan pẹlu agba ọjẹ olorin ni, Lagbaja nilu Abuja ṣalaye pe ọrọ naa dun oun gidigidi.
Ninu atẹjade kan ti alukoro ileeṣẹ ọlọpaa ni ipinlẹ Eko fi sita, ọwọ awọn ọtọlẹmuyẹ tẹ ọgbẹni Hassan Maiwake ni ilu Kano ṣugbọn awakọ ajagbe elepo naa ṣi na papa bora
Di National Bureau of Statistics (NBS) measure Gross Domestic Product (GDP) and other things, to report say di economy of di West African country don dey improve.
Ileeṣẹ ọlọpaa ni ọwọ awọn ti tẹ arakunrin ti o ni ọkọ agbepo to ṣokunfa ijamba ina to waye lori afara Ọtẹdọla nilu Eko."""
#text = Text(written_text)
#text = open("C:\Hackathon\WhatsAppTexts\WhatsApp Chat with Moniepoint Agent Kogi.txt", "r")
#print(text.read())
#number = "test"

##file_name = 'Sentiment_Analysis_of_{}_Statements.csv'.format(number)
##
##with open(file_name, 'w', newline='') as csvfile:
##   csv_writer = csv.DictWriter(
##       f=csvfile,
##       fieldnames=["Text", "Language", "Sentiment"]
##   )
##   csv_writer.writeheader()
##
##   print("I have created a CSV file to store your results. \n")
##
##   for w in text.sentences:
##        csv_writer.writerow({
##           'Text': u"""{}""".format(w).encode('ascii', 'ignore'),
##           'Language':Detector(u"""{}""".format(w)).language.name,
##           'Sentiment':w.polarity
##       })
