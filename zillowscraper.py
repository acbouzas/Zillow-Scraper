import requests
import pandas as pd
import json
from ipdb import set_trace

def get_zillow_data():
    url = "https://www.zillow.com/search/GetSearchPageState.htm"

    querystring = {
        "searchQueryState": "{\"pagination\":{},\"usersSearchTerm\":\"TX\",\"mapBounds\":{\"west\":-112.93084640624998,\"east\":-87.22283859374998,\"south\":27.852469056070166,\"north\":34.66374447603762},\"mapZoom\":6,\"regionSelection\":[{\"regionId\":54,\"regionType\":2}],\"isMapVisible\":true,\"filterState\":{\"isAllHomes\":{\"value\":true},\"sortSelection\":{\"value\":\"globalrelevanceex\"}},\"isListVisible\":true}",
        "wants": "{\"cat1\":[\"mapResults\"]}",
        "requestId": "2"
    }

    payload = ""
    headers = {
        "cookie": '"AWSALB=vbVwJJz%2FklYvWleyEbK6R52JaI5M1NJ89DXwN589PPL%2BHdxViK6e4Xj7ZG7%2BinkmqWAXBnTrgbUbpsULsiLnAgiKAYWPYO3%2BgJuUibg4kwR4Q3HRiOuwATbr%2Fw59; AWSALBCORS=vbVwJJz%2FklYvWleyEbK6R52JaI5M1NJ89DXwN589PPL%2BHdxViK6e4Xj7ZG7%2BinkmqWAXBnTrgbUbpsULsiLnAgiKAYWPYO3%2BgJuUibg4kwR4Q3HRiOuwATbr%2Fw59; search=6%7C1689198115584%257Crect%253D34.66374447603762%25252C-87.22283859374998%25252C27.852469056070166%25252C-112.93084640624998%2526rid%253D54%2526disp%253Dmap%2526mdm%253Dauto%2526p%253D1%2526z%253D1%2526listPriceActive%253D1%2526fs%253D1%2526fr%253D0%2526mmm%253D0%2526rs%253D0%2526ah%253D0%2526singlestory%253D0%2526housing-connector%253D0%2526abo%253D0%2526garage%253D0%2526pool%253D0%2526ac%253D0%2526waterfront%253D0%2526finished%253D0%2526unfinished%253D0%2526cityview%253D0%2526mountainview%253D0%2526parkview%253D0%2526waterview%253D0%2526hoadata%253D1%2526zillow-owned%253D0%25263dhome%253D0%2526featuredMultiFamilyBuilding%253D0%2526commuteMode%253Ddriving%2526commuteTimeOfDay%253Dnow%2509%250954%2509%2509%2509%2509%2509%2509; JSESSIONID=06806A5298F1CD6E4BC63300337738CC; zguid=24%7C%252443e7c5bb-c94f-4926-a010-17226e783e0b; zgsession=1%7Ccd87f749-cd29-44ce-96f6-88bd9ad115de"',
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Cookie": '"zguid=24|%2475e22ba2-3335-4c89-ba0f-33751d0ed30c; zgsession=1|cf5fbad7-3744-4512-83ae-23a1cee50772; _ga=GA1.2.1574531640.1686600777; _gid=GA1.2.1468507049.1686600777; _gcl_au=1.1.724311443.1686600778; DoubleClickSession=true; _hp2_id.1215457233=%7B%22userId%22%3A%228541318438097936%22%2C%22pageviewId%22%3A%226112375597325420%22%2C%22sessionId%22%3A%22715339850241011%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; zjs_anonymous_id=%2275e22ba2-3335-4c89-ba0f-33751d0ed30c%22; zjs_user_id=null; zg_anonymous_id=%223e326971-bc64-4a3c-946a-46a8a1d386ab%22; pxcts=202facbe-095d-11ee-9397-4b4850466b59; _pxvid=202f9fd3-095d-11ee-9397-6f2a0866a97e; _px3=7e855bf0c732c97e0d50bd3c258dd75de4d4b09bfe3b30adacbd0c2f84b73eb1:wCu5dki6pERlFazqBMgpoySN7ey2OOwtwDoN92B4q9U61qI0cWi3EYRw0x5RWeKukstFw5I6TTdX/Gb3M3jXsg==:1000:S+UQ2j+EXHrPIXnzPUK+gYZCd/26sNMoBxT51OF2HFUm0Mdh+GX2buqO8bKA8smUxtQ3ZhfY8ytyYiu8lqgTMm30kpPwcLLb4sXhECTwn9QjF6kEDXKLaTYN9CSr+OhHA2sUiJCCUJj6gwbGBEtuFrA5BiftS8QUY+FMv7vR1cGlGpI3US/IewWtvjpq348d12iSRYESsPA5yhvK2tUjlw==; __pdst=a5bab507f4024427a06f850c0c2cac9c; _pin_unauth=dWlkPVlqSTFPV0U0T0dRdE56VTJZUzAwTTJSbExUaGlPVFF0TVdVeE1XWXlZVGRsTnpWaQ; _clck=1cpzeh4|2|fce|0|1258; _fbp=fb.1.1686600781497.1274990582; _clsk=1wezys1|1686606091290|15|0|o.clarity.ms/collect; g_state={"i_p":1686607982596,"i_l":1}; AWSALB=Vh0aAy4hVEbDa+VR6oe59sE2SBo9o2AIEyPHv2MiGAg/cXKVPJiYpEZJCKWMBzba6FbtRoSuT7lfWlqwrs3FCrUhyU+QqDkyNTNe3h4GJ31aS5VUsysmjhsBMYcV; AWSALBCORS=Vh0aAy4hVEbDa+VR6oe59sE2SBo9o2AIEyPHv2MiGAg/cXKVPJiYpEZJCKWMBzba6FbtRoSuT7lfWlqwrs3FCrUhyU+QqDkyNTNe3h4GJ31aS5VUsysmjhsBMYcV; JSESSIONID=E4F3754F5FDF28C8043E244309228AD7; search=6|1689197952703%7Cregion%3Dtx%26rb%3DTX%26rect%3D36.500704%252C-93.508039%252C25.837164%252C-106.645646%26disp%3Dmap%26mdm%3Dauto%26listPriceActive%3D1%26fs%3D1%26fr%3D0%26mmm%3D1%26rs%3D0%26ah%3D0%09%0954%09%09%09%09%09%09; __gads=ID=0cbdaf51e37382e7:T=1686600625:RT=1686605837:S=ALNI_MaSImYoYa3Z3Gbt9fGG-vUG6eehEw; __gpi=UID=0000057b720043e8:T=1686600625:RT=1686605837:S=ALNI_MbcZXHnyadl6KavspMBlg42_x79cg; tfpsi=99ca83b3-7260-493e-9e2a-8e2932d36a56; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; _hp2_ses_props.1215457233=%7B%22ts%22%3A1686606010623%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; _gat=1; _uetsid=87784da0095d11eeae74079e3d743b11; _uetvid=87786a10095d11eea5040f72cacdfd1e"',
    #    "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }
    response = requests.get(url, data=payload, headers=headers, params=querystring)
    response.raise_for_status()

    content = response.text
    data = json.loads(content)

    return data

def extract_listings_data(data):
    cat1 = data['cat1']['searchResults']
    map_results = cat1['mapResults']

    results = []
    for listing in map_results:
        try:
            hdp = listing['hdpData']
            home_info = hdp['homeInfo']
        except KeyError:
            continue

        item = {
            'price': home_info['price'],
            'latitude': home_info['latitude'],
            'longitude': home_info['longitude'],
            'homeStatus': home_info['homeStatus'],
            'zestimate': home_info.get('zestimate', ''),
            'rentZestimate': home_info.get('rentZestimate', ''),
            'detailUrl': listing['detailUrl'],
            'address': listing['address']
        }

        results.append(item)

    return results

def save_data_to_csv(data, filename):
    df = pd.DataFrame(data)
    set_trace()
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    zillow_data = get_zillow_data()
    listings_data = extract_listings_data(zillow_data)
    save_data_to_csv(listings_data, "scraped_data.csv")