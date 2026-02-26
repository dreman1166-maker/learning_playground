# ML Learning Playground

This repository contains a set of tutorials and experiments to learn basic machine learning concepts using Python, PyTorch, scikit-learn, and other libraries.

## Contents

- `train_linear.py`: simple one-layer neural network training on synthetic data (y=2x).
- `requirements.txt`: pinned dependencies for reproducing the environment.
- Notebooks summarizing key concepts, tensor operations, training loops, data pipelines, and model evaluation.

## Getting Started

1. Install the dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run the training script:
   ```bash
   python ml_learning/train_linear.py
   ```
3. Explore notebooks for detailed explanations and examples.

## Topics covered

- Linear algebra essentials (vectors, matrices, dot product)
- Probability basics (mean, variance)
- PyTorch tensor operations and training loops
- GPU vs CPU differences (CUDA primer)
- scikit-learn classification (Iris dataset)
- Data pipelines with pandas
- Model evaluation: train/val/test split, confusion matrix, precision/recall
- Using pretrained transformer models from Hugging Face

Feel free to modify and extend the examples as you learn.
