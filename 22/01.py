class Ranking:
    size: int
    arr: list[int]

    def __init__(self, size):
        self.size = size
        self.arr = []

    def add(self, el: int):
        if len(self.arr) < self.size:
            self.arr.append(el)
        if self.arr[-1] < el:
            self.arr[-1] = el
        self.arr = sorted(self.arr, reverse=True)

cum = 0
ranking = Ranking(3)
with open('input_01.txt') as f:
    for line in f.read().splitlines():
        if line:
            cum += int(line)
        else:
            ranking.add(cum)
            cum = 0

print(ranking.arr[0])
print(sum(ranking.arr))
