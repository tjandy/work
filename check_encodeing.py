#!/usr/bin/env python

import sys
import chardet
import json
import os


prepath='/data/sqlcheck/'

def get_charset(s):
	return chardet.detect(s)['encoding']


def check_contain_chinese(check_str):
	for ch in check_str.decode('utf-8'):
		if u'\u4e00' <= ch <= u'\u9fff':
			return True
	return False


def print_charset(file_name):
	f = open(file_name)
	s = f.read()
	if check_contain_chinese(s) != True:
		return
	old_charset = get_charset(s)
	if old_charset != 'utf-8':
		print('error:'+file_name+"  encoding:"+old_charset)
	f.close()


def do(file_name):
	if file_name.find('svn') != -1:
		return
	if os.path.isdir(file_name):
		for item in os.listdir(file_name):
			try:
				if os.path.isdir(file_name+"/"+item):
					do(file_name+"/"+item)	
				else:
					print_charset(file_name+"/"+item)
			except OSError, e:
				print e
	else:
		print_charset(file_name)


def main(argv):
	filename = argv[1]
	do(filename)

if __name__ == '__main__':
	main(sys.argv)
