#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-  

from .SDK.CCPRestSDK import REST
# import ConfigParser

#���ʺ�
accountSid= '8aaf07086904be0b01695622e26d2493';

#���ʺ�Token
accountToken= '5f9ec5ae92554c1f8ef180987b44ecc0';

#Ӧ��Id
appId='8aaf07086904be0b01695622e2c22499';

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com';

#����˿� 
serverPort=8883;

#REST�汾��
softVersion='2015-05-11';

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id

def sendTemplateSMS(to,datas,tempId):

    
    #��ʼ��REST SDK
    rest = REST(serverIP,serverPort,softVersion)
    rest.setAccount(accountSid,accountToken)
    rest.setAppId(appId)
    
    result = rest.sendTemplateSMS(to,datas,tempId)
    for k,v in result.iteritems(): 
        
        if k=='templateSMS' :
                for k,s in v.iteritems(): 
                    print('%s:%s' % (k, s))
        else:
            print('%s:%s' % (k, v))
    
   
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)