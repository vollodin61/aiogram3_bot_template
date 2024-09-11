from redis.asyncio.client import Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry
from redis.exceptions import BusyLoadingError, ConnectionError, TimeoutError

RETRY = 3
TIMEOUT = 2


class Singleton:
    _instance = None

    @staticmethod
    def get_connection(host: str, port: str):
        port = int(port)
        if not Singleton._instance:
            Singleton._instance = Redis(host=host, port=port, socket_timeout=TIMEOUT,
                                        retry=Retry(ExponentialBackoff(), RETRY),
                                        retry_on_error=[BusyLoadingError, ConnectionError, TimeoutError])
        return Singleton._instance
