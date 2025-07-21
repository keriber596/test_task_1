import os
import redis
import logging

logging.basicConfig(level=logging.INFO, filename="redis.log", filemode="w", )
r = redis.Redis(host=os.environ.get("REDIS_HOST"), port=int(os.environ.get("REDIS_PORT")), decode_responses=True)


def main():
    if r.get("back") == None:
        await r.set("back", 0)

    length = r.xlen(os.environ.get("STREAM_NAME"))
    if length > 0:
        messages = r.xread(count=length, streams={os.environ.get("STREAM_NAME"): r.get("back")})
        for message in messages:
            logging.info(message)
            await r.set('last', message[-1][-1][0])


while True:
    main()
