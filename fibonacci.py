# 递归方式实现斐波那契数列
def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)

# 迭代方式实现斐波那契数列（更高效）
def fib_iterative(n: int) -> int:
    if n <= 1:
        return n
    
    prev = 0
    current = 1
    
    for i in range(2, n + 1):
        temp = current
        current = prev + current
        prev = temp
    
    return current

# 使用记忆化优化的递归实现
def fib_memoized(n: int, memo: dict = None) -> int:
    if memo is None:
        memo = {}
    
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fib_memoized(n - 1, memo) + fib_memoized(n - 2, memo)
    return memo[n]

# 测试不同实现
if __name__ == '__main__':
    import time
    
    print('计算斐波那契数列的前10个数：')
    for i in range(10):
        print(f'F({i}) = {fib_iterative(i)}')
    
    print('\n比较不同实现方式的第20个斐波那契数：')
    
    # 测试递归方式
    start_time = time.time()
    result = fib_recursive(20)
    end_time = time.time()
    print(f'递归结果: {result}')
    print(f'递归方式耗时: {(end_time - start_time) * 1000:.2f}ms')
    
    # 测试迭代方式
    start_time = time.time()
    result = fib_iterative(20)
    end_time = time.time()
    print(f'迭代结果: {result}')
    print(f'迭代方式耗时: {(end_time - start_time) * 1000:.2f}ms')
    
    # 测试优化递归方式
    start_time = time.time()
    result = fib_memoized(20)
    end_time = time.time()
    print(f'优化递归结果: {result}')
    print(f'优化递归方式耗时: {(end_time - start_time) * 1000:.2f}ms')