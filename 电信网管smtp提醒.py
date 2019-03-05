import requests 
import json
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


def sendmail(content):
	mail_host = 'smtp.163.com'
	smtp_user = ''
	smtp_pass = ''

	send_user = ''


	message = MIMEText(content,'html','utf-8')
	message['From'] = smtp_user
	message['To'] = send_user


	subject = '电信网管SMTP提醒'
	message['Subject'] = subject
	smtpObj = smtplib.SMTP()
	smtpObj.connect(mail_host,25)
	smtpObj.login(smtp_user,smtp_pass)
	smtpObj.sendmail(smtp_user,send_user,message.as_string())
	print ('SMTP Success---')

print ('[Start]...')
content=""
cookies = {'amlbcookie':'02',
           'AMAuthCookie':'', 
           'TRACE':'CN=yDZ32UpEdyk='}
url = "http://url/DevSettings/RepairTasksJson" #url
data ={'page':'1',
        'size':'100',
        'filterStatus':'0',
        'filterCategory':'1',
        'filterWorker':''
}
headers = {'X-Requested-With':'XMLHttpRequest'}

codesuccess=1
#X-Requested-With: XMLHttpRequest
s = requests.session()
while True:
	r = s.post(url,data = data,cookies = cookies,headers=headers)

	datas = json.loads(r.text)
	#print (datas)
	for i in datas['data']:
	
		content += ('[ID]:'+''.join(str(i['Id']))+'</br>')
		content += ('[Description]:'+''.join(str(i['Description']))+'</br>')
		content += ('[Status]:'+''.join(str(i['Status']))+'</br>')
		content += ('[SubmitUserMobile]:'+''.join(str(i['SubmitUserMobile']))+'</br>')
		content += ('[SubmitUser]:'+''.join(str(i['SubmitUser']))+'</br>')
		content += ('[BuildingName]:'+''.join(str(i['BuildingName']))+'</br>')
		content += ('[Space]:'+''.join(str(i['Space']))+'</br>')
		print ('content:',content)
		if(str(i['Status'])=='0'):
			#print (i['Status'])
			sendmail(content)
			content=""
		break
	codesuccess+=1
	print ('本脚本已经成功运行',codesuccess,'次')
	time.sleep(60)


