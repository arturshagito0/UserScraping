import gspread
import json
import pandas as pd
import requests

headers_location = headers = {
    'authority': 'www.linkedin.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-restli-protocol-version': '2.0.0',
    'dnt': '1',
    'x-li-lang': 'en_US',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'x-li-page-instance': 'urn:li:page:d_flagship3_profile_view_base;bHbaEEZiTquzNa6mV60PNg==',
    'accept': 'application/vnd.linkedin.normalized+json+2.1',
    'csrf-token': 'ajax:2832829851912680547',
    'x-li-track': '{"clientVersion":"1.9.7977","mpVersion":"1.9.7977","osName":"web","timezoneOffset":0,"timezone":"UTC","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.25,"displayWidth":1920,"displayHeight":1080}',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.linkedin.com/groups/35222/members/',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'bcookie="v=2&f457616b-52cc-43eb-8e90-23ec38ea8e86"; bscookie="v=1&20211209170108357be425-a454-435b-8ca7-9551fa4ffca6AQGVosJ8KTyHxfgZXF9tDWm4S3Wmpceo"; li_alerts=e30=; li_rm=AQFQMJ4yEoLSDwAAAX2gJIimwD7K6Hv2DTulPWxxzatwJ0_CGRTcLtinpdhEeuBlO7bF_jftEgBKRjUw6RwaCdvOEhIyL-WSprF_nzxwDIBSqGux_RLv46Dy; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; timezone=UTC; visit=v=1&M; g_state={"i_l":1,"i_p":1639752278386}; li_gc=MTsyMTsxNjM5NzQ1MDkyOzI7MDIxJHi6i2xtQLBFvfvdRnIYX1UYGduaPK2/lXJvBSqBLQw=; _gcl_au=1.1.2073284504.1639745101; JSESSIONID="ajax:2832829851912680547"; liap=true; li_at=AQEDASw3s0MChB9CAAABfciCSG4AAAF97I7MblYAIgMDUKhNRUJyH8jEx-cZLWegcURa10wBn-bjQ7V1kEPJM3P7cyS53dXwwpFnWo1vuyCCWYH0mkaDSS9eBrdCzNgckzWT4IeCGqnMqJwTg7Lp8L_I; lang=v=2&lang=en-us; li_mc=MTsyMTsxNjM5NzQ4ODU4OzI7MDIxPBozlMbM6iUI+ec6OMGb63WoO23eu9MEhLPMjx9zDlE=; gpv_pn=www.linkedin.com%2Flegal%2Fcrawling-terms.; s_tp=2450; s_cc=true; s_plt=0.79; s_pltp=www.linkedin.com%2Flegal%2Fcrawling-terms.; s_ips=722; s_ppv=www.linkedin.com%2Flegal%2Fcrawling-terms.%2C29%2C29%2C722%2C1%2C3; s_tslv=1639749043148; lidc="b=OB75:s=O:r=O:a=O:p=O:g=2525:u=19:x=1:i=1639749043:t=1639835258:v=2:sig=AQEYt7CTzb9WXPS2LlATP_yX_v23tMdu"; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C18979%7CMCMID%7C22952632177093777836618679733005828475%7CMCOPTOUT-1639756344s%7CNONE%7CvVersion%7C5.1.1',

    'sec-gpc': '1',
}

def get_user_location(p_url):
    response_location = requests.get(f'https://www.linkedin.com/voyager/api/identity/dash/profiles?q=memberIdentity&memberIdentity={p_url}&decorationId=com.linkedin.voyager.dash.deco.identity.profile.FullProfileWithEntities-93', headers=headers_location)
    print(f"Loooking... for {p_url}")
    for i in json.loads(response_location.text)['included']:
        for k in i.keys():
            if k == "defaultLocalizedName":
                return i[k]
    return ""


def main(table_name, sheet_name):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open(table_name)
    worksheet = sh.worksheet(sheet_name)
    data = worksheet.get_all_values()
    headers = data.pop(0)
    n = 5
    df = pd.DataFrame(data, columns=headers)

    df['location'] = df['id'][:10].apply(lambda x: get_user_location(x))
    df = df.fillna("mt")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    print(df)



main("TEST_USERS", "TEST_USERS-1691")