import requests
import json
import requests

# Fill in your details here to be posted to the login form.


# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.linkedin.com/login/', auth=('art_shagi@mail.ru', 'Lightlight1313'))
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
    r = s.get('A protected web page url')
    print (r.text)
        # etc...