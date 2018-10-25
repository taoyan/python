import requests


url = 'https://www.yaozh.com/member'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
# cookies = {
#     'cookies':'WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=fu19r23jrmuh971kehr1tm2mv7; _ga=GA1.2.1278869565.1540210320; MEIQIA_EXTRA_TRACK_ID=1AKqKD6HXdJYfQnXoA8kjWFP3Nv; _gid=GA1.2.603826180.1540383826; MEIQIA_VISIT_ID=1C1OqBzcU7phLj7wgpgzGoslC7C; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1540210324,1540210619,1540383828; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540383944; yaozh_logintime=1540383985; yaozh_user=634472%09yantao123; yaozh_userId=634472; db_w_auth=594108%09yantao123; UtzD_f52b_saltkey=BcyjRMmh; UtzD_f52b_lastvisit=1540380388; UtzD_f52b_lastact=1540383988%09uc.php%09; UtzD_f52b_auth=18d3k5LBi569kW8clNM3cNFTItM9HRcFGTR1HTbj3TlR1Ynu05seBnuU2e%2BCo84iKOZBLkEF7FXxT7BdYaDh5zqRz20; yaozh_uidhas=1; yaozh_mylogin=1540383991; _gat=1'
# }


cookies_str ='WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; PHPSESSID=fu19r23jrmuh971kehr1tm2mv7; _ga=GA1.2.1278869565.1540210320; MEIQIA_EXTRA_TRACK_ID=1AKqKD6HXdJYfQnXoA8kjWFP3Nv; _gid=GA1.2.603826180.1540383826; MEIQIA_VISIT_ID=1C1OqBzcU7phLj7wgpgzGoslC7C; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1540210324,1540210619,1540383828; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1540383944; yaozh_logintime=1540383985; yaozh_user=634472%09yantao123; yaozh_userId=634472; db_w_auth=594108%09yantao123; UtzD_f52b_saltkey=BcyjRMmh; UtzD_f52b_lastvisit=1540380388; UtzD_f52b_lastact=1540383988%09uc.php%09; UtzD_f52b_auth=18d3k5LBi569kW8clNM3cNFTItM9HRcFGTR1HTbj3TlR1Ynu05seBnuU2e%2BCo84iKOZBLkEF7FXxT7BdYaDh5zqRz20; yaozh_uidhas=1; yaozh_mylogin=1540383991; _gat=1'

# cookie_dict = {}
# cookies_list = cookies_str.split(';')
# for cookie in cookies_list:
#     cookie_dict[cookie.split('=')[0]] = cookie.split('=')[1]
#
# print(cookie_dict)

#字典推倒式
cookies_dict2 = {cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies_str.split(';')}
print(cookies_dict2)

response = requests.get(url=url,headers = headers, cookies = cookies_dict2)
data = response.content.decode()
with open('04-cookie.html','w') as f:
    f.write(data)