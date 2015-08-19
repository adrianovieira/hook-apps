# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('UTF-8')

sys.path.insert(0, '/var/www/webhook')

from webhook import app as application

