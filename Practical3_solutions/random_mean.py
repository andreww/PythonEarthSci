import random

gen = random.Random()
gen.seed()
tot = 0
for i in range(100):
    tot = tot + gen.random()

print tot, tot/100
