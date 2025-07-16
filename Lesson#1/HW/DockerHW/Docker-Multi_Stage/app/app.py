from flask import Flask
from flask_caching import Cache
import redis
import os

def create_app():
    app = Flask(__name__)

    # Setting the environment variables for the flask to connect to redis
    app.config['CACHE_TYPE'] = os.getenv('CACHE_TYPE')
    app.config['CACHE_REDIS_HOST'] = os.getenv('CACHE_REDIS_HOST')
    app.config['CACHE_REDIS_PORT'] = int(os.getenv('CACHE_REDIS_PORT'))
    app.config['CACHE_REDIS_DB'] = int(os.getenv('CACHE_REDIS_DB'))


    cache = Cache(app)
    cache.init_app(app)

    # Launching the redis client for testing key pull
    redis_client = redis.Redis(
        host=app.config['CACHE_REDIS_HOST'],
        port=app.config['CACHE_REDIS_PORT'],
        db=app.config['CACHE_REDIS_DB']
    )

    @app.route('/')
    @cache.cached(timeout=30)
    def home():
        return "This is for the Docker homework."

    @app.route('/redis-test')
    def redis_test():
        redis_client.set('test', 'Testing key pulling from redis container.')
        return redis_client.get('test').decode('utf-8')

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=8000)