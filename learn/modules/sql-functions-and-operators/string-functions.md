---
title: "String Functions"
---

String functions allow you to manipulate text data in various ways.

---

### CONCAT

The `CONCAT` function is used to combine two or more strings into one.

**Syntax:**

```sql
CONCAT(string1, string2, ...);
```

**Example:**
Imagine you have a table `Actors` with columns `FirstName` and `LastName`. You want to create a full name for each actor.

```sql
SELECT CONCAT(FirstName, ' ', LastName) AS FullName
FROM Actors;
```

**Real-life Example:**
Think of `CONCAT` as pasting together different pieces of text to form a complete message. For example, combining a first name and last name to form a full name.

---

### SUBSTRING

The `SUBSTRING` function extracts a portion of a string.

**Syntax:**

```sql
SUBSTRING(string, start, length);
```

**Example:**
You have a table `Movies` with a column `Title`. You want to extract the first three characters of each title.

```sql
SELECT SUBSTRING(Title, 1, 3) AS ShortTitle
FROM Movies;
```

**Real-life Example:**
Using `SUBSTRING` is like taking a specific segment of text from a paragraph, such as extracting the first word from a sentence.

---

### LENGTH

The `LENGTH` function returns the number of characters in a string.

**Syntax:**

```sql
LENGTH(string);
```

**Example:**
To find out the length of movie titles in the `Movies` table:

```sql
SELECT Title, LENGTH(Title) AS TitleLength
FROM Movies;
```

**Real-life Example:**
Using `LENGTH` is similar to counting the number of characters in a sentence, including spaces and punctuation.
