errcode = ''

res = run_check('ls -1 /dev/sd? | wc -l')
if int(res.stdout) < 2:
 errcode += 'd'

res = run_check('head -1 /proc/meminfo | grep -oP "\d+"')
memory = int(res.stdout)
if memory < 2000000:
 errcode += 'r'

res = run_check('ip l | grep -cP "^\d:"')
if int(res.stdout) < 3:
 errcode += 'i'

res = run_check('who | grep pts')
if res.returncode != 0:
 errcode += 'p'

res = run_check('test -d /home/padavan/archive')
if res.returncode != 0:
 errcode += 'k'

res = run_check('ls -1 /result/ | grep -cvP "7z$"')
if int(res.stdout) != 14:
 errcode += 'D'

res = run_check('rpm -qa | grep -i p7zip')
if res.returncode != 0:
 errcode += 'P'

res = run_check("7za l /root/result.7z | tail -1 | grep -P '14 files' | awk '{print $3}' | md5sum | cut -c5-15 | grep -P '^a9339'")
if res.returncode != 0:
 errcode += 'a'

if errcode != '':
 print ('The task is not completed yet')
else:
 print ('SUCCESS! Please use this string as the correct answer: ', res.stdout)


try:
 if sys.argv[1] == '-d':
  print ('Status:', errcode)
except:
 exit()
