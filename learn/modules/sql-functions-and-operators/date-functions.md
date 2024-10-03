---
title: "Date Functions"
---

Date functions are used to manipulate date and time values.

---

### CURRENT_DATE

The `CURRENT_DATE` function returns the current date.

**Syntax:**

```sql
SELECT CURRENT_DATE;
```

**Example:**
To get the current date in a report:

```sql
SELECT CURRENT_DATE AS TodayDate;
```

**Real-life Example:**
Using `CURRENT_DATE` is like checking today’s date on your calendar.

---

### DATEADD

The `DATEADD` function adds a specified number of intervals to a date.

**Syntax:**

```sql
DATEADD(interval, number, date);
```

**Example:**
Adding 7 days to the current date:

```sql
SELECT DATEADD(day, 7, CURRENT_DATE) AS NextWeek;
```

**Real-life Example:**
Using `DATEADD` is like scheduling a reminder for a week from today.

---

### DATEDIFF

The `DATEDIFF` function returns the difference between two dates.

**Syntax:**

```sql
DATEDIFF(interval, start_date, end_date);
```

**Example:**
Calculating the number of days between the release date and today's date for movies in the `Movies` table:

```sql
SELECT Title, DATEDIFF(day, ReleaseDate, CURRENT_DATE) AS DaysSinceRelease
FROM Movies;
```

**Real-life Example:**
Using `DATEDIFF` is like calculating the number of days between two events, such as the number of days left until a movie release.
