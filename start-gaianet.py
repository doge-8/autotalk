import time
import subprocess

def run_commands():
    while True:
        # 运行 `gaianet stop` 命令
        subprocess.run(["gaianet", "stop"])
        
        # 等待5秒
        time.sleep(5)
        
        # 运行 `gaianet run` 命令
        subprocess.run(["gaianet", "run"])
        
        # 每小时循环一次
        time.sleep(3600)

if __name__ == "__main__":
    run_commands()
