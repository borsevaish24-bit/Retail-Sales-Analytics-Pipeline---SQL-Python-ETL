# Retail-Sales-Analytics-Pipeline SQL-Python-ETL

## Overview
End-to-end data analytics project analysing 9,994 retail sales 
transactions across 4 regions, 3 product categories, and 17 
subcategories. The project follows a complete ETL pipeline 
architecture, raw data is extracted, cleaned, and loaded into 
a structured database before all analysis is performed via SQL.

## Project architecture
```
Sample - Superstore.csv
         ↓
   pipeline.py        # cleans and transforms raw data
         ↓
superstore_cleaned.db # structured SQLite database
         ↓
   analysis.ipynb     # SQL queries + visualisations
         ↓
   5 business questions answered with charts and findings
```

## How to run
1. Clone this repository
2. Place `Sample - Superstore.csv` in the project folder
3. Run the pipeline first:
```bash
   python pipeline.py
```
4. Open and run `analysis.ipynb` in Jupyter Notebook

## Tools and technologies
- Python (pandas, matplotlib, seaborn)
- SQL (SQLite via sqlite3)
- Jupyter Notebook
- Git

## Business questions answered

### 1. Which region generates the most revenue and profit?
| Region | Revenue | Profit | Margin |
|--------|---------|--------|--------|
| West | $725,458 | $108,418 | 14.94% |
| East | $678,781 | $91,523 | 13.48% |
| South | $391,722 | $46,749 | 11.93% |
| Central | $501,240 | $39,706 | 7.92% |

West leads in both revenue and absolute profit. Central has 
the weakest margin at 7.92% despite being third in revenue.

### 2. What is the monthly revenue trend?
Revenue shows consistent year-on-year growth across the 
4-year period, with notable Q4 spikes — particularly in 
November and December — suggesting strong seasonal demand.

### 3. Which category has the best profit margin?
| Category | Revenue | Profit | Margin |
|----------|---------|--------|--------|
| Technology | $836,154 | $145,455 | 17.40% |
| Office Supplies | $719,047 | $122,491 | 17.04% |
| Furniture | $742,000 | $18,451 | 2.49% |

Furniture generates $742,000 in revenue — second highest — 
but delivers only 2.49% profit margin. Technology and Office 
Supplies both exceed 17% margin, making Furniture a critical 
area for pricing and cost review.

### 4. At what discount level does profit turn negative?
| Discount | Avg Profit per Order |
|----------|----------------------|
| 0% | +$66.90 |
| 10% | +$71.56 |
| 20% | +$24.70 |
| 30% | -$50.24 |
| 40% | -$111.93 |
| 50% | -$298.70 |

Profitability turns negative between 20% and 30% discount. 
Orders with 50% discount generate an average loss of $298.70 
per order. 1,393 orders (13.9% of all orders) carry discounts 
of 30% or more — representing a significant source of profit 
erosion.

### 5. Which subcategories are losing money?
| Subcategory | Total Profit | Total Sales |
|-------------|-------------|-------------|
| Tables | -$17,725 | $206,966 |
| Bookcases | -$3,473 | $114,880 |
| Supplies | -$1,189 | $46,674 |

Tables generate $206,966 in sales but produce a net loss of 
$17,725 — a margin of -8.6%. Combined with Bookcases and 
Supplies, these three subcategories collectively lose $22,387 
despite generating $368,520 in revenue.

## Key findings and business recommendations

1. **Discount policy needs revision** : discounts above 20% 
   destroy profit. A hard cap at 20% across all categories 
   would protect margins while remaining competitive.

2. **Furniture requires urgent review** : at 2.49% margin, 
   Furniture is barely profitable as a category. Tables alone 
   lose $17,725. Pricing, supplier costs, or product mix 
   changes are warranted.

3. **West and East are the strongest markets** : combined they 
   represent 58% of total revenue and 62% of total profit. 
   Investment in these regions has the highest return.

4. **Technology is the most efficient category** : highest 
   revenue ($836,154) and highest margin (17.40%). Increasing 
   Technology's share of the product mix would improve overall 
   profitability.

5. **Central region underperforms** : $501,240 revenue but 
   only 7.92% margin, the lowest of all regions. Operational 
   costs or pricing strategy in Central warrants investigation.
   


