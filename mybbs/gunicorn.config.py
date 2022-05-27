import gevent.monkey
import multiprocessing


gevent.monkey.patch_all()

workers = 4
# threads = multiprocessing.cpu_count()*2 +1
worker_class = 'gevent'

bind = '0.0.0.0:2001'
pid = '/tmp/bbs.pid'
