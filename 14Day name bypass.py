import requests
from uuid import uuid4
re = requests.session()
uuid = uuid4()
print("""
███████╗██████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
Add me on my instagram account @y9l5o
""")
user = input('[+] Username :')
password = input('[+] Password :')
name = input('[+] New Name :')
hdlog = {
'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
'Accept': "*/*",
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Host': 'i.instagram.com'
}
dtlog = {
'uuid': uuid,
'password': password,
'username': user,
'device_id': uuid,
'from_reg': 'false',
'_csrftoken': 'missing',
'login_attempt_countn': '0'
}
dtname = {
'first_name': name
}
log = re.post('https://i.instagram.com/api/v1/accounts/login/', headers=hdlog, data=dtlog, allow_redirects=True)
if log.text.find("is_private") >= 0:
  print('[+] Logged in :',user)
  re.headers.update({'X-CSRFToken': log.cookies['csrftoken']})
elif "The username you entered doesn't appear to belong to an account" in log:
  print("[-] Username is wrong")
  exit()
elif "The password you entered is incorrect. Please try again." in log:
  print('[-] Password is wrong')
  exit()
elif "challenge_required" in log:
  print('[-] Secure required')
elif '"two_factor_required":true' in log:
  print("[-] Two factor required")
  exit()
else:
  print("Some Error Happend , Try again !")
  print(log.text)
  exit()
url = 'https://i.instagram.com/api/v1/accounts/set_phone_and_name/'
reqna = re.post(url, headers=hdlog, data=dtname).text
if '"status":"ok"' in reqna:
  print(f'[+] Done changed name to {name}')
elif '"Ensure this value has at most 30 characters' in reqna:
  print('[-] The new name too long')
else:
  print('[-] Some Error Happend , Try again')
  print(reqna)