#coding:utf8
import redis


r = redis.Redis(host='10.10.10.172',port=6379)
"""
for i in range(10000):
	r.set(str(i),i)
"""
"""
r.set('foo','bar')
value = r.get('foo')
print(value)

r.set('foo', 'foo')
value = r.get('foo')
print(value)
"""
r.set("LeeChungIn","01074376721")
print r.get('LeeChungIn')
