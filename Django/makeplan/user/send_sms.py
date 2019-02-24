
import requests
import json


class SendSMS(object):
    def __init__(self):
        self.app_id = "C92781433"
        self.app_key = "85916c177b989fb7388e8ec362fb08fe"
        self.url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"

    def send_sms(self, code, mobile):
        text = "您的验证码是：%s。请不要把验证码泄露给其他人。" % code

        params = {
            'account': self.app_id,
            'password': self.app_key,
            'content': text,
            'mobile': mobile,
            'format': 'json'
        }
        response = requests.post(self.url, data=params)
        re_dict = json.loads(response.text)
        return re_dict

