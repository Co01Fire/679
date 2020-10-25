from random import sample
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json
import random
from threading import Timer


headers = {"User-Agent":"bilibili Security Browser",
	"Cookie": "自己填",
	"Referer": "https://security.bilibili.com/sec1024/",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"Content-Type": "application/json;charset=UTF-8",
	"Origin": "https://security.bilibili.com",
	"Accept": "application/json, text/plain, */*",}


def work():
	while True:
		flag = random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+'-'+ random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+'-'+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+'-'+ random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')+random.choice('abcdef1234567890')
		
		data = {"flag":flag,"ctf_id":6}
		res = requests.post("https://security.bilibili.com/sec1024/api/v1/flag",headers=headers,data=json.dumps(data),verify=False)
		print(flag+" ------> "+res.text)
		if res.text != '{"code":200,"msg":"Flag错误，请继续努力"}' :
			fp=open("flag.txt","a+",encoding="utf-8")
			fp.write(flag+'\n')
			fp.close()
		

t1 = Timer(1, work)
t2 = Timer(2, work)
t3 = Timer(3, work)
t4 = Timer(4, work)
t5 = Timer(5, work)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
print('线程启动完毕')
