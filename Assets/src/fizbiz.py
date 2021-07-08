#!\Users\nswinn27\.conda\envs\alpha\python.exe
from os import sys
sys.path.append("c:\\users\\nswinn27\\documents\\fitbit\\assets\\lib\\fitbit")

import gather_keys_oauth2 as Oauth2

import fitbit
import pandas as pd 
import datetime




USERS = {'User1':
            {'client_id':'23B96N',
            'client_secret':'41affdb8b5ff55412aa29c95f5415548',
            'redirect_url':'http://127.0.0.1:8080/',
            'auth_uri':'https://www.fitbit.com/oauth2/authorize',
            'access_refresh_req':'https://api.fitbit.com/oauth2/token'}
            }


server = Oauth2.OAuth2Server(USERS['User1']['client_id'],USERS['User1']['client_secret'])
server.browser_authorize()

ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])


auth2_client = fitbit.Fitbit(USERS['User1']['client_id'],USERS['User1']['client_secret'],
                    oauth2=True,access_token=ACCESS_TOKEN,
                    refresh_token=REFRESH_TOKEN)



