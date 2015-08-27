# -*- coding: utf-8 -*-
import logging
from time import asctime, gmtime, strftime
#FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'

class WebhookError:
    def __init__(self, message, log_levelname=logging.INFO,module='PandocParser', package='pandoc', app_name='Webhook'):
        self.message = message
        self.log_levelname = log_levelname
        self.app_name = app_name
        self.package = package
        self.module = module

    def __str__(self):
        return '%s em [%s, %s, %s]'%(self.message,self.module,self.package,self.app_name)
    def __unicode__(self):
        return u'%s em [%s, %s, %s]'%(self.message,self.module,self.package,self.app_name)
    def logging(self):
        return u'%s [%s] %s em [%s, %s, %s]'%(asctime(), self.log_levelname ,self.message,self.module,self.package,self.app_name)
