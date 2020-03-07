import urllib.request as req
import bs4 #BeautifulSoup

url = "https://www.flipkart.com/wearable-smart-devices/pr?sid=all&p[]=facets.serviceability%5B%5D%3Dtrue&offer=nb:mp:029b565b04&fm=neo%2Fmerchandising&iid=M_1ef992e7-1231-43ad-85f2-45d788163f00_3.IY67JVS8T909&ssid=a62toe5crk0000001583562397004&otracker=hp_omu_Deals%2Bof%2Bthe%2BDay_1_3.dealCard.OMU_Deals%2Bof%2Bthe%2BDay_IY67JVS8T909_2&otracker1=hp_omu_SECTIONED_neo%2Fmerchandising_Deals%2Bof%2Bthe%2BDay_NA_dealCard_cc_1_NA_view-all_2&cid=IY67JVS8T909"
#url = "https://www.google.com/search?sxsrf=ALeKk0230HEZkJlawIsTU0ZaLXCKUfT--A%3A1583562600703&ei=aD9jXtTGKtOvyAOb7LnQAw&q=baaghi+3&oq=baagh&gs_l=psy-ab.3.0.0i131l10.1054.7149..8096...4.2..1.619.2426.2-6j1j0j1......0....1..gws-wiz.....10..0i71j35i39j0i131i67j0i67j0j35i362i39j35i39i70i249j0i273.fPm_NzynK9U"
response = req.urlopen(url)
#print(response)

htmlPage = bs4.BeautifulSoup(response, 'lxml')

#a_tag = htmlPage.find('a', '_2cLu-l')

a_tag_list = htmlPage.find_all('a', '_2cLu-l')

#print(a_tag['title'])

#<a ..........title =" abcd"  >   Some data    </a>

#print(a_tag.text)

for a_tag in a_tag_list:
    print(a_tag.text)
