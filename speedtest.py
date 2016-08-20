import datetime
n = 10000000
print "Executing %d million loops" % (n/1000000.0)
t1 = datetime.datetime.now()
r = 0
for i in range(n):
    r += 1
t2 = datetime.datetime.now()
diff = t2-t1
print diff.microseconds / 1000.0, "ms"
