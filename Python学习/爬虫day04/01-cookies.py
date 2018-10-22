import urllib.request

'''
将cookie复制到请求头
'''

url = 'https://www.yaozh.com/member/'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie':'WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=fu19r23jrmuh971kehr1tm2mv7; _ga=GA1.2.1278869565.1540210320; _gid=GA1.2.2027581890.1540210320; MEIQIA_VISIT_ID=1BvjA2IdLZrpQZujTCAFtGBfsgC; MEIQIA_EXTRA_TRACK_ID=1AKqKD6HXdJYfQnXoA8kjWFP3Nv; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540210619; yaozh_logintime=1540210670; yaozh_user=634466%09yant; db_w_auth=594102%09yant; UtzD_f52b_saltkey=bpR2tPIo; UtzD_f52b_lastvisit=1540207071; UtzD_f52b_lastact=1540210671%09uc.php%09; UtzD_f52b_auth=3574GTRwiK67uVbzGfVZyTDpig0S11Zwu%2BOygltD8HzrSyxZa5N6lr8B9H5CMlDi5FyaoazVeEtdBY2ttq%2FfJ9ur4wo; yaozh_uidhas=1; yaozh_mylogin=1540210674; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; MEIQIA_VISIT_ID=1BvjA2IdLZrpQZujTCAFtGBfsgC; MEIQIA_EXTRA_TRACK_ID=1AKqKD6HXdJYfQnXoA8kjWFP3Nv; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1540210324%2C1540210619; _gat=1'
}

request = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(request)

data = response.read()

#保存文件中，验证数据
with open('01cook.html','wb') as f:
    f.write(data)