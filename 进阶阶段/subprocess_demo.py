import subprocess
result = subprocess.run(["echo", "Hello"], capture_output=True,text=True)
print(result.stdout)
subprocess.run("grep 'error' log.txt | wc -l", shell=True,check=True)
Proc = subprocess.Popen(["tail", "-f", "log.txt"], stdout=subprocess.PIPE)
while True:
    line = Proc.stdout.readline()
    if not line:
        break
    print(line.decode().strip())
try:
    subprocess.run(["sleep", "10"], timeout=5)
except subprocess.TimeoutExpired:
    print("命令超时！")
    