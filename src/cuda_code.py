import torch
import time

# Example: Matrix multiplication
matrix_size = 1000
a_cpu = torch.randn(matrix_size, matrix_size)
b_cpu = torch.randn(matrix_size, matrix_size)

start_time = time.time()
result_cpu = torch.matmul(a_cpu, b_cpu)
end_time = time.time()
print(f"CPU computation time: {end_time - start_time:.4f} seconds")

if torch.cuda.is_available():
    a_gpu = a_cpu.to("cuda")
    b_gpu = b_cpu.to("cuda")

    start_time = time.time()
    result_gpu = torch.matmul(a_gpu, b_gpu)
    torch.cuda.synchronize() # Wait for GPU operations to complete
    end_time = time.time()
    print(f"GPU computation time: {end_time - start_time:.4f} seconds")

