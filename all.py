import time
import random

# 计算矩阵每列与向量的内积
def dot_product_trivial(matrix, vector):
    n = len(matrix)
    result = [0] * n
    for j in range(n):  # 遍历矩阵的每一列
        for i in range(n):  # 计算每列与向量的内积
            result[j] += matrix[i][j] * vector[i]
    return result

def dot_product_optimized(matrix, vector):
    n = len(matrix)
    result = [0] * n
    for i in range(n):  # 遍历矩阵的每一行
        for j in range(n):  # 计算每行与向量的内积
            result[j] += matrix[i][j] * vector[i]
    return result

# 计算 n 个数的和
def sum_trivial(nums):
    result = 0
    for num in nums:
        result += num
    return result

def sum_optimized(nums):
    n = len(nums)
    if n <= 2:
        return sum_trivial(nums)
    else:
        mid = n // 2
        left_sum = sum_optimized(nums[:mid])
        right_sum = sum_optimized(nums[mid:])
        return left_sum + right_sum

# 生成测试数据
n = 1000
matrix = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
vector = [random.randint(1, 10) for _ in range(n)]
nums = [random.randint(1, 100) for _ in range(10000)]  # 将nums的长度增加到10000

# 性能测试
start_time = time.time()
result_trivial_dot_product = dot_product_trivial(matrix, vector)
end_time = time.time()
print("Trivial dot product algorithm time:", end_time - start_time)

start_time = time.time()
result_optimized_dot_product = dot_product_optimized(matrix, vector)
end_time = time.time()
print("Optimized dot product algorithm time:", end_time - start_time)

start_time = time.time()
result_trivial_sum = sum_trivial(nums)
end_time = time.time()
print("Trivial sum algorithm time:", end_time - start_time)

start_time = time.time()
result_optimized_sum = sum_optimized(nums)
end_time = time.time()
print("Optimized sum algorithm time:", end_time - start_time)
