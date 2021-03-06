#!/usr/bin/env python
#coding:utf8
import os
import sys
import subprocess

def genThumb(src):
	"""
	경로를 입력받으면 썸네일을 만든다.
	"""
	if not os.path.exist(src):
		return "", "파일이 존재하지 않습니다."

	if not os.path.isfile(src):
		return "", "파일형태가 아닙니다."

	if not os.path.exists("/usr/bin/convert"):
		return "", "ImageMagick이 설치되지 않았습니다."

	
	d, f = os.path.split(src)
	notuse, ext = os.path.splitext(f)
	dst = d+"/"+f.replace(ext,".jpg")
	#cmd = "convert {src} -thumbnail {size} -background black -gravity center -extent {size} {dst}".format(
	#		src=src,
	#		dst=dst,
	#size = "360x240")
	size="360x240"
	cmds = ["convert",src,"-thumbnail",size,
			"-background","black","-gravity","center",
			"-extent",size,dst]
	p = subprocess.Popen(cmds, stdout=subprocees.PIPE, stderr=subprocess.PIPE)
	return p.communicate() # stdout, stderr 2개 나옴
	#print cmd
	#os.system(cmd)

if __name__="__main__":
	src = "/project/circle/in/aces_exr/A003c025_150830_R0D0/A003C025_150830_R0D0.078727.exr"
	stdout, stderr = genThumb(src)
	if stdErr:
		sys.stderr.write(stderr)
	sys.stdout.write(stdout)

