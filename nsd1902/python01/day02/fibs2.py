fib = [0, 1]

n = int(input('长度: '))

for i in range(n - 2):
    # 将列表中最后两项之和追加到列表尾部
    fib.append(fib[-1] + fib[-2])

print(fib)
