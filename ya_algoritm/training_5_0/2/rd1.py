import threading
import time


def worker():
    thread = threading.current_thread()
    name = thread.name
    ident = thread.ident

    print(f'Поток с именем "{name}" запустился c id: {ident}')
    time.sleep(3)
    print(f'Поток с именем "{name}" завершился')


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(name=f'Поток {i}', target=worker)
        threads.append(t)
        t.start()

    amount = threading.active_count()
    print(f'Всего потоков запущено: {amount}')

    threads_list = threading.enumerate()
    print(threads_list)

    [thread.join() for thread in threads]