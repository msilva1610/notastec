#!/usr/bin/env python3

import redis

redis_host = "192.168.70.5"
redis_port = 6379
redis_password = ""

def hello_redis():
    """Exemplo"""

    try:
        print("Conectando com o servidor ...")
        r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
        print("Salvando variáveis ...")
        r.set("msg:hello", "Hello Redis!!!")
        print("Recuperando variáveis ...")
        msg = r.get("msg:hello")
        print("valor recuperado:",msg)        
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    hello_redis()
