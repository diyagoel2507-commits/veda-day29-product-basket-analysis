# VEDA Day 29 - Product Basket Analysis

## Objective
Find products frequently purchased together and introduce association-style analysis using Python and Pandas.

## Tools
- Python
- Pandas
- NumPy

## Dataset
`data/retail_transactions.csv` contains transaction-level retail data with: 
- `OrderID` - unique order identifier
- `Product` - product purchased in that order

## Methodology
1. Group products by `OrderID` to create baskets.
2. Generate unique product pairs using `combinations()`.
3. Count how many orders contain each pair.
4. Calculate pair support:
   `Support = Orders containing pair / Total orders × 100`
5. Sort pairs to identify the most frequently purchased combinations.
6. Generate simple product recommendations from the strongest pair relationships.

## Deliverables
- `outputs/top_product_pairs.csv` - top product combinations
- `outputs/product_pairs.csv` - all product pair results
- `outputs/recommendations.csv` - product recommendation results
- `src/product_basket_analysis.py` - reusable analysis script

## Key Insight
Basket analysis helps a business understand which products tend to appear in the same order. These relationships can be used for product recommendations, cross-selling, bundle offers, and store or website placement.

## How to Run
```bash
pip install pandas numpy
python src/product_basket_analysis.py
```

## Interview Questions

### What is market-basket analysis?
Market-basket analysis is a technique used to identify products that are frequently purchased together in the same transaction.

### Why use Order ID?
Order ID defines the transaction or basket. It tells us which products were purchased together by the same customer in the same order.

### Why exclude self-pairs?
A product paired with itself does not provide useful association information. Therefore, combinations are generated only between two different products.
