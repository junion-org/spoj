import sys,re
for l in sys.stdin:print 2**len(re.findall('[TDLF]',l))
