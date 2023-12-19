import pandas as pd

data = {
    'Description': ['Coffee at Starbucks', 'Grocery shopping at Walmart', 'Flight to NYC', 'Uber ride', 'Netflix subscription', 'Something else'],
    'Amount': [5.75, 76.32, 225.00, 13.45, 15.99, 100]
}
expenses_df = pd.DataFrame(data)

category_rules = {
    'Food & Drink': ['Coffee', 'Grocery', 'Restaurant'],
    'Travel': ['Flight', 'Uber', 'Hotel'],
    'Entertainment': ['Netflix', 'Spotify', 'Cinema']
}


def categorize_expenses(expenses_df: pd.DataFrame, category_rules: dict, default_category: str) -> pd.DataFrame:

  categories = []

  for i in expenses_df.index:
      category = default_category
      for key in category_rules.keys():
          description_set = set(expenses_df['Description'][i].split())
          match_set = description_set & set(category_rules[key])
          if match_set:
              category = key
              continue
      categories.append(category)

  expenses_df['Category'] = categories
  return expenses_df




# Expected output

#               Description  Amount       Category
# 0     Coffee at Starbucks    5.75   Food & Drink
# 1  Grocery shopping at...   76.32   Food & Drink
# 2           Flight to NYC  225.00         Travel
# 3               Uber ride   13.45         Travel
# 4     Netflix subscription   15.99  Entertainment

categorized_df = categorize_expenses(expenses_df, category_rules, 'Miscellaneous')
print(categorized_df)