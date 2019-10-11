#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from .SDK.CCPRestSDK import REST
# import ConfigParser


#主帐号
accountSid= '8aaf07086904be0b01695622e26d2493';

#主帐号Token
accountToken= '5f9ec5ae92554c1f8ef180987b44ecc0';

#应用Id
appId='8aaf07086904be0b01695622e2c22499';

#请求地址，格式如下，不需要写http://
serverIP='app.cloopen.com';

#请求端口 
serverPort=8883;

#REST版本号
softVersion='2013-12-26';

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为数组 例如：{'12','34'}，如不需替换请填 ''
  # @param $tempId 模板Id

def sendTemplateSMS(to,datas,tempId):

    
    #初始化REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)

    # 先使用统一模版
    tempId = 479135

    print('=======' , datas)
    result = rest.sendTemplateSMS(to,datas,tempId)
    print(result)
    if 'statusCode' in result.keys():
        return True if(result['statusCode'] == '000000') else False
    return False

    # for k,v in result.iteritems():
    #
    #     if k=='templateSMS' :
    #             for k,s in v.iteritems():
    #                 print('%s:%s' % (k, s))
    #     else:
    #         print('%s:%s' % (k, v))
    
   
#sendTemplateSMS(手机号码,内容数据,模板Id)