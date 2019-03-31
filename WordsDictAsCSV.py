from bs4 import BeautifulSoup
import requests
from nltk.corpus import stopwords
import csv


def parse(site):
    # extracts substantial words as a list from a webpage

    try:
        url = requests.get(str(site)).text
        soup = BeautifulSoup(url, features='html.parser')
        for script in soup (["script", "style"]):
            script.extract()
        soup = soup.text.split()
        remove = set(stopwords.words('english'))
        [soup.remove(word) for word in soup if word in remove]
        soup = [word.lower() for word in soup]
        print(len(soup))
        return soup
    except:
        return

def relatedLinks(site):
    '''extracts substantial, English words as a list from all pages
    from a website including any other urls listed on the website'''

    try:
        englishDictionary = parse('http://www-personal.umich.edu/~jlawler/wordlist')
        url = requests.get(site)
        html_doc = url.text
        soup = BeautifulSoup(html_doc, features='html.parser')
        a_tags = soup.find_all('a')

        links = [site]
        for link in a_tags:
            links = links + [link.get('href')]
        print('Number of pages visited: ' + str(len(links)))

        wordlist = []
        for link in links:
            try:
                words = parse(link)
                wordlist = wordlist + words
            except:
                continue
        t = []
        [t.append(word) for word in wordlist if word in englishDictionary]
        return t
    except:
        return
groupDict = {'Causa': 'https://causaoregon.org', 'Chemawa': 'https://chemawa.bie.edu', 'ChemeketaMulticultural': 'https://www.chemeketa.edu/aboutchemeketa/collegelife/multicultural/', 'COFA': 'https://cann.us/', 'FACESofAmerica': 'http://www.facesofamercia.org', 'GreaterSalemFilipino': 'https://gsfaa.com/', 'INDUS': 'http://www.salemindus.org', 'JapaneseCulturalSociety': 'https://www.oregonjcs.org/', 'LatinoBusinessAlliance': 'http://latinobizalliance.com', 'LatinosUnidosSiempre': 'https://www.facebook.com/LatinosunidossiempreSalem/', 'ManoaMano': 'http://manoamanofc.org/', 'MicronesianIslander': 'http://www.micoregon.org/', 'NAACPSalem': 'http://www.sknaacp1166.org/', 'OregonBlackPioneers': 'http://www.oregonblackpioneers.org/blog/', 'OregonMarshallese': 'https://www.facebook.com/groups/OregonMarshalleseCommunity/', 'RacialJusticeCommunitte': 'https://www.facebook.com/groups/150645702008503/', 'SalemChineseAcademy': 'http://www.salemchineseacademy.org/', 'SalemForRefugees': 'http://salemforrefugees.org', 'SalemCoalitionforEquality': 'https://skcequality.org/', 'GrandRonde': 'https//www.grandronde.org', 'USAAcademyOnline': 'http://usaacademyonline.org/cgi-sys/suspendedpage.cgi', 'WillametteMulticultural': 'http://willamette.edu/offices/oma/index.html', 'WorldBeatSalem': 'https://www.worldbeatfestival.org', 'VietnameseVoice': 'http://vvsinoregon.blogspot.com/', 'Vozhispana': 'https://www.facebook.com/VozdelInmigranteLatinoenOregon/', 'BahaiWorldFaith': 'http://www.bahaisofsalem.org/', 'CHABAD': 'https://jewishsalem.com/', 'ChineseEvangelicalChurch': '', 'KoreanChurch': 'https://www.facebook.com/pages/Korean-Church-of-Salem/118530614825832?hc_ref=ARSNiXT1xGAeaqROMT61dX5OseSE_MI34P_Tlzo__THCKZqQQ90aJDhAgwIFy0nh4PI', 'DasmeshDarbarSikh': 'http://salemgurdwara.com/', 'PastorsofToGodbetheGlory': '', 'SalemIslamicCenter': 'https://www.facebook.com/MuslimsofSalem/', 'SalemLeadershipFoundation': 'https://www.salemlf.org/', 'SikhSevaNorthwest': '', 'TempleBethShalom': 'http://tbsholom.org/', 'UnitarianUniversalist': 'https://uusalem.org/', 'AlliesforEquality': 'http://alznet.org/', 'AssociationUniversityWomen': 'http://salem-or.aauw.net/', 'BasicRightsOregon': 'http://www.basicrights.org', 'CapitolPride': 'https://www.capitolpride.org/', 'GenderSexualitySafeChemeketa': 'http://ccctriangleclub.weebly.com/', 'ImperialCourtWillamette': 'https://iscwe.wordpress.com/', 'RainbowYouth': 'http://rainbowyouth.org', 'SalemGayLesbianHotline': '', 'SocialJusticeCollective': 'https://salemsjc.wordpress.com', 'AlzheimersNetwork': 'http://alznet.org/', 'Center50': 'http://www.cityofsalem.net/seniors', 'GovernorsCommissionSenior': 'http://www.oregon.gov/DHS/SENIORS-DISABILITIES/ADVISORY/GCSS/Pages/index.aspx', 'ARCMarionCounty': '', 'AccessTechnologies': 'https://www.accesstechnologiesinc.org/', 'DisabilityRights': 'https://droregon.org/', 'EasterSealsOregon': 'http://www.easterseals.com/oregon/?referrer=http://es.easterseals.com/site/PageServer?pagename=ORDR_locations', 'GartenServices': 'http://www.garten.org/', 'NorthwestSeniorDisabilities': 'http://www.nwsds.org/', 'OregonCommissionBlind': 'http://www.oregon.gov/blind/Pages/index.aspx', 'OregonAssociationDeaf': 'http://www.oad1921.org', 'OregonSchoolDeaf': 'http://www.osd.k12.or.us/', 'ShangriLa': 'http://www.shangrilacorp.org', 'DHS': 'http://www.oregon.gov/DHS/assistance/Pages/index.aspx', 'CommunityActionAgency': 'https://www.ssa.gov/', 'SalemforAll': 'https://salemforall.org/', 'CenterHopeSafety': 'https://www.mvwcs.com/', 'FellowshipReconciliation': 'https://www.facebook.com/SALEM-Fellowship-of-Reconciliation-1382120305376827/', 'LeagueWomenVoters': 'http://lwvmarionpolk.org/', 'NWHumanServices': 'http://www.northwesthumanservices.org', 'NeighborhoodAssociations': 'https://www.cityofsalem.net/my-neighborhood', 'OregoniansPeace': 'https://www.facebook.com/oregoniansforpeace/', 'HomelessCoalition':'', 'OnenessCoalition': 'https://www.facebook.com/The-Oneness-Coalition-255373187899504/', 'UnitedNationsAssociation':''}

for k, v in groupDict.items():
    # creates dictionary for each group and saves it to a file as csv with seperate subfolder and file for each group

    try:
        print(k)
        data = relatedLinks(v)
        dictionary = {key:data.count(key) for key in data}

        print(dictionary)

        with open(k + 'wordsDict.csv', 'w', newline='') as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['Word', 'Frequency', 'DictionaryWebsite'])
            for ke, va in dictionary.items():
                thewriter.writerow([ke, va, 'https://www.merriam-webster.com/dictionary/' + ke])

    except:
        continue