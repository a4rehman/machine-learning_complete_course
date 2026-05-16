# Exercises: Pandas Mastery

### Beginner Problems

**Exercise 1: Loading Data**
Write the Pandas code to load a CSV file named `housing.csv` into a DataFrame. Print the first 10 rows and the names of all the columns.

**Exercise 2: loc vs iloc**
Given a DataFrame `df`:
1. Use `.iloc` to select the 5th row in the dataset.
2. Use `.loc` to select the column named "Price".

---

### Intermediate Problems

**Exercise 3: Handling Missing Values**
You have a DataFrame `sales_df` with a column `Revenue` containing several `NaN` values. 
Write the code to fill these missing values with the **median** of the `Revenue` column, ensuring the change happens *in-place* (modifying the original DataFrame without reassigning).

**Exercise 4: GroupBy Analytics**
You have a DataFrame `ecommerce_df` with columns: `['Country', 'Category', 'Sales']`.
Write the code to find the **total (sum) sales** for each `Category` within each `Country`. (Hint: group by multiple columns).

---

### Advanced Problems

**Exercise 5: Merge and Join**
You have two DataFrames:
- `users`: `['user_id', 'name', 'signup_date']`
- `orders`: `['order_id', 'user_id', 'amount']`

Write the code to perform a **Left Join** combining these tables so that all users are kept in the final DataFrame, even if they have made 0 orders. Fill any `NaN` values in the `amount` column with `0`.

**Exercise 6: The Apply Trap**
A junior engineer wrote the following code to calculate a 10% tax on sales:
```python
def calc_tax(row):
    return row['sales'] * 0.10
df['tax'] = df.apply(calc_tax, axis=1)
```
This is taking 10 minutes to run on 5 million rows. Rewrite this operation using standard Pandas vectorization so it runs in less than 1 second.
