import twitter
import os

import codecs
import re
from textblob import TextBlob

#Keys redacted
api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    s = s.replace("\n", " ")
    # replace lines
    s = re.sub(r'http\S*', 'link', s)
    return s


data = {'Alabama': [['AlabamaFTBL', 'DrRobertBentley', 'GovernorKayIvey'], 0],
        'Alaska': [['SarahPalinUSA', 'adndotcom', 'AlaskaWx'], 0],
        'Arizona':[['SenJohnMcCain', 'abc15', 'Suns'],0],
        'Arkansas':[['Arkansasgov', 'UArkansas', 'AustinKellerman'],0],
        'California':[['RepAdamSchiff', 'LANow', 'LAPDHQ'],0],
        'Colorado':[['Denverpost', 'Rockies', 'ColoradoDOT'],0],
        'Connecticut':[['connpost', 'CorcoranTerence', 'bobbrownct'],0],
        'Delware':[['JoeBiden', 'carronJphillips', 'GovernorMarkell'],0],
        'Florida':[['marcorubio','nbc6', 'FranklyFlorida'],0],
        'Georgia':[['QuavoStuntin', 'Braves', 'ajc'],0],
        'Hawaii':[['hawaii','HawaiiNewsNow','Volcanoes_NPS'],0],
        'Idaho':[['KTVB','IdahoPotato','KevinRichert'],0],
        'Illinois':[['nprillinois', 'SenatorKirk', 'Cubs'],0],
        'Indiana':[['Pacers', 'IndianaUniv', 'IndStatePolice'],0],
        'Iowa':[['IowaPublicRadio', 'IowaGOPer ‏', 'iowadot'],0],
        'Kansas':[['Royals', 'KansasCityKDOT', 'KCTV5'],0],
        'Kentucky':[['RandPaul', 'UKCoachCalipari','WKYT'],0],
        'Louisiana':[['BobbyJindal','theadvocatebr', 'JonathanWashamh'],0],
        'Maine':[['PressHerald', 'chelliepingree', 'MaineDOT1'],0],
        'Maryland':[['MartinOMalley', 'MdWeather', 'WTOPinMD'],0],
        'Massachuesetts':[['SenWarren', 'MassStatePolice', 'MittRomney'],0],
        'Michigan':[['onetoughnerd', 'CoachJim4UM', 'AndreaBitely'],0],
        'Minnesota':[['WCCO', 'MPRnews', 'edinacityman'],0],
        'Mississippi':[['clarionledger', 'CoachDanMullen', 'MississippiDOT'],0],
        'Missouri':[['GovJayNixon', 'MoGov', 'MoDOT'],0],
        'Montana':[['mtpublicradio','NBCMontana', 'GovernorBullock'],0],
        'Nebraska':[['NBCNebraska', 'CoachMiles', 'NECornBoard'],0],
        'Nevada':[['SenatorReid', 'LasVegasSun', 'SteveSebelius'],0],
        'New Hampshire':[['NewHampshireDOT', 'nhpr', '603facts'],0],
        'New Jersey':[['corybooker', 'NJGOP', 'NJSP'],0],
        'New Mexico':[['KOB4', 'NewMexicoOAG', 'ThinkNewMexico'],0],
        'New York':[['nytimes', 'humansofny', 'ericbolling'],0],
        'North Carolina':[['newsobserver', 'SenatorBurr', 'HarrisTeeter'],0],
        'North Dakota':[['BismarckPolice', 'AP_NorthDakota', 'SenJohnHoeven'],0],
        'Ohio':[['OhioState', 'JohnKasich', 'DispatchAlerts'],0],
        'Oklahoma:':[['OKDOT', 'NEWS9', 'StateImpactOK'],0],
        'Oregon':[['OregonDOT', 'OregonGovBrown','Oregonian'],0],
        'Pennsylvania':[['GovernorTomWolf', 'SeanFedorko', 'fox43'],0],
        'Rhode Island':[['jonbouch','NBC10','GinaRaimondo'],0],
        'South Carolina':[['MayorKnoxWhite','thestate','GrahamBlog'],0],
        'South Dakota':[['PriceHP1','argusleader','johnthune'],0],
        'Tennessee':[['Titans', 'TEN_GOP', 'tndp'],0],
        'Texas':[['3lectric5heep','TexasObserver','ayanmittra'],0],
        'Utah':[['abc4utah', 'GovHerbert','UtahDOT'],0],
        'Vermont':[['SenSanders', 'VermontCynic','VTStatePolice'],0],
        'Virginia':[['timkaine','DMVFollowers','pattonoswalt'],0],
        'Washington':[['wsdot','SenatorCantwell', 'BillGates'],0],
        'West Virginia':[['WestVirginiaU','WVGovernor','wchs8fox11'],0],
        'Wisconsin':[['CityofManitowoc','WiStateJournal', 'SpartaWIPD'],0],
        'Wyoming':[['WyomingPBS','wyomingpd', 'butterbob'],0]}

#print data['Alabama']
print("Start Samuel's program")

for state, info in data.items():
    # print (state)
    twitter_handles = info[0]
    sentiment = info[1]
    # reset to 0 for each state
    for id in twitter_handles:
        statuses = api.GetUserTimeline(screen_name=id, exclude_replies=True, include_rts=False, count='1')
        for s in statuses:
            blob = TextBlob(s.text)
            for sentence in blob.sentences:
                sentiment += sentence.sentiment.polarity

    # print(sentiment)
    # store it in our data structure
    info[1] = sentiment

file = codecs.open('output.txt', "w", "utf8")
# print results to file
for state, info in data.items():
    print(state)
    print(info[1])  # this is the sentiment aggregation
    file.write(state + "," + str(info[1]) + "\n")

file.close()


def find_state_index(state_abb):
    for a in attributes:
        if (a['id'] == state_abb):
            return a


def set_state_color(state, hexcolor):
    state['fill'] = hexcolor


from svgpathtools import svg2paths2, wsvg

# load basic map
paths, attributes, svg_attributes = svg2paths2('map.svg')

# find the state base on abbreviation
state = find_state_index("VA")
# set the color
set_state_color(state, "#0000ff")

#Assign value to happiness rating
#Code redacted

# write svg file
wsvg(paths, attributes=attributes, svg_attributes=svg_attributes, filename='new_map.svg')
print("End Samuel's program")

#VeryHighHappiness (X >= 1)
#estatic = ['VA', 'DC','WA','NY', 'AL', 'HI', 'LA', 'ME', 'MA']

#HighHappiness ( 1 > X >0.5)
#'MO', 'KT', 'KA' 'UT', 'MS', 'OH', 'PA', 'NV', 'IA', 'SC', 'OR', 'NH', 'Wyoming'

#Average(0.5> X >0.1 )
#'WV','SD', 'MD', 'FL', 'AK', 'MN', 'NM', 'CT', 'WI', 'NJ', 'OK', 'TX','ND', 'AK', 'CA',

#Neutral (0.1 > X >=0)
#VT', 'NE', 'NC', 'DE', 'MI', 'CO', 'ID', 'GA'

#LowHappiness ( 0 < X > -0.5)
#'IN', 'IL', 'AZ', 'RI'

#LittleHappiness( X < -0.5)
#'MO', 'TN'
