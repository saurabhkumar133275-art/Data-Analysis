# Day 20 - Data Visualization using Tableau

## Topics Covered

- Introduction to Tableau Data Visualization
- Connecting CSV Data to Tableau
- Exploring the Video Game Sales Dataset
- Dimensions and Measures
- Analyzing Video Game Sales
- Global Sales Calculation
- Sales Analysis by Genre
- Sales Analysis by Year
- Regional Sales Analysis
- Applying Filters in Tableau
- Profit Analysis
- Category and Sub-Category Analysis
- Creating Worksheets
- Creating a Dashboard

## Tool Used

- Tableau
- CSV Dataset

## Dataset Used

### 1. Video Game Sales Dataset

**File Name:** `vgsales.csv`

The dataset contains video game sales information across different regions.

### Fields Used

- Rank
- Name
- Platform
- Year
- Genre
- Publisher
- NA_Sales
- EU_Sales
- JP_Sales
- Other_Sales

## Practicals Performed

### Example 1 - Connecting the Dataset

- Open Tableau.
- Connect to the `vgsales.csv` file.
- Load the dataset.
- Explore the available dimensions and measures.
- Understand the structure of the dataset.

### Example 2 - Creating a Global Sales Calculation

Create a calculated field named `Global_Sales`.

**Formula:**

```text
[NA_Sales] + [EU_Sales] + [JP_Sales] + [Other_Sales]
