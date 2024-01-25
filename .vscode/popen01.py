fileObj = open('hello.txt', 'w')
fileObj.write('Witaj, świecie!')

fileObj.close()

import subprocess, time
process = subprocess.Popen(['start', 'hello.txt'], shell=True)
time.sleep(7)
process.wait()
delta = subprocess.Popen(['start', '/Applications/Calculator.app/'])