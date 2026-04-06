import threading
import time


def work():
    print(f"{threading.current_thread()} start")
    time.sleep(10)
    print(f"{threading.current_thread()} end ")
    print("----------")

if __name__ == '__main__':
    for i in range(10):
        threading.Thread(target=work).start()