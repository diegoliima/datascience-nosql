import redis

redis = redis.Redis('localhost')

redis.flushall()

for i in range(1, 50):
    user_hash = "user:" + str(i)
    cartela_hash = "cartela:"+str(i)
    score_hash = "score:"+str(i)

    user_info = {"name": "user"+str(i), "cartela" : cartela_hash, "score": score_hash}
    redis.hmset(user_hash, user_info)
    redis.sadd("cartela", *set(range(1, 100)))

    cartela = redis.srandmember("cartela", 15)

    print(cartela)
    redis.sadd(cartela_hash, *set(cartela))
    redis.zadd("score", i, score_hash)

while(True):
    print(1)
    exit

print(redis.hgetall("user:1"))
print(redis.smembers("cartela:1"))
