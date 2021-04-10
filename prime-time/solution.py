class Solver:
    def solve(self, configs):
        self.answer = 0
        
        cards = []
        for config in configs:
            cards += [config[0]] * config[1]
        
        self.perm(cards, 0, 0, 1)
        
        return self.answer
        
    def perm(self, cards, index, summ, product):
        if not index < len(cards):
            if summ == product:
                self.answer = summ
                return True
            return False
        
        if self.perm(cards, index+1, summ + cards[index], product) or \
            self.perm(cards, index+1, summ, product * cards[index]): return True
        return False

t = int(input())
for i in range(1, t+1):
    m = int(input())
    cards = []
    for _ in range(m):
        c, n = input().split(" ")
        cards.append((int(c), int(n)))
    
    print('Case #{}: {}'.format(i, solve(cards)))
