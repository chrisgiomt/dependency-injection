import redis
r = redis.Redis()
players_dict = {"Dave": 340, "Kendra": 400, "Tom": 560, "Barbara": 650, "Jennifer": 690, "Peter": 690, "Frank": 740}

# print(r.get("Dave").decode("utf-8"))
for player, score in players_dict.items():
    r.zadd("players_dict", {player: score})

print(r.zrevrange("players_dict", start=0, end=5, withscores=True))