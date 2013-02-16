#
#Love-clss -- http://loveplusplus.ru client
#
#name: Taras Zakharchenko
#e-mail: taras.zakharchenko@gmail.com
#vk.com: id5022249
#web: zakharchenko.in.ua
#version: 0.1.0 16.02.2013
#

# -*- coding: UTF-8 -*-

import urllib.request
import urllib.parse
import argparse
import getpass
from http.cookiejar import CookieJar



class loveplusplus:
	def __init__(self):
		cj = CookieJar()
		self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
		urllib.request.install_opener(self.opener)
		self.prepare_parsers()
	
	def prepare_parsers(self):
		self.login_parser = argparse.ArgumentParser(prog='login', description='')
		self.login_parser.usage = "login [options]"
		self.login_parser.add_argument('-e', '--email', metavar='', help='Set email', nargs=1, required=False)
	
		self.edit_parser = argparse.ArgumentParser(prog='edit', description='')
		self.edit_parser.usage = "edit [options]"
		self.edit_parser.add_argument('-p', '--pwd', metavar='', help='Set new password', nargs=1, required=False)
		self.edit_parser.add_argument('-n', '--name', metavar='', help='Set name', nargs='*', required=False)
		self.edit_parser.add_argument('-a', '--age', metavar='', help='Set age', nargs=1, required=False)
		self.edit_parser.add_argument('--photo', metavar='', help='Set profile photo url', nargs=1, required=False)
		self.edit_parser.add_argument('--city', metavar='', help='Set living city', nargs=1, required=False)
		self.edit_parser.add_argument('--about', metavar='', help='Set about text', nargs='*', required=False)
		self.edit_parser.add_argument('--salary', metavar='', help='Set salary amount', nargs='*', required=False)
		self.edit_parser.add_argument('--sex', metavar='', help='Set your sex (male|female)', nargs=1, required=False)
		
	def loverequest(self, method, fields):	
		data = {
			"method" : method
		}
		for key in fields:
			data["obj[%s]"%key] = fields[key]
		post_data = urllib.parse.urlencode(data)
		r = urllib.request.urlopen('http://loveplusplus.ru/con', bytearray(post_data.encode('utf-8')))
		return r.read().decode('utf-8')
	
	def command_processor(self, line):
		line = line.split(' ')
		cmd_name = line[0]
		cmd_args = line[1:]
		if cmd_name == "login":
			self.love_login(cmd_args)
		elif cmd_name == "edit":
			self.love_edit(cmd_args)
		else:
			print("Unknown command!")
		
	
	def love_login(self, args):
		try:
			params = self.login_parser.parse_args(args)
		except:
			return
		if params.email == None:
			print("Email address not supplied!")
			return
		pwd = getpass.getpass()
		json = self.loverequest("login", {"email":params.email[0], "password":pwd})
		json = eval(json)
		self.email = params.email[0]
		if json["status"] == "fail":
			print("Error: %s"%json["message"])
		else:
			print("Logined as: %s"%json["uid"])
			
	def love_edit(self, args):
		try:
			params = self.edit_parser.parse_args(args)
		except:
			return
		data = {}
		if params.about != None:
			data["about"] = " ".join(params.about)
		if params.pwd != None:
			data["pwd"] = " ".join(params.pwd)
		if params.name != None:
			data["name"] = " ".join(params.name)
		if params.photo != None:
			data["photo"] = " ".join(params.photo)
		if params.age != None:
			data["age"] = params.age
		if params.photo != None:
			data["salary"] = " ".join(params.salary)
		if params.city != None:
			data["city"] = " ".join(params.city)
		if params.sex != None:
			data["sex"] = params.sex
		if len(data) == 0:
			print("Paramaters are not supplied")
			return
		pwd = getpass.getpass()
		data["password"] = pwd
		json = self.loverequest("edit", data)
		json = eval(json)
		if json["status"] == "fail":
			print("Error: %s"%json["message"])
		if json["status"] == "ok":
			print(json["message"])