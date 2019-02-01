#!usr/bin/env python
#coding:utf8
import re

def project(path):
	"""
	경로에서 project 이름을 반환.
	"""
	p= re.findall('/prject/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 project정보를가져 올 수 없습니다" 
	return p[0],None

def seq(path):
	"""
	경로에서 seq 이름을 반환.
	"""
	p= re.findall('/shot/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 seq 정보를가져 올 수 없습니다" 
	return p[0],None

def shot(path):
	"""
	경로에서 shot 이름을 반환.
	"""
	p= re.findall('/shot/\w/(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 shot 정보를가져 올 수 없습니다" 
	return p[0],None

def task(path):
	"""
	경로에서 task 이름을 반환.
	"""
	p= re.findall('/shot/\w/\w(\w+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 task 정보를가져 올 수 없습니다" 
	return p[0],None

def ver(path):
	"""
	경로에서 version 정보를 반환.
	"""
	p= re.findall('_v(\d+)',path.replace("\\","/"))
	if len(p) != 1:
		return "", "경로에서 version 정보를가져 올 수 없습니다" 
	return int(p[0]),None

def seqNum(path):
	"""
	경로에서sequence number 반환.
	"""
	p= re.findall('\.(\d+)\.\w+$',path.replace("\\","/"))
	#p= re.findall('\.(\d+)\.',path.replace("\\","/"))
	if len(p) != -1:
		return "", "경로에서 sequence number 정보를가져 올 수 없습니다" 
	return int(p[0]),None

def digitNum(path):
	"""
	경로에서 시퀀스 넘버 자릿수를 반환.
	"""
	p= re.findall('\.(\d+)\.',path.replace("\\","/"))
	if len(p) != -1:
		return "", "경로에서 sequence number 자릿수를 가져 올 수 없습니다" 
	return int(p[0]),None

def toFFmpeg(path):
	"""
	경로를 받아서 시퀀스라면 ffmpeg 경로로 바꿈.
	"""
	p= re.findall('\.(\d+)\.',path.replace("\\","/"))
	if len(p) != -1:
		return path, "경로가 시퀀스 구조가 아닙니다."
	digitNum=len(p[0])
	head, tail = path.split(p[0])
	return "%s%%%dd%s" % (head,digitNum,tail),None

