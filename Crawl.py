import twitter
import codecs

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

print('start harvest')

ids = [
#Alabama
'AlabamaFTBL','DrRobertBentley', 'GovernorKayIvey',
#Alaska
'SarahPalinUSA', 'adndotcom', 'AlaskaWx',
#Arizona
'SenJohnMcCain', 'abc15', 'Suns',
#Arkansas
'Arkansasgov', 'UArkansas', 'AustinKellerman',
#California
'RepAdamSchiff', 'LANow', 'LAPDHQ',
#Colorado
'Denverpost', 'Rockies', 'ColoradoDOT',
#Connecticut
'connpost', 'CorcoranTerence', 'bobbrownct',
#Delaware
'JoeBiden', 'carronJphillips', 'GovernorMarkell',
#Florida
'marcorubio','nbc6', 'FranklyFlorida',
#Georgia
'QuavoStuntin', 'Braves', 'ajc',
#Hawaii
'hawaii','HawaiiNewsNow','Volcanoes_NPS',
#Idaho
'KTVB','IdahoPotato','KevinRichert',
#Illinois
'nprillinois', 'SenatorKirk', 'Cubs',
#Indiana
'Pacers', 'IndianaUniv', 'IndStatePolice',
#Iowa
'IowaPublicRadio', 'IowaGOPer ‏', 'iowadot',
#Kansas
'Royals', 'KansasCityKDOT', 'KCTV5',
#Kentucky
'RandPaul', 'UKCoachCalipari','WKYT',
#Louisiana
'BobbyJindal','theadvocatebr', 'JonathanWashamh',
#Maine
'PressHerald', 'chelliepingree', 'MaineDOT1',
#Maryland
'MartinOMalley', 'MdWeather', 'WTOPinMD',
#Massachusetts
'SenWarren', 'MassStatePolice', 'MittRomney',
#Michigan
'onetoughnerd', 'CoachJim4UM', 'AndreaBitely',
#Minnesota
'WCCO', 'MPRnews', 'edinacityman',
#Mississippi
'clarionledger', 'CoachDanMullen', 'MississippiDOT',
#Missouri
'GovJayNixon', 'MoGov', 'MoDOT',
#Montana
'mtpublicradio','NBCMontana', 'GovernorBullock',
#Nebraska
'NBCNebraska', 'CoachMiles', 'NECornBoard',
#Nevada
'SenatorReid', 'LasVegasSun', 'SteveSebelius',
#New Hampshire
'NewHampshireDOT', 'nhpr', '603facts',
#New Jersey
'corybooker', 'NJGOP', 'NJSP',
#New Mexico
'KOB4', 'NewMexicoOAG', 'ThinkNewMexico',
#New York
'nytimes', 'humansofny', 'ericbolling',
#North Carolina
'newsobserver', 'SenatorBurr', 'HarrisTeeter',
#North Dakota
'BismarckPolice', 'AP_NorthDakota', 'SenJohnHoeven',
#Ohio
'OhioState', 'JohnKasich', 'DispatchAlerts',
#Oklahoma
'OKDOT', 'NEWS9', 'StateImpactOK',
#Oregon
'OregonDOT', 'OregonGovBrown','Oregonian',
#Pennsylvania
'GovernorTomWolf', 'SeanFedorko', 'fox43',
#Rhode Island
'jonbouch','NBC10','GinaRaimondo',
#South Carolina
'MayorKnoxWhite','thestate','GrahamBlog',
#South Dakota
'PriceHP1','argusleader','johnthune',
#Tennessee
'Titans', 'TEN_GOP', 'tndp',
#Texas
'3lectric5heep','TexasObserver','ayanmittra',
#Utah
'abc4utah', 'GovHerbert','UtahDOT',
#Vermont
'SenSanders', 'VermontCynic','VTStatePolice',
#Virginia
'timkaine','DMVFollowers','pattonoswalt',
#Washington
'wsdot','SenatorCantwell', 'BillGates',
#West Virginia
'WestVirginiaU','WVGovernor','wchs8fox11',
#Wisconsin
'CityofManitowoc','WiStateJournal', 'SpartaWIPD',
#Wyoming
'WyomingPBS','wyomingpd', 'butterbob',
#Washington, DC
'BarackObama','realdonaldtrump','MurielBowser','AdamTuss'
]

import os

import codecs
import re


def unescape(s):
    s = s.replace("&lt;", "<")
    s = s.replace("&gt;", ">")
    # this has to be last:
    s = s.replace("&amp;", "&")
    s = s.replace("\n", " ")
    # replace lines
    s = re.sub(r'http\S*', 'link', s)
    return s


#import sys

#reload(sys)
#sys.setdefaultencoding('utf8')

file = codecs.open('output.txt', "w", "utf8")
#example of possible exclusions
for i in ids:

    statuses = api.GetUserTimeline(screen_name=i, exclude_replies=True, include_rts=False, count='1')
    for s in statuses:
        print(s)
        file.write(unescape(s.text) + "\n")

file.close()

print('harvest ended')