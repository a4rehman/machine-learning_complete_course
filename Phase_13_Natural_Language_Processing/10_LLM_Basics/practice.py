"""
Practice: LLM Basics
Run this file, then modify the examples to test your understanding.
"""

def main():
    topic = "LLM Basics"
    print(f"Studying: {topic}")
    examples = ["define", "practice", "test", "explain"]
    for step, action in enumerate(examples, start=1):
        print(f"{step}. {action.title()} the concept")

if __name__ == "__main__":
    main()
