class BinaryIndexTree:
    def __init__(self, size):
        self.size = size
        self.array = [0] * (size + 1)
    
    def add(self, x, a):
        index = x
        while index <= self.size:
            self.array[index] += a
            index += index & (-index)
    
    def sum(self, x):
        index = x
        ans = 0
        while index > 0:
            ans += self.array[index]
            index -= index & (-index)
        return ans

    def least_upper_bound(self, value):
        if self.sum(self.size) < value:
            return -1
        elif value <= 0:
            return 0

        m = 1
        while m < self.size:
            m *= 2

        k = 0
        k_sum = 0
        while m > 0:
            k0 = k + m
            if k0 < self.size:
                if k_sum + self.array[k0] < value:
                    k_sum += self.array[k0]
                    k += m
            m //= 2
        if k < self.size:
            return k + 1
        else:
            return -1

def main():
    N, K = map(int, input().split())
    ab = []
    max_a = 0
    for _ in range(N):
        a, b = map(int, input().split())
        ab.append((a, b))
        max_a = max(max_a, a)
    
    bit = BinaryIndexTree(max_a)
    for a, b in ab:
        bit.add(a, b)
    
    k = bit.least_upper_bound(K)
    print(k)
   
if __name__ == "__main__":
    main()