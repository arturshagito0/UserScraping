from dataframe_api import save_to_google_drive, populate_dataframe, create_new_spreadsheet, update_spreadsheet
import json
import numpy as np
import requests
import string
import time
import pandas as pd

headers_users = {
    'authority': 'www.linkedin.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-restli-protocol-version': '2.0.0',
    'dnt': '1',
    'x-li-lang': 'en_US',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'x-li-page-instance': 'urn:li:page:d_flagship3_groups_members;oT92kslcQROBVV0+qRK6mQ==',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'csrf-token': 'ajax:5514574330745441635',
    'x-li-track': '{"clientVersion":"1.9.7586","mpVersion":"1.9.7586","osName":"web","timezoneOffset":0,"timezone":"UTC","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.linkedin.com/groups/35222/members/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'bcookie="v=2&f457616b-52cc-43eb-8e90-23ec38ea8e86"; bscookie="v=1&20211209170108357be425-a454-435b-8ca7-9551fa4ffca6AQGVosJ8KTyHxfgZXF9tDWm4S3Wmpceo"; li_gc=MTswOzE2MzkwNjkyNjg7MjswMjEx78wVbKoosovs1b+4nHWpjYV+JqxOwxRQu9ePeYR43w==; li_alerts=e30=; g_state={"i_p":1639076487900,"i_l":1}; li_rm=AQFQMJ4yEoLSDwAAAX2gJIimwD7K6Hv2DTulPWxxzatwJ0_CGRTcLtinpdhEeuBlO7bF_jftEgBKRjUw6RwaCdvOEhIyL-WSprF_nzxwDIBSqGux_RLv46Dy; li_at=AQEDASw3s0MAw6ohAAABfaAkjsMAAAF9xDESw00ANWCAkZdc3rAAHaydJaHx6FBsQyH_MrJ1eEDuddY8eoGERED9p_UDY4W9EfCZj_gjIsYCEUJJNCuOz_afXi6CRJS590uyB4V6EBCF64sf43O9UGby; liap=true; JSESSIONID="ajax:5514574330745441635"; lang=v=2&lang=en-us; li_mc=MTsyMTsxNjM5MDY5MjkwOzI7MDIx0hulJPhi7pbZalMiFFUyG2IbxNNJv9jMhHXTw3kQ6EU=; lidc="b=OB75:s=O:r=O:a=O:p=O:g=2524:u=13:x=1:i=1639069290:t=1639148875:v=2:sig=AQEBJAatC3G98pvh--ddg-YLp3-cGYi7"; timezone=UTC; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18971%7CMCMID%7C22952632177093777836618679733005828475%7CMCOPTOUT-1639076494s%7CNONE%7CvVersion%7C5.1.1',
    'sec-gpc': '1',
}
headers_location = {
    'authority': 'www.linkedin.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-restli-protocol-version': '2.0.0',
    'dnt': '1',
    'x-li-lang': 'en_US',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;yMzD4o7yS4axRYbSVefQng==',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'csrf-token': 'ajax:7943871578965923745',
    'x-li-track': '{"clientVersion":"1.9.7860","mpVersion":"1.9.7860","osName":"web","timezoneOffset":0,"timezone":"UTC","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.linkedin.com/groups/35222/members/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'bcookie="v=2&f457616b-52cc-43eb-8e90-23ec38ea8e86"; bscookie="v=1&20211209170108357be425-a454-435b-8ca7-9551fa4ffca6AQGVosJ8KTyHxfgZXF9tDWm4S3Wmpceo"; li_gc=MTswOzE2MzkwNjkyNjg7MjswMjEx78wVbKoosovs1b+4nHWpjYV+JqxOwxRQu9ePeYR43w==; li_alerts=e30=; g_state={"i_p":1639076487900,"i_l":1}; li_rm=AQFQMJ4yEoLSDwAAAX2gJIimwD7K6Hv2DTulPWxxzatwJ0_CGRTcLtinpdhEeuBlO7bF_jftEgBKRjUw6RwaCdvOEhIyL-WSprF_nzxwDIBSqGux_RLv46Dy; li_at=AQEDASw3s0MAw6ohAAABfaAkjsMAAAF9xDESw00ANWCAkZdc3rAAHaydJaHx6FBsQyH_MrJ1eEDuddY8eoGERED9p_UDY4W9EfCZj_gjIsYCEUJJNCuOz_afXi6CRJS590uyB4V6EBCF64sf43O9UGby; liap=true; lang=v=2&lang=en-us; timezone=UTC; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; lidc="b=OB75:s=O:r=O:a=O:p=O:g=2524:u=17:x=1:i=1639568817:t=1639655217:v=2:sig=AQGvy4wYrSpa-Rm_7W-Feq21G9ySDcY-"; JSESSIONID=ajax:7943871578965923745; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18977%7CMCMID%7C22952632177093777836618679733005828475%7CMCOPTOUT-1639606206s%7CNONE%7CvVersion%7C5.1.1; li_mc=MTsyMTsxNjM5NjAwNDM5OzI7MDIxGcX+Qsc85hObSfjfS629eaxCaoBGJMeJEWbGiQ7YFg8=',
    'sec-gpc': '1',
}


def get_user_location(p_url):
    response_location = requests.get(f'https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity={p_url}&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-93', headers=headers_location)
    for i in json.loads(response_location.text)['included']:
        print(f"Loooking... for {p_url}")
        for k in i.keys():
            if k == "defaultLocalizedName":
                return i[k]
    return ""

#todo Single file many sheets, Location, Interface, progress-bar,

COUNT_LENGTH = 100
GROUP_ID = 35222
SAMPLE_FRACTION = 0.0002
BLOCK_SIZE = 100

class UserEntry:
    def __init__(self, firstname, lastName, id, occupation):
        self.lastName = lastName
        self.id = id
        self.occupation = occupation
        self.firstname = firstname

    def __eq__(self, other):
        return self.lastName == other.lastName and self.id == other.id


unique_array = np.array([])
leads_frame = pd.DataFrame()
def scrape(g_id):

    global unique_array

    for i in string.ascii_lowercase:
        temp_url = f'https://www.linkedin.com/voyager/api/groups/groups/urn%3Ali%3Agroup%3A{g_id}/members?count={COUNT_LENGTH}&filters=List()&membershipStatuses=List(OWNER,MANAGER,MEMBER)&q=typeahead&query={i}&start=0'

        try:
            responseNo = json.loads(requests.get(temp_url, headers=headers_users).text)['data']['paging']['total'] * SAMPLE_FRACTION
        except:
            repsonseNo = 0

        for index in range(int(responseNo / 100 + 1)):
            p = index * 100
            time.sleep(1)
            url = f'https://www.linkedin.com/voyager/api/groups/groups/urn%3Ali%3Agroup%3A{g_id}/members?count={COUNT_LENGTH}&filters=List()&membershipStatuses=List(OWNER,MANAGER,MEMBER)&q=typeahead&query={i}&start={p}'

            response = requests.get(url, headers=headers_users)
            json_data = json.loads(response.text)

            raw_user_list = json_data['included'][2*COUNT_LENGTH:]

            for entry in raw_user_list:
                user = UserEntry(entry['firstName'],entry['lastName'], entry['publicIdentifier'],  entry['occupation'])
                if user not in unique_array:
                    unique_array = np.append(unique_array, user)

        print(f"Total users for letter {i}: {responseNo} , duplicate percentage:Pokhuy%")

# url = 'https://www.linkedin.com/voyager/api/groups/groups/urn%3Ali%3Agroup%3A35222/members?count=100&filters=List()&membershipStatuses=List(OWNER,MANAGER,MEMBER)&q=typeahead&query=b&start=0'
#
# params = (
#         ('count', '50'),
#         ('filters', 'List()'),
#         ('membershipStatuses', 'List(OWNER,MANAGER,MEMBER)'),
#         ('q', 'typeahead'),
#         ('query', 'a'),
#         ('start', '0'),
#     )
#
# response = requests.get(url, headers = headers)
# json_data = json.loads(response.text)
# print(json_data['data']['paging']['total'])
# print(unique_array.size)


leads = np.array([])


ans = int(input("Group No: "))
s_name = "LDS"

def main():
    scrape(ans)
    ddf = populate_dataframe(unique_array)
    print(ddf)
    #create_new_spreadsheet(s_name)
    update_spreadsheet(unique_array.size, ddf, "bullshit_leads", "HARRRO")

main()