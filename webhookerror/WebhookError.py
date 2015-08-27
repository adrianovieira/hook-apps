# -*- coding: utf-8 -*-
import logging
from time import asctime, gmtime, strftime
#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

class WebhookError:
    def __init__(self, message, module='PandocParser', package='artigo', app_name='Webhook'):
        self.message = message
        self.app_name = app_name
        self.package = package
        self.module = module
        self.log_level = '???' # obter logging level e name

    def __str__(self):
        return '%s em [%s, %s, %s]'%(self.message,self.module,self.package,self.app_name)
    def __unicode__(self):
        return u'%s em [%s, %s, %s]'%(self.message,self.module,self.package,self.app_name)
    def logging(self):
        return u'%s %s em [%s, %s, %s]'%(asctime(), self.message,self.module,self.package,self.app_name)
