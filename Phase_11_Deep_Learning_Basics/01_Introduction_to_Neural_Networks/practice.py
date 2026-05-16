"""
Practice: Introduction to Neural Networks
Run this file, then modify the examples to test your understanding.
"""

def main():
    topic = "Introduction to Neural Networks"
    print(f"Studying: {topic}")
    examples = ["define", "practice", "test", "explain"]
    for step, action in enumerate(examples, start=1):
        print(f"{step}. {action.title()} the concept")

if __name__ == "__main__":
    main()
