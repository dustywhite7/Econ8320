<!--
$theme: gaia
template: invert
-->

# Week 7 - Pandas, SQL

---

### Data Handling

What are the ways that we have learned so far to handle data?

- Flat Files
- Numpy arrays
- Lists of lists
- Dictionaries

None of these are particularly conducive to data exploration and quick manipulation

---

### Introducing Data Frames

When we want to manipulate data in a clean and efficient manner, we want to start thinking about data in terms of vectors:

- Each variable can be considered a vector
- Operations on a variable can be applied to all observations uniformly
- We can quickly reduce the number of variables for specific questions

---

### Introducing Data Frames

In Python, the `pandas` library contains the necessary code to begin working with Data Frames. It is dependent on many functions in the `numpy` library.

<br>

```python
import pandas as pd # Import the library for use
```

---

### Creating a Data Frame

Create an empty Data Frame:

```python
data = pd.DataFrame()
```

A Data Frame is a class that accepts the following:
- data (typically as a numpy array)
- index (if you don't want this to be created for you)
- columns (so you can name your variables)
- dtype (specify the type of data)
- copy (whether or not the data should be copied)

---

### Creating a Data Frame

We can also use pandas to easily read many types of files, and import them as Data Frames:

```python
# CSV
data = pd.read_csv(your_filename_here.csv)
# or Excel Files
data = pd.read_excel(your_filename_here.xlsx)
# or Stata Data
data = pd.read_stata(your_filename_here.dta)
# or SAS Data
data = pd.read_sas(your_filename_here.sas7bdat)
# or SQL Queries
data = pd.read_sql(your_query_here, your_connection_here)
# and many others!
```

---

### Referencing a Single Column

To access a list of all of the column names in your Data Frame:

```python
data.columns
```

To then reference a single column:

```python
data['Column_Name']
```

To reference several columns, pass a list of column names:
```python
data[['Column1','Column2']]
```

---

### Slicing the Data Frame

Two selection (or slicing) tools allow us to quickly subset our data.

```python
data.iloc[row_selection, column_selection]
```

With the `.iloc` method, we can provide **integer**-based selections, or choose to select all rows or columns, and only subset on a single dimension.

```python
data.iloc[:, 0] # Selects all rows, and first column
```

---

### Slicing the Data Frame

Two selection (or slicing) tools allow us to quickly subset our data.

```python
data.loc[row_selection, column_selection]
```

With the `.loc` method (now with no `i`), we can provide **name**-based selections, choose to select all rows or columns, and create subsets based on conditions.

```python
data.iloc[:, 'ColumnName'] # Selects all rows, one column
```

---

### Slicing the Data Frame

Two selection (or slicing) tools allow us to quickly subset our data.

```python
data.loc[row_selection, column_selection]
```

With the `.loc` method (now with no `i`), we can provide **name**-based selections, choose to select all rows or columns, and create subsets based on conditions.

```python
data.iloc[data['Column1'] == some_value, :]
# Selects only the observations (rows) where the
#   condition is met
```