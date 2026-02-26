import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser(description="Count words in a file")
    parser.add_argument('path', help='path to text file')
    args = parser.parse_args()
    
    try:
        with open(args.path, 'r', encoding='utf-8') as f:
            words = f.read().split()
        
        counts = Counter(words)
        for word, cnt in counts.most_common():
            print(f"{word}: {cnt}")
            
    except FileNotFoundError:
        print(f"Error: The file '{args.path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
