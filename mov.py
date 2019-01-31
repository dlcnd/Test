#!/usr/bin/env python
#coding:utf8

#1. 폴더를 탐색한다.
#2. exr로 jpg를 만든다.
#3. jpg로 mov를 만든다.
#4. jpg를 삭제한다.

import os

for i in os.listdir("/project/circle/in"):
	print i

if not os.path.exists("/project/circle/in")
	print("there is no existing path")
	os.makedirs("/project/circle/in")


if __name__=="__main__":
	p = "/project/circle/in/aces_exr"
	for i in os.listdir(p):
		for j in os.listdir(p+"/"+i):
			print "/".join([p,i,j])

os.makedirs("/tmp/proxy/..")


