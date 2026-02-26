# GPU/CUDA Primer: Understanding GPU Acceleration for Machine Learning

## What is a GPU?

A **GPU (Graphics Processing Unit)** is a specialized processor optimized for parallel computation. Unlike CPUs which excel at sequential tasks, GPUs can execute thousands of operations simultaneously, making them perfect for machine learning workloads.

### CPU vs GPU Architecture

| Aspect | CPU | GPU |
|--------|-----|-----|
| **Cores** | Few (4-64) | Many (1000s) |
| **Design** | Sequential, low latency | Parallel, high throughput |
| **Memory Bandwidth** | ~100 GB/s | ~1000+ GB/s |
| **Best Use** | General computing | Matrix ops, neural nets |

## Why GPUs Accelerate Machine Learning

Machine learning, especially deep learning, involves massive matrix operations:

- **Matrix multiplication**: W × X (millions of elements)
- **Element-wise operations**: Activation functions, element-wise products
- **Reduction operations**: Sum, mean, max across dimensions

GPUs excel at these because:

1. **Massive parallelism**: Thousands of cores compute different elements simultaneously
2. **Memory bandwidth**: Move huge amounts of data quickly between memory and compute
3. **Tensor operations**: Specialized instructions for linear algebra

### Example: Matrix Multiplication

```
CPU (sequential):  FOR i in rows: FOR j in cols: compute element (i,j)
                   → Takes O(n) time per element

GPU (parallel):    Compute all elements simultaneously
                   → Takes O(1) time (theoretically, with infinite cores)
```

## CUDA: GPU Programming for NVIDIA

**CUDA (Compute Unified Device Architecture)** is NVIDIA's platform for GPU computing:

- **CUDA Toolkit**: Compiler, libraries (cuBLAS, cuDNN), profiling tools
- **GPU Drivers**: Enable communication between CPU and GPU
- **PyTorch/TensorFlow**: Use CUDA under the hood automatically

### Installation (if GPU available)

```bash
# Check if you have an NVIDIA GPU
nvidia-smi

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Performance Comparison: CPU vs GPU

For a training loop with 1000 epochs on 100k samples:

| Device | Time | Speedup |
|--------|------|---------|
| CPU | ~500s | 1x |
| GPU (RTX 3090) | ~20s | **25x** |
| GPU (RTX 4090) | ~10s | **50x** |

Larger models and batch sizes → even greater GPU advantage.

## How PyTorch Uses the GPU

```python
import torch

# CPU tensor (default)
x_cpu = torch.randn(1000, 1000)

# Move to GPU
x_gpu = x_cpu.to('cuda')
# or
x_gpu = x_cpu.cuda()

# Automatic GPU computation
y_gpu = torch.matmul(x_gpu, x_gpu.t())

# Move result back to CPU
y_cpu = y_gpu.cpu()
```

## Memory Considerations

GPUs have **limited VRAM** (typically 6-80 GB):

- **Batch size**: Smaller batches on GPU due to memory limits
- **Model size**: Large models may not fit on a single GPU
- **Trade-off**: GPU is fast but memory-constrained

## When to Use GPU vs CPU

| Scenario | Device |
|----------|--------|
| Deep learning training | GPU |
| Inference on large models | GPU |
| Small models, few samples | CPU |
| Data preprocessing | CPU |
| Multinodal distributed training | Multiple GPUs |

## Multi-GPU & Distributed Training

For very large models/datasets:

- **Data parallelism**: Split batch across GPUs
- **Model parallelism**: Split model across GPUs
- **Frameworks**: Horovod, Ray, PyTorch DDP (Distributed Data Parallel)

## Summary

- **GPUs**: Thousands of cores, massive parallelism
- **CUDA**: NVIDIA's platform for GPU programming
- **Speed-up**: 10–100x faster for deep learning vs CPU
- **Trade-off**: Limited VRAM, requires GPU hardware
- **PyTorch**: Automatic GPU support with `.cuda()` or `.to('cuda')`

For this project: CPU is sufficient for learning; try GPU on Google Colab for comparison.
