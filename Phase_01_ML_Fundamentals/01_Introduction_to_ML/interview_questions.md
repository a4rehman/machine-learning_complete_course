# Interview Questions: Introduction to ML

### 🟢 Beginner Level

**Q1: Explain Machine Learning to a 5-year-old.**
**Answer:** "Imagine you are learning to ride a bike. At first, you fall a lot because you don't know how to balance. But every time you fall, your brain learns what *not* to do. Eventually, after enough practice, your brain figures out the rules of balance automatically. Machine Learning is exactly that—teaching computers to learn from practice (data) instead of giving them an instruction manual."

**Q2: What is the difference between Supervised and Unsupervised learning?**
**Answer:** In supervised learning, the dataset has an "answer key" (labels). The algorithm learns by comparing its guesses to the actual answers. In unsupervised learning, there are no labels; the algorithm's job is to find hidden structures or groupings in raw, unstructured data.

### 🟡 Intermediate Level

**Q3: What is the difference between Artificial Intelligence, Machine Learning, and Deep Learning?**
**Answer:** 
- **AI** is the broad concept of machines being able to carry out tasks in a way we consider "smart".
- **ML** is a subset of AI based on the idea that systems can learn from data and identify patterns with minimal human intervention.
- **Deep Learning** is a subset of ML that uses massive Artificial Neural Networks (inspired by the human brain) to solve highly complex problems like speech and image recognition.

**Q4: Can you explain the difference between Classification and Regression?**
**Answer:** Both fall under Supervised Learning. Classification predicts a discrete, categorical label (e.g., Cat vs Dog, Spam vs Not Spam). Regression predicts a continuous numerical value (e.g., House Price in dollars, Temperature in degrees).

### 🔴 FAANG Level (System & Product Sense)

**Q5: A Product Manager suggests using Deep Learning for every feature on the platform because "it's the most powerful." As an ML Engineer, how do you respond?**
**Answer:** "While Deep Learning is powerful, it is computationally expensive, requires massive amounts of labeled data, is prone to overfitting on small datasets, and acts as a 'black box' lacking interpretability. In production, we should always start with the simplest model (like Logistic Regression or Random Forests) to establish a baseline. If the simple model solves the business problem efficiently, Deep Learning introduces unnecessary engineering debt. We only scale to Deep Learning when the data complexity (like images or text) absolutely demands it."
