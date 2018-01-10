## This is the python script to let netperf experiment running
## in long run

import subprocess
import time

f = open('UDP_Local.txt', 'a+')
for i in xrange(1050, 3100, 100): ## (start, end, gap)
  cmd = './netperf -t UDP_STREAM -H 192.168.0.1 -- -P 12866 -r %s  -m 3100' % i
  ##cmd = './netperf -t UDP_STREAM -H 192.168.0.1 -- -P 12866 -s %s  -m 3100' % i
  print(cmd)
  result = subprocess.check_output(cmd, shell=True)
  f.write(cmd + '\n')
  f.write(result)
  f.flush()
  time.sleep(60)
f.close()


