import subprocess

p1=subprocess.Popen('python cut.py -d " " record.txt',shell=True,stdout=subprocess.PIPE)
#piping
p2=subprocess.Popen('python cut.py -d " " -f 1,2',shell=True,stdin=p1.stdout,stdout=subprocess.PIPE)


result=p2.stdout.read()
print(result.decode("utf-8"))
