import os

port = int(os.getenv('PORT', '8000'))
bind = f'0.0.0.0:{port}'
workers = os.getenv('WORKERS_NUM', 4)
threads = os.getenv('THREADS_NUM', 2)
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
timeout = 600