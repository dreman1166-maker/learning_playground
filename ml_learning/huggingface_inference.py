"""
Hugging Face Pretrained Model Inference: Text Classification
Note: Due to environment constraints, this demonstrates the concept.
In practice, use: pip install transformers torch
Then uncomment the pipeline code below.
"""

print("=" * 60)
print("Hugging Face Pretrained Model Inference")
print("=" * 60)
print()

# Demonstration of how to use Hugging Face (for environments with proper setup)
print("Code Example (uncomment in proper environment):")
print("-" * 60)
example_code = '''
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment = pipeline("sentiment-analysis")

# Test examples
test_sentences = [
    "I absolutely love this product! It's amazing!",
    "This is terrible. I hate it.",
    "The movie was okay, nothing special.",
]

for sentence in test_sentences:
    result = sentiment(sentence)
    label = result[0]['label']
    score = result[0]['score']
    print(f"Text: {sentence}")
    print(f"  → Label: {label}, Confidence: {score:.4f}")
'''
print(example_code)
print("-" * 60)
print()

# Demonstrate manual classification (simulating what HF does)
print("=" * 60)
print("SIMULATED SENTIMENT ANALYSIS (Manual)")
print("=" * 60)
print()

# Simple word-based sentiment (demonstrates the concept)
positive_words = {"love", "amazing", "great", "excellent", "best", "wonderful", "perfect"}
negative_words = {"hate", "terrible", "awful", "bad", "worst", "horrible", "disgusting"}

test_sentences = [
    "I absolutely love this product! It's amazing!",
    "This is terrible. I hate it.",
    "The movie was okay, nothing special.",
    "Best experience ever!",
    "Worst purchase I've ever made."
]

for sentence in test_sentences:
    words = sentence.lower().split()
    pos_count = sum(1 for w in words if w.strip('!?,;:') in positive_words)
    neg_count = sum(1 for w in words if w.strip('!?,;:') in negative_words)
    
    if pos_count > neg_count:
        label = "POSITIVE"
    elif neg_count > pos_count:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    
    print(f"\nText: {sentence}")
    print(f"  → Label: {label}")

print()
print("=" * 60)
print("Key Learning Points")
print("=" * 60)
print("""
1. Hugging Face transformers provide pretrained models for:
   - Sentiment analysis, text classification, named entity recognition,
     question answering, machine translation, summarization, etc.

2. Pipeline makes inference simple:
   model = pipeline("task-name")
   result = model(text)

3. Models are cached locally after first download (~400MB for BERT)

4. For GPU acceleration:
   model = pipeline("sentiment-analysis", device=0)
   (device=0 means first GPU)

5. Transfer learning: Use pretrained models as starting point
   for your own classification tasks.
""")
