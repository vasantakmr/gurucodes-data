---
title: "Intermediate Excel: Key Skills for Data Analysts [Week 17]"
---

### 3.1 Data Cleaning
As a data analyst, cleaning messy data is critical:
- **Remove Duplicates**: Remove repeated rows.  
  Go to `Data > Remove Duplicates`.
- **Text to Columns**: Split text into multiple columns (e.g., separating first and last names).  
  Go to `Data > Text to Columns`.
- **Find & Replace**: Quickly replace specific values.  
  Use `Ctrl + H`.

### 3.2 Conditional Formatting
Conditional formatting highlights cells based on conditions, making patterns in data more visible.
- Highlight cells greater than a specific value, lower than the average, or duplicate values.  
  Go to `Home > Conditional Formatting`.

### 3.3 Sorting and Filtering Data
Sorting and filtering allow you to manipulate large datasets.
- **Sort**: Arrange data in ascending/descending order based on a column.  
  Go to `Data > Sort`.
- **Filter**: Display only the rows that meet certain criteria (e.g., sales > 1000).  
  Go to `Data > Filter`.

### 3.4 Excel Tables
Convert a range into an **Excel Table** for better data management:
- Auto-filters, column sorting, and total rows are part of tables.
- `Ctrl + T` to create a table.  
  Go to `Insert > Table`.

### 3.5 Logical and Lookup Functions
- **IF**: Perform logical comparisons.  
  `=IF(A1>100, "Pass", "Fail")`
- **VLOOKUP**: Lookup values vertically in a table.  
  `=VLOOKUP(value, table, col_index, [range_lookup])`
- **HLOOKUP**: Lookup values horizontally in a table.
  `=HLOOKUP(value, table, row_index, [range_lookup])`
- **INDEX & MATCH**: More flexible lookup functions compared to VLOOKUP.
  `=INDEX(range, row_num, col_num)`  
  `=MATCH(lookup_value, lookup_array, match_type)`
