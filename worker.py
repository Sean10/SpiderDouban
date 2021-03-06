from redis import Redis,ConnectionPool
from rq import Worker, Queue, Connection
import time

listen = ['high', 'default', 'low']

pool = ConnectionPool(db=0, host='localhost', port=6379)
redis_conn = Redis(connection_pool=pool)

if __name__ == '__main__':
    start = time.time()
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen))
        worker.work()
        stop = time.time()
        print(stop-start)
