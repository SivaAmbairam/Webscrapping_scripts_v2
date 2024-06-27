import re

from module_package import *


def write_visited_log(url):
    with open(f'Visited_Fisher_urls.txt', 'a', encoding='utf-8') as file:
        file.write(f'{url}\n')


def read_log_file():
    if os.path.exists(f'Visited_Fisher_urls.txt'):
        with open(f'Visited_Fisher_urls.txt', 'r', encoding='utf-8') as read_file:
            return read_file.read().split('\n')
    return []


if __name__ == '__main__':
    timestamp = datetime.now().date().strftime('%Y%m%d')
    file_name = 'Fisher_products'
    all_data = []
    url = 'https://www.fishersci.com/us/en/browse/products'
    base_url = 'https://www.fishersci.com'
    headers = {
        'authority': 'www.fishersci.com',
        'method': 'GET',
        'path': '/us/en/home.html',
        'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        # 'Cookie': 'new_hf=true; new_cart=true; new_overlay=true; f_num=gmr; estore=estore-scientific; mdLogger=false; kampyle_userid=3cc8-fbfb-d62f-9006-dc00-3c93-3bdc-21c7; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_cookie_privacy=permit 1,2,3; s_vi=[CS]v1|330F088F363E0F9D-40001AC782A03632[CE]; s_ecid=MCMID%7C37161450081914606704547458763525740027; _gcl_au=1.1.1721032353.1713246496; QuantumMetricUserID=833703007cfee3fe1bd5ef1002d272d4; _hjSessionUser_341846=eyJpZCI6IjZlMzQ0MDQ1LWNkZTMtNWE1NS05YzczLTNhNTc2NDc1NzkxNSIsImNyZWF0ZWQiOjE3MTMyNDY0OTU2NjAsImV4aXN0aW5nIjp0cnVlfQ==; aam_uuid=40520749103498727913797215346890034770; WCXUID=35760512971517138714287; preventSingleResultRedirect=true; _gid=GA1.2.273275572.1714052867; locale=en_US; usertype=G; formSecurity=sv2cer9z3ul; akacd_FS_US_ProdA_Search_LucidWorks=3891575502~rv=10~id=1ff70e092d28aa94c023c341544a4939; AMCVS_8FED67C25245B39C0A490D4C%40AdobeOrg=1; AMCV_8FED67C25245B39C0A490D4C%40AdobeOrg=359503849%7CMCIDTS%7C19839%7CMCMID%7C37161450081914606704547458763525740027%7CMCAAMLH-1714727504%7C12%7CMCAAMB-1714727504%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1714129904s%7CNONE%7CMCAID%7C330F088F363E0F9D-40001AC782A03632%7CvVersion%7C5.0.1%7CMCCIDH%7C-1997303517; akacd_FS_Prod_AWS_EKS=3891575503~rv=70~id=78d608c4b1e6e7d51523efc10909b204; BIGipServerwww.fishersci.com_magellan_pool=1288357898.37919.0000; vcCookie=1; testTLD=test; WCXSID=00007737851171412270517166666666; userTypeDescription=guest; akacd_FS_Prod_AWS_EKS_Users=3891575503~rv=48~id=dc1fd6e52d24b3f40fdfb308193fcccc; memberId_AAM=; at_check=true; PFM=unsorted; accountId_AAM=Guest%20or%20No%20Account%20Chosen; com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId=com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId; bm_mi=A1B64201425E6D725F37E26F190F73BC~YAAQdDkgFzxaqBWPAQAAnwmtGRf3pU/gt8nqSvSytoynTAstbxQLcdnkVfrk/0OKxnml3vjgEntEWpB+M2XlBxZsM13g1AEyg9nuqwvUGjhDYuZMkc6z8L++DodS2lEV4/37mFfAVuY9b84NUVbJkVACBWH3RPqEICroDl0/k6EmjfIwIYc11l/tM7FM7bzwMx1V/DwdG8WB9YyKHIqIkX2sXTGSc1sLQRgYSqRTpKDiu+tCS3zuuoROAZQZUXR/30SG2C0raPkXlHfmic8ZPqauVPl2qvA5v6uK67s1LCpKHnd67qIzzzW1wGBBIbKB0VM4yyv31mecUGaNuEM=~1; WCXSID_expiry=1714123073316; TAsessionID=6bfaa024-0300-4019-8b07-e8294456460c|EXISTING; _hjSession_341846=eyJpZCI6Ijk2MGRmZTRjLWU4ZTUtNDRkZC1iYmJhLTZlYzUwMWYwYzc3NyIsImMiOjE3MTQxMjYyNjMwMzAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; s_days_since_new_s=Less than 1 day; dmdbase_cdc=DBSET; QuantumMetricSessionID=69d1356ac01e048f5f2e8fe90226cf63; adcloud={%22_les_v%22:%22c%2Cy%2Cfishersci.com%2C1714128068%22}; notice_behavior=implied,eu; new_quote=true; new_checkout=gmr; cmapi_gtm_bl=; s_days_since_new=1714126681820; s_pers=%20s_fid%3D14A195C2B6AD3030-11BBF514B556C1B0%7C1871012895376%3B%20gpv_pn%3Dhome%7C1714128482190%3B; _ga_TX98RX25ZK=GS1.1.1714126263.5.1.1714126682.58.0.0; _ga=GA1.1.573004469.1713246496; kampyleUserSession=1714126682365; kampyleUserSessionsCount=10; kampyleSessionPageCounter=1; mbox=PC#a38a87586d78400a8f67559b29c65b00.41_0#1777371483|session#5dc60f80a46b42d390f715ea7176ed40#1714128124; ak_bmsc=D8688914345F53570EFBDCDD4A60A8BB~000000000000000000000000000000~YAAQdDkgF8McqxWPAQAAwIXpGReAE0uBCMsGdjRMkKYoLDb7Bpm/MGhth0UXa5X0rpiduwas4Om5wZcOH9ZoUsbbmto+a2KxIV1n6Z/ivcaTFzAqpFxZ83PqvbuFoiedM76WvdCjZ6RplHHBLAeEgSrxSMposV19B48xF4XVC3Ot075eZTolInyS46J7mdk9Vkry9zKM21ECZwzU9x/0I25NUlHsolsbxk0m24YyemvQQIfRlfSjxkZ48FNO6k/UkcdM9hsel3dAcrAP3M7xlfSDixy7kYlMDEUsHl0FVkNALiaWswNPNKuusEECCjS9DdH/R2MpwaklmzCtkF6crZAeU2N97rMnyo0zU8GGi7RKeyc6nDG6n29jSrBnnESZBOTDZPqyxVi/X8aROFdJDhy7WU6LiVGwRisdh0LTQ8+sSnhG6JqKC2fjIkGe5fWJCcsmdpLfHs+zdcgO14SzVyfYs5GqpE0Ae3mTBYAo8Ys7mdSmnxO54R+cLataBsJQlLBk6O39kJC5ApG3/GaP3VI=; bm_sv=89AECBB20820FF8B2CA64B2B79139709~YAAQdDkgF8QcqxWPAQAAwIXpGReyb4SruJ82mMiMatFUEaN0LKBtB/wAZ3bw3nDA5Blf/H39K6tLCG/y99qHj8Y7ucAjrkx9h2bQ6KtZxEEEhXKZZ+EUQCXkalj1WGqcjL9UJ4X6Hah5z1i7LJubD/cxpft3t48o9Yex/uMBY0o4c049YXQ7btPGWAo5m0lgS+iR3HYeVQ7KNeYqdAxfIawmr7Q+7JeYvGYlbIu6RUJdNUcKGts4RRkJps3X5DD95FtmEg==~1; cto_bundle=OOIu2V9SeEo2c0E0U3owbW01NmJYUlNpQ0pMZHo2UHhSVnRsd0p2UHJveGJNRyUyRiUyRlZPWklJJTJGTVVNdHBaSnh4QVRTVDBxaUpLdCUyQlhIU3ZLeThnNHVOU0tveE41MWVaJTJCdmJ2cHQ5OWt4VEY2RDNIUk43bTkwcWlWcUd1RUtKMUdLZEVJSmgxUzhGRlVBam1XYUVKWlhTNGl4eFJZaVdMckdCakU1elFETVVSVWFTVmFCN3NkZ0VxSXoxWEljcko2RWV4Und6Zkg4R3JNTGx6TThBaXJMMFFsZEpFQSUzRCUzRA; s_sess=%20s_cc%3Dtrue%3B%20s_sq%3Dthermofisherfishersciprod%253D%252526pid%25253Dhome%252526pidt%25253D1%252526oid%25253D%2525250A%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%2525250A%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%25252520%252526oidt%25253D3%252526ot%25253DSUBMIT%3B',
        'Priority': 'u=0, i',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    cookies = {
        'new_hf': 'true',
        'new_cart': 'true',
        'new_overlay': 'true',
        'f_num': 'gmr',
        'estore': 'estore-scientific',
        'mdLogger': 'false',
        'kampyle_userid': '3cc8-fbfb-d62f-9006-dc00-3c93-3bdc-21c7',
        'notice_preferences': '2:',
        'notice_gdpr_prefs': '0,1,2:',
        'cmapi_cookie_privacy': 'permit 1,2,3',
        's_vi': '[CS]v1|330F088F363E0F9D-40001AC782A03632[CE]',
        's_ecid': 'MCMID%7C37161450081914606704547458763525740027',
        '_gcl_au': '1.1.1721032353.1713246496',
        'QuantumMetricUserID': '833703007cfee3fe1bd5ef1002d272d4',
        '_hjSessionUser_341846': 'eyJpZCI6IjZlMzQ0MDQ1LWNkZTMtNWE1NS05YzczLTNhNTc2NDc1NzkxNSIsImNyZWF0ZWQiOjE3MTMyNDY0OTU2NjAsImV4aXN0aW5nIjp0cnVlfQ==',
        'aam_uuid': '40520749103498727913797215346890034770',
        'WCXUID': '35760512971517138714287',
        'preventSingleResultRedirect': 'true',
        'prevMemberId.GUEST': 'undefined',
        'CART_ID': '16c3916e-94ac-4e98-8131-47fc46198795_2',
        'DECLINED_DATE': '1714647379337',
        'kampylePageLoadedTimestamp': '1715162627345',
        '_gid': 'GA1.2.746056097.1715507249',
        'akacd_FS_Prod_AWS_EKS': '3893204279~rv=24~id=d88e4250c6714331b5d1c6bbb24e0929',
        'locale': 'en_US',
        'usertype': 'G',
        'formSecurity': 'ixdw8mja1m',
        'TAsessionID': '54cb2866-d259-4fb6-8c59-25b6fed7a04e|EXISTING',
        's_days_since_new_s': 'Less than 1 day',
        'AMCVS_8FED67C25245B39C0A490D4C%40AdobeOrg': '1',
        'AMCV_8FED67C25245B39C0A490D4C%40AdobeOrg': '359503849%7CMCIDTS%7C19858%7CMCMID%7C37161450081914606704547458763525740027%7CMCAAMLH-1716356280%7C12%7CMCAAMB-1716356280%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1715758680s%7CNONE%7CMCAID%7C330F088F363E0F9D-40001AC782A03632%7CvVersion%7C5.0.1%7CMCCIDH%7C-1997303517',
        'userTypeDescription': 'guest',
        'akacd_FS_Prod_AWS_EKS_Users': '3893204281~rv=33~id=7396902e93e8870a47b473b67de1c4ba',
        'BIGipServerwww.fishersci.com_magellan_pool': '1271580682.37919.0000',
        'vcCookie': '1',
        '_hjSession_341846': 'eyJpZCI6ImI2MDM5MjMwLWUxY2YtNGI3ZS1hNGRmLWFjYTkzNDVlNDYzNyIsImMiOjE3MTU3NTE0ODEzNDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=',
        'akacd_FS_US_ProdA_Search_LucidWorks': '3893204280~rv=87~id=8ed31f9faa4de1ac94991577176bd1bf',
        'bm_mi': 'DF78605E7139C59170A8BECD83FEE192~YAAQdDkgFxJhqXePAQAAlfzBehejhy/jGCnx6zG+LpWMzU1HTg7iKr+c2sSKI5w1S6Pw3c1KBrja9Wn319g2T7o9jIJQ7+lcmYvEPYzhpIFtggjjGVJ2GQ/T7X9C3isCUWM/BdohMe+M751xqwSi+zCdEo3dsz8kep2KDL7BVYdzASiwaAey3EIGB5Ky8cwENaZhTtinPrY2gaCiXs/fMSIoLH5Unsqke6bz1QNcABJpXCnAJKWZDA4+txYO/mpTaXMzQXIIvJKOQMM8iu7kebWxwnAm0lu89jE8Pl4QbABg3imxbE1PodlF/DtlPRlDJO3Tre2qw8WYnxoAmWDZUKB+0WIhpEaP4a2l+ZnYPh+I0r0=~1',
        'PFM': 'unsorted',
        's_sess': '%20s_cc%3Dtrue%3B',
        'testTLD': 'test',
        'WCXSID': '00004997855171575148410466666666',
        'ak_bmsc': 'DFB8632143C5F30543B2597A36C95040~000000000000000000000000000000~YAAQdDkgFylhqXePAQAALAHCeheTSMfddTc72YCi8eAh6SxxvieSZEj6YVsVrOl/C/VAQgOwcCWVk8cyaYQyBfhAOLbOhqVZytihFBljZx4C34jPjzdDgzLOdgWlCZBzkpjfgXn97bowMkWOLqygzyx62VuGdRENLJXHAkIjmN2ud5FNruCwgUYdwr0pJZ46qn6sswYlNOatrfRSN5dcFrEHSEt6KX58sNB1oYrcphpd2Nt0WDQCadaj+xA2TRJpwQM2hhMGvpEbGNH4PN9u8FdfzTu/GUhCLiUjuQp6qcPMtlVeocGQRPR4rgQDqlcRcCf+ojio5z3gHh/VVKZ+r3Jc3wyEo/vQMJv1n6bNPNSwGts+Bz/yNi2KMKqbLNYwJABqvLxE3g6VOBJ3eL4OTG5BbTI8XyKqMaMSioyyRFtQ/R5Y7cuqyY3mk2z4tHOUebpbha08WVa8HZ5t7HDZS/boct2D9FlIDyaXFjVnte8Ddj0N6aO+QaCU12l/61lqlqoSmhmn4hINLw==',
        'memberId_AAM': '',
        'at_check': 'true',
        'dmdbase_cdc': 'DBSET',
        's_days_since_new': '1715751485919',
        'accountId_AAM': 'Guest%20or%20No%20Account%20Chosen',
        'kampyleUserSession': '1715751486354',
        'kampyleUserSessionsCount': '232',
        'kampyleSessionPageCounter': '1',
        'bm_sv': '471445F47CCFE8EA7417CFC5284C4009~YAAQdDkgF1ZhqXePAQAA/QnCehcwIXLnC7XIsBQOZneiFV/FJ3/Lf7wzSCQf7uhAWhsFQvspwv6jLyItWtdgb7u6mVJgSNtIaH+CxkaDLNM03Yh8d/TzxJ3R+xCQ2PYD0gpq6TmF7h07Pss6mOUFoZeSLaXvfYl2/4E4QwkYAL5VffcqugwdhbvPaYQpLf69DrbNwpyeMt0vqsUiG0n4Wo1omI0jD1xcZ1BCMLpGxcopGIO6+WG6uOq4aY4Tl/8jVyP3~1',
        'mbox': 'PC#a38a87586d78400a8f67559b29c65b00.41_0#1778996287|session#79d5b746d81745d280d2936a3a8efec0#1715753345',
        's_pers': '%20s_fid%3D14A195C2B6AD3030-11BBF514B556C1B0%7C1871012895376%3B%20gpv_pn%3D%253Aus%253Aen%253Abrowse%253A80013463%253Aamino-acids%7C1715753286545%3B',
        '_ga': 'GA1.1.573004469.1713246496',
        'WCXSID_expiry': '1715751487191',
        'adcloud': '{%22_les_v%22:%22c%2Cy%2Cfishersci.com%2C1715753287%22}',
        'cto_bundle': 'R9Hp3F9SeEo2c0E0U3owbW01NmJYUlNpQ0pFM3IyRlo2eVNZbXZ4WGRIOTNZWWpRQVpYUjJQeVp3QSUyRkhXTVA5NlBrdGNsdkxyT2Ztb0lhSHNoc3VWNGN3MElWQWR1QWNsUXJsVnZpV0JtWnVaYlU3ZTFEdVVxRTY3QkRSTE1EOG9ZNFRRd1RLNTJIN1lrdURtbXUzMWRoZjNJd2FuRW1mNHh4bkp5aG55dkFDQWV2MCUzRA',
        'com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId': 'com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId',
        'QuantumMetricSessionID': 'b52e0db45e28f6b633dc7a4259f25ee8',
        '_ga_TX98RX25ZK': 'GS1.1.1715751486.55.1.1715751929.60.0.0',
        'notice_behavior': 'implied,eu',
        'new_quote': 'true',
        'new_checkout': 'gmr',
        'cmapi_gtm_bl': '',
    }
    post_headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'new_hf=true; new_cart=true; new_overlay=true; f_num=gmr; estore=estore-scientific; mdLogger=false; kampyle_userid=3cc8-fbfb-d62f-9006-dc00-3c93-3bdc-21c7; notice_preferences=2:; notice_gdpr_prefs=0,1,2:; cmapi_cookie_privacy=permit 1,2,3; s_vi=[CS]v1|330F088F363E0F9D-40001AC782A03632[CE]; s_ecid=MCMID%7C37161450081914606704547458763525740027; _gcl_au=1.1.1721032353.1713246496; QuantumMetricUserID=833703007cfee3fe1bd5ef1002d272d4; _hjSessionUser_341846=eyJpZCI6IjZlMzQ0MDQ1LWNkZTMtNWE1NS05YzczLTNhNTc2NDc1NzkxNSIsImNyZWF0ZWQiOjE3MTMyNDY0OTU2NjAsImV4aXN0aW5nIjp0cnVlfQ==; aam_uuid=40520749103498727913797215346890034770; WCXUID=35760512971517138714287; preventSingleResultRedirect=true; prevMemberId.GUEST=undefined; CART_ID=16c3916e-94ac-4e98-8131-47fc46198795_2; DECLINED_DATE=1714647379337; kampylePageLoadedTimestamp=1715162627345; _gid=GA1.2.746056097.1715507249; akacd_FS_Prod_AWS_EKS=3893204279~rv=24~id=d88e4250c6714331b5d1c6bbb24e0929; locale=en_US; usertype=G; formSecurity=ixdw8mja1m; TAsessionID=54cb2866-d259-4fb6-8c59-25b6fed7a04e|EXISTING; s_days_since_new_s=Less than 1 day; AMCVS_8FED67C25245B39C0A490D4C%40AdobeOrg=1; AMCV_8FED67C25245B39C0A490D4C%40AdobeOrg=359503849%7CMCIDTS%7C19858%7CMCMID%7C37161450081914606704547458763525740027%7CMCAAMLH-1716356280%7C12%7CMCAAMB-1716356280%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1715758680s%7CNONE%7CMCAID%7C330F088F363E0F9D-40001AC782A03632%7CvVersion%7C5.0.1%7CMCCIDH%7C-1997303517; userTypeDescription=guest; akacd_FS_Prod_AWS_EKS_Users=3893204281~rv=33~id=7396902e93e8870a47b473b67de1c4ba; BIGipServerwww.fishersci.com_magellan_pool=1271580682.37919.0000; vcCookie=1; _hjSession_341846=eyJpZCI6ImI2MDM5MjMwLWUxY2YtNGI3ZS1hNGRmLWFjYTkzNDVlNDYzNyIsImMiOjE3MTU3NTE0ODEzNDgsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; akacd_FS_US_ProdA_Search_LucidWorks=3893204280~rv=87~id=8ed31f9faa4de1ac94991577176bd1bf; bm_mi=DF78605E7139C59170A8BECD83FEE192~YAAQdDkgFxJhqXePAQAAlfzBehejhy/jGCnx6zG+LpWMzU1HTg7iKr+c2sSKI5w1S6Pw3c1KBrja9Wn319g2T7o9jIJQ7+lcmYvEPYzhpIFtggjjGVJ2GQ/T7X9C3isCUWM/BdohMe+M751xqwSi+zCdEo3dsz8kep2KDL7BVYdzASiwaAey3EIGB5Ky8cwENaZhTtinPrY2gaCiXs/fMSIoLH5Unsqke6bz1QNcABJpXCnAJKWZDA4+txYO/mpTaXMzQXIIvJKOQMM8iu7kebWxwnAm0lu89jE8Pl4QbABg3imxbE1PodlF/DtlPRlDJO3Tre2qw8WYnxoAmWDZUKB+0WIhpEaP4a2l+ZnYPh+I0r0=~1; PFM=unsorted; s_sess=%20s_cc%3Dtrue%3B; testTLD=test; WCXSID=00004997855171575148410466666666; ak_bmsc=DFB8632143C5F30543B2597A36C95040~000000000000000000000000000000~YAAQdDkgFylhqXePAQAALAHCeheTSMfddTc72YCi8eAh6SxxvieSZEj6YVsVrOl/C/VAQgOwcCWVk8cyaYQyBfhAOLbOhqVZytihFBljZx4C34jPjzdDgzLOdgWlCZBzkpjfgXn97bowMkWOLqygzyx62VuGdRENLJXHAkIjmN2ud5FNruCwgUYdwr0pJZ46qn6sswYlNOatrfRSN5dcFrEHSEt6KX58sNB1oYrcphpd2Nt0WDQCadaj+xA2TRJpwQM2hhMGvpEbGNH4PN9u8FdfzTu/GUhCLiUjuQp6qcPMtlVeocGQRPR4rgQDqlcRcCf+ojio5z3gHh/VVKZ+r3Jc3wyEo/vQMJv1n6bNPNSwGts+Bz/yNi2KMKqbLNYwJABqvLxE3g6VOBJ3eL4OTG5BbTI8XyKqMaMSioyyRFtQ/R5Y7cuqyY3mk2z4tHOUebpbha08WVa8HZ5t7HDZS/boct2D9FlIDyaXFjVnte8Ddj0N6aO+QaCU12l/61lqlqoSmhmn4hINLw==; memberId_AAM=; at_check=true; dmdbase_cdc=DBSET; s_days_since_new=1715751485919; accountId_AAM=Guest%20or%20No%20Account%20Chosen; kampyleUserSession=1715751486354; kampyleUserSessionsCount=232; kampyleSessionPageCounter=1; bm_sv=471445F47CCFE8EA7417CFC5284C4009~YAAQdDkgF1ZhqXePAQAA/QnCehcwIXLnC7XIsBQOZneiFV/FJ3/Lf7wzSCQf7uhAWhsFQvspwv6jLyItWtdgb7u6mVJgSNtIaH+CxkaDLNM03Yh8d/TzxJ3R+xCQ2PYD0gpq6TmF7h07Pss6mOUFoZeSLaXvfYl2/4E4QwkYAL5VffcqugwdhbvPaYQpLf69DrbNwpyeMt0vqsUiG0n4Wo1omI0jD1xcZ1BCMLpGxcopGIO6+WG6uOq4aY4Tl/8jVyP3~1; mbox=PC#a38a87586d78400a8f67559b29c65b00.41_0#1778996287|session#79d5b746d81745d280d2936a3a8efec0#1715753345; s_pers=%20s_fid%3D14A195C2B6AD3030-11BBF514B556C1B0%7C1871012895376%3B%20gpv_pn%3D%253Aus%253Aen%253Abrowse%253A80013463%253Aamino-acids%7C1715753286545%3B; _ga=GA1.1.573004469.1713246496; WCXSID_expiry=1715751487191; adcloud={%22_les_v%22:%22c%2Cy%2Cfishersci.com%2C1715753287%22}; cto_bundle=R9Hp3F9SeEo2c0E0U3owbW01NmJYUlNpQ0pFM3IyRlo2eVNZbXZ4WGRIOTNZWWpRQVpYUjJQeVp3QSUyRkhXTVA5NlBrdGNsdkxyT2Ztb0lhSHNoc3VWNGN3MElWQWR1QWNsUXJsVnZpV0JtWnVaYlU3ZTFEdVVxRTY3QkRSTE1EOG9ZNFRRd1RLNTJIN1lrdURtbXUzMWRoZjNJd2FuRW1mNHh4bkp5aG55dkFDQWV2MCUzRA; com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId=com.ibm.commerce.ubx.idsync.DSPID_ADOBE%2CaaUserId%2CmcId%2Cx1VisitorId; QuantumMetricSessionID=b52e0db45e28f6b633dc7a4259f25ee8; _ga_TX98RX25ZK=GS1.1.1715751486.55.1.1715751929.60.0.0; notice_behavior=implied,eu; new_quote=true; new_checkout=gmr; cmapi_gtm_bl=',
        'origin': 'https://www.fishersci.com',
        'priority': 'u=1, i',
        'referer': 'https://www.fishersci.com/shop/products/methyl-red-acs-2/AA3668214',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-b3-traceid': '3b5ea14e442c5575e1481f2c1ccb79f1',
        'x-requested-with': 'XMLHttpRequest',
    }
    soup = get_soup(url, headers)
    all_products = soup.find_all('div', class_='category_group list_group collapsible')
    for single_products in all_products:
        '''PRODUCT_CATEGORY'''
        product_category = single_products.find('span', class_='filter_heading_name').text.strip()
        inner_href = single_products.find_all('a', class_='')
        for single_href in inner_href:
            product_sub_category = single_href.text.strip()
            href_split = str(single_href).split('/browse/', 1)[-1].split('/', 1)[0].strip()
            main_url = f'{base_url}{single_href["href"]}'
            print(f'main_url---------->{main_url}')
            if main_url in read_log_file():
                continue
            inner_request = get_soup(main_url, headers)
            if inner_request is None:
                continue
            if inner_request.find('h3', class_='result_title'):
                '''PAGINATION'''
                page_content = strip_it(inner_request.find('div', class_='results_count').text.replace('results', '').replace(',', ''))
                for i in range(1, int(math.ceil(int(page_content.split('of', 1)[-1].strip()) / int(page_content.split('of', 1)[0].split('–', 1)[-1].strip()))) + 1):
                    page_link = f'{main_url}?categoryKey={href_split}&page={i}'
                    page_soup = get_soup(page_link, headers)
                    if page_soup is None:
                        continue
                    content_url = page_soup.find_all('h3', class_='result_title')
                    for single_url in content_url:
                        product_url = f'{base_url}{single_url.a["href"]}'
                        print(product_url)
                        product_request = get_soup(product_url, headers)
                        if product_request is None:
                            continue
                        if product_request.find('table', class_='general_table product_table responsive_product_table'):
                            other_content = product_request.find('table', class_='general_table product_table responsive_product_table').find_all('tbody', class_='itemRowContent')
                            for single_content in other_content:
                                '''PRODUCT URL'''
                                product_url = f'{base_url}{single_content.find('a', class_='chemical_fmly_glyph')['href']}'
                                print(product_url)
                                '''PRODUCT ID'''
                                try:
                                    product_id = strip_it(single_content.find('a', class_='chemical_fmly_glyph').text)
                                except:
                                    product_id = ''
                                if product_id in read_log_file():
                                    continue
                                '''PRODUCT NAME'''
                                try:
                                    if product_request.find('h1', id='qa_product_description'):
                                        main_name = product_request.find('h1', id='qa_product_description').text.strip()
                                    elif product_request.find('h1', id='item_header_text'):
                                        main_name = product_request.find('h1', id='item_header_text').text.strip()
                                    else:
                                        main_name = ''
                                except:
                                    main_name = ''
                                try:
                                    extract_content = single_content.find('td', attrs={'data-title': 'Price'}).extract()
                                    inner_extract = single_content.find('td', attrs={'data-title': 'Qty'}).extract()
                                    other_extract = single_content.find('td', attrs={'data-type': 'addtocart'}).extract()
                                except:
                                    extract_content = ''

                                if single_content.find('td', attrs={'data-title': re.compile('.*?')}):
                                    title_list = []
                                    title_content = single_content.find_all('td',  attrs={'data-title': re.compile('.*?')})
                                    for single_title in title_content:
                                        title_text = strip_it(single_title.text.strip())
                                        title_list.append(title_text)
                                    product_names = ', '.join(title_list)
                                    if main_name in product_names:
                                        product_name = product_names
                                    else:
                                        product_name = f'{main_name}, {product_names}'
                                else:
                                    product_name = main_name
                                product_request = get_soup(product_url, headers)
                                if product_request is None:
                                    continue
                                '''DESCRIPTION'''
                                try:
                                    desc = product_request.find('div', class_='small-12 medium-12 large-12 columns')
                                    desc_replace = str(desc).replace('<li', '• <li').replace('Description', '')
                                    product_desc = strip_it(BeautifulSoup(desc_replace, 'html.parser').text.strip())
                                except:
                                    product_desc = ''
                                '''IMAGE URL'''
                                try:
                                    fisher_image_url = product_request.find('img', id='productImage')['src']
                                except:
                                    fisher_image_url = ''
                                '''OFFERS'''
                                if product_request.find('span', attrs={'itemprop': 'offers'}):
                                    '''PRODUCT PRICE'''
                                    try:
                                        product_price = f'$ {strip_it(product_request.find('span', attrs={'itemprop': 'offers'}).find('span', itemprop='price')['content'].strip())}'
                                    except:
                                        product_price = ''
                                    '''PRODUCT QUANTITY'''
                                    try:
                                        if product_price == '':
                                            product_quantity = ''
                                        else:
                                            product_quantity = strip_it(product_request.find('span', attrs={'itemprop': 'offers'}).find('span', itemprop='unitText')['content'].replace('Each of 1', '1').replace('Each', '1').replace('Case of', '').replace('Pack of', '').replace('EA', '').strip())
                                            product_quantity = re.search('\\d+', str(product_quantity)).group()
                                    except:
                                        product_quantity = ''
                                else:
                                    '''PRODUCT PRICE'''
                                    try:
                                        product_price = f'$ {strip_it(product_request.find('span', itemprop='price')['content'].strip())}'
                                    except:
                                        product_price = ''
                                    '''PRODUCT QUANTITY'''
                                    try:
                                        if product_price == '':
                                            product_quantity = ''
                                        else:
                                            product_quantity = strip_it(product_request.find('span', itemprop='price').find('span', itemprop='unitText')['content'].replace('Each of 1', '1').replace('Each', '1').replace('Case of', '').replace('Pack of', '').strip())
                                            if re.search('\\d+', str(product_quantity)).group():
                                                product_quantity = re.search('\\d+', str(product_quantity)).group()
                                            else:
                                                product_quantity = 1
                                    except:
                                        product_quantity = ''
                                print('current datetime------>', datetime.now())
                                dictionary = {
                                    'Fisher_product_category': product_category,
                                    'Fisher_product_sub_category': product_sub_category,
                                    'Fisher_product_id': product_id,
                                    'Fisher_product_name': product_name,
                                    'Fisher_product_quantity': product_quantity,
                                    'Fisher_product_price': product_price,
                                    'Fisher_product_url': product_url,
                                    'Fisher_image_url': fisher_image_url,
                                    'Fisher_product_desc': product_desc
                                }
                                articles_df = pd.DataFrame([dictionary])
                                articles_df.drop_duplicates(subset=['Fisher_product_id', 'Fisher_product_name'], keep='first',
                                                            inplace=True)
                                if os.path.isfile(f'{file_name}.csv'):
                                    articles_df.to_csv(f'{file_name}.csv', index=False, header=False, mode='a')
                                else:
                                    articles_df.to_csv(f'{file_name}.csv', index=False)
                                write_visited_log(product_id)
                        else:
                            '''DESCRIPTION'''
                            try:
                                desc = product_request.find('div', class_='small-12 medium-12 large-12 columns')
                                desc_replace = str(desc).replace('<li', '• <li').replace('Description', '')
                                product_desc = strip_it(BeautifulSoup(desc_replace, 'html.parser').text.strip())
                            except:
                                product_desc = ''
                            '''IMAGE URL'''
                            try:
                                fisher_image_url = product_request.find('img', id='productImage')['src']
                            except:
                                fisher_image_url = ''
                            product_content = product_request.find('div', id='ProductDescriptionContainer')
                            '''PRODUCT NAME'''
                            try:
                                product_name = strip_it(product_content.find('h1', id='item_header_text').text.strip())
                            except:
                                product_name = ''
                            product_id = ''
                            product_price = ''
                            product_quantity = ''
                            if product_request.find('span', class_='part_number_container hide_in_tablet hide_in_desktop'):
                                product_id = product_request.find('span', class_='part_number_container hide_in_tablet hide_in_desktop').text.replace('Catalog Number', '').strip()
                                data = {
                                    'partNumber': f'{product_id}',
                                    'callerId': 'products-ui-single-page',
                                }
                                response = requests.post('https://www.fishersci.com/shop/products/service/pricing',
                                                         cookies=cookies, headers=post_headers, data=data)
                                soup_json = json.loads(response.content)
                                if soup_json is None:
                                    continue
                                data = soup_json['priceAndAvailability'][f'{product_id}']
                                for datas in data:
                                    product_price = datas['price']
                                    product_quantity = datas['quantity']
                            else:
                                '''PRODUCT ID'''
                                try:
                                    product_id = strip_it(product_content.find('p', class_='rightProductCode').span.text)
                                except:
                                    product_id = ''
                                '''OFFERS'''
                                if product_content.find('span', attrs={'itemprop':'offers'}):
                                    '''PRODUCT PRICE'''
                                    try:
                                        product_price = f'$ {strip_it(product_content.find('span', attrs={'itemprop':'offers'}).find('span', itemprop='price')['content'].strip())}'
                                    except:
                                        product_price = ''
                                    '''PRODUCT QUANTITY'''
                                    try:
                                        if product_price == '':
                                            product_quantity = ''
                                        else:
                                            product_quantity = strip_it(product_content.find('span', attrs={'itemprop':'offers'}).find('span', itemprop='unitText')['content'].replace('Each of 1', '1').replace('Each', '1').replace('Case of', '').replace('Pack of', '').replace('EA', '').strip())
                                            product_quantity = re.search('\\d+', str(product_quantity)).group()
                                    except:
                                        product_quantity = ''
                                else:
                                    '''PRODUCT PRICE'''
                                    try:
                                        product_price = f'$ {strip_it(product_content.find('span', itemprop='price')['content'].strip())}'
                                    except:
                                        product_price = ''
                                    '''PRODUCT QUANTITY'''
                                    try:
                                        if product_price == '':
                                            product_quantity = ''
                                        else:
                                            product_quantity = strip_it(product_content.find('span', itemprop='price').find('span', itemprop='unitText')['content'].replace('Each of 1', '1').replace('Each', '1').replace('Case of', '').replace('Pack of', '').strip())
                                            product_quantity = re.search('\\d+', str(product_quantity)).group()
                                    except:
                                        product_quantity = ''
                            if product_id in read_log_file():
                                continue
                            print('current datetime------>', datetime.now())
                            dictionary = {
                                'Fisher_product_category': product_category,
                                'Fisher_product_sub_category': product_sub_category,
                                'Fisher_product_id': product_id,
                                'Fisher_product_name': product_name,
                                'Fisher_product_quantity': product_quantity,
                                'Fisher_product_price': product_price,
                                'Fisher_product_url': product_url,
                                'Fisher_image_url': fisher_image_url,
                                'Fisher_product_desc': product_desc
                            }
                            articles_df = pd.DataFrame([dictionary])
                            articles_df.drop_duplicates(subset=['Fisher_product_id', 'Fisher_product_name'], keep='first',
                                                        inplace=True)
                            if os.path.isfile(f'{file_name}.csv'):
                                articles_df.to_csv(f'{file_name}.csv', index=False, header=False, mode='a')
                            else:
                                articles_df.to_csv(f'{file_name}.csv', index=False)
                            write_visited_log(product_id)
            write_visited_log(main_url)

