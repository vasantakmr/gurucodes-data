---
title: "Getting Started: Excel Basics [Week 17]"
---
### 2.1 Understanding the Excel Interface
Begin by familiarizing yourself with Excel's user interface:
- **Workbook**: The entire file you work in.
- **Worksheet**: A single tab (or sheet) inside the workbook.
- **Cell**: The intersection of a row and a column where you input data.
- **Ribbon**: The menu with tools like Home, Insert, Formulas, etc.

### 2.2 Basic Operations in Excel
- **Entering Data**: Inputting data into cells.
- **Copy/Paste**: Use Ctrl+C and Ctrl+V for fast data entry.
- **Formatting Cells**: Learn how to format cells to display numbers, text, dates, or currency.

### 2.3 Basic Excel Formulas
Start with the most commonly used formulas:
- **SUM**: Adds a range of cells.  
  `=SUM(A1:A10)`
- **AVERAGE**: Finds the average of a range.  
  `=AVERAGE(B1:B10)`
- **MIN/MAX**: Finds the smallest/largest number in a range.  
  `=MIN(C1:C10)`  
  `=MAX(C1:C10)`
- **COUNT/COUNTA**: Counts the number of cells with numbers or any data.  
  `=COUNT(D1:D10)`  
  `=COUNTA(E1:E10)`

### 2.4 Formula Mastery
Master essential formulas to perform calculations, summarize data, and create dynamic reports. Key formulas include:

- **SUM**: Add a range of numbers.  
  `=SUM(A1:A10)`
  
- **COUNT**: Count the number of cells with numerical data.  
  `=COUNT(A1:A10)`

- **AVERAGE**: Calculate the average of a range.  
  `=AVERAGE(A1:A10)`

- **SUMIFS**: Sum cells based on multiple criteria.  
  `=SUMIFS(sum_range, criteria_range1, criteria1)`

- **COUNTIFS**: Count cells based on multiple criteria.  
  `=COUNTIFS(range1, criteria1, range2, criteria2)`

- **VLOOKUP**: Lookup values vertically in a table.  
  `=VLOOKUP(value, table, col_index, [range_lookup])`

- **HLOOKUP**: Lookup values horizontally.  
  `=HLOOKUP(value, table, row_index, [range_lookup])`

- **XLOOKUP**: A more flexible replacement for VLOOKUP.  
  `=XLOOKUP(lookup_value, lookup_array, return_array)`

- **INDEX & MATCH**: Combine these two functions for flexible lookups.  
  `=INDEX(range, row_num, col_num)`  
  `=MATCH(lookup_value, lookup_array, match_type)`

- **IF**: Perform logical comparisons.  
  `=IF(A1 > 100, "Pass", "Fail")`

- **IFERROR**: Handle errors in formulas.  
  `=IFERROR(A1/B1, "Error")`

- **AND/OR/NOT**: Combine logical conditions.  
  `=AND(A1>100, B1<200)`  
  `=OR(A1>100, B1>100)`  
  `=NOT(A1>100)`

- **Nested Functions**: Combine multiple functions in a single formula (e.g., nested IFs).  
  `=IF(A1>100, "High", IF(A1>50, "Medium", "Low"))`

- **ARRAY Formulas**: Perform calculations over multiple ranges.  
  `=SUM(IF(A1:A10 > 100, 1, 0))`

- **LET**: Assign names to calculation results for readability and performance.  
  `=LET(x, A1*B1, x+100)`

- **SUMPRODUCT**: Multiply arrays and sum the results.  
  `=SUMPRODUCT(A1:A10, B1:B10)`

- **INDIRECT**: Reference a cell indirectly.  
  `=INDIRECT("A" & B1)`

- **CHOOSE**: Select from a list of values.  
  `=CHOOSE(index, value1, value2, ...)`

- **OFFSET**: Return a reference to a range that is a specified number of rows and columns away from a cell.  
  `=OFFSET(reference, rows, cols)`

- **LEFT/RIGHT**: Extract characters from text.  
  `=LEFT(A1, 3)`  
  `=RIGHT(A1, 3)`