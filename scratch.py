

import requests
from requests.auth import HTTPBasicAuth

# Making a get request
response = requests.get('https://www.linkedin.com/login/ru?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin',
                        auth=HTTPBasicAuth('art_shagi@mail.ru', 'Lightlight1313'))

# print request object
dic_a = response.cookies.get_dict(".linkedin.com")
dic_b = response.cookies.get_dict(".www.linkedin.com")

dic_b.update(dic_a)
print(dic_b)