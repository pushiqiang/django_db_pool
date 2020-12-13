
import requests
import threading


def test_view():
    for i in range(1000):
        requests.get('http://localhost:8000/view')


def test_transaction_view():
    for i in range(1000):
        requests.get('http://localhost:8000/transaction_view')


def test_threading_view():
    for i in range(1000):
        requests.get('http://localhost:8000/threading_view')


if __name__ == '__main__':
    threads = []
    for target in [test_view, test_transaction_view, test_threading_view]:
        threads.append(threading.Thread(target=target))

    for t in threads:
        t.start()

    for t in threads:
        t.join()
