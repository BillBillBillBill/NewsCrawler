import subprocess
import time


if __name__ == '__main__':
    while True:
        subprocess.call(['python', 'start_crawl.py'])
        time.sleep(30)
