import redis
import random

redis = redis.Redis('localhost')

redis.flushall()
redis.sadd("cartela", *set(range(1, 101)))

for i in range(1, 51):
    user_hash = "user:" + str(i)
    cartela_hash = "cartela:"+str(i)
    score_hash = "score:"+str(i)

    user_info = {"name": "user"+str(i), "cartela" : cartela_hash, "score": score_hash}
    redis.hmset(user_hash, user_info)
    
    cartela = redis.srandmember("cartela", 15)

    redis.sadd(cartela_hash, *set(cartela))
    redis.zadd("score", {score_hash: 0})

print(redis.zrange("score", 0, -1))

while True:
    numero_sorteado = redis.spop("cartela")
    users_keys = redis.keys("user:*")

    for key in users_keys:
        user = redis.hgetall(key)
        cartela = redis.smembers(user[b'cartela'])

        if(numero_sorteado in (cartela)):
            redis.zincrby("score", 1, user[b'score'])

    score = redis.zrange("score", 0, 0, desc=True, withscores=True)

    if(score[0][1] == 15):
        break

print(score[0][1])
print(score[0][0])