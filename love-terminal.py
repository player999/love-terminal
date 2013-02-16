#
#Love-terminal -- http://loveplusplus.ru client
#
#name: Taras Zakharchenko
#e-mail: taras.zakharchenko@gmail.com
#vk.com: id5022249
#web: zakharchenko.in.ua
#version: 0.1.0 16.02.2013
#

# -*- coding: UTF-8 -*-

from loveplusplus import loveplusplus

lpp = loveplusplus()
while 1:
	line = input("lpp> ")
	lpp.command_processor(line)