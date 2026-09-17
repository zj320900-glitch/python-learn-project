people = list(range(1, 31))
index = 0
for _ in range(15):
    index = (index + 8) % len(people)
    print(f"{people.pop(index)}号下船了")


from collections import deque
people = deque(range(1,31))
print(people)
count = 0
while len(people) > 15:
    person = people.popleft()
    count += 1
    if count == 9:
        print(f"{person}号下船了")
        count = 0
    else:
        people.append(person)