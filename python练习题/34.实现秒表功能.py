import time
print("按下回车开始计时，按下Ctrl + C 停止计时")
while True:
    input("")
    start_time = time.time()
    print("开始计时...")
    try:
        while True:
            elapsed_time = round(time.time() - start_time)
            print(f"计时：{elapsed_time} 秒", end="\r", flush = True) 
            time.sleep(1)
    except KeyboardInterrupt:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)
        print(f"\n计时结束，总共时间为：{total_time} 秒")
        break
    