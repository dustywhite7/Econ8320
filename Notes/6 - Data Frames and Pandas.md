# Data Frames and Pandas

Data Frames are the standard method for opening, storing, and manipulating data within the Python environment. They are heavily inspired by the Data Frames of the `R` programming language, and have many similar functions. While Data Frames have a huge number of features, we will focus on those that are most beneficial to a new user, and will come in handy for almost any data-focused project.

In order to create and use Data Frames, we will need to import a specific library containing the code and functionality of Data Frames. In Python, this functionality resides in the `pandas` package. We will use `pandas` throughout this lesson, and it will become integral to our data work for the remainder of the course.

## Creating Data Frames

Obviously, the first thing we need to learn is how to *create* a Data Frame. We have many options, and each is useful in specific contexts that we will discuss as we describe how to implement each option.

### Reading data from a CSV

The first, and most common, way that we will create a Data Frame is to import data from a CSV. The `pandas` library contains functionality that enables us to use a **single-line** import statement to collect data from a CSV and transform that data into a Data Frame:


```python
# Import the pandas library
import pandas as pd

# Choose data to import
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/footballAttendance.csv")
```

As you can see above, it is helpful to import libraries with abbreviated names. In almost all cases, `pandas` is imported as `pd`. There is no reason that this **has** to happen, but it becomes convenient in large projects to shorten the names of libraries that will be used regularly in order to minimize the amount of code that must be written, read, and maintained.

The `read_csv` function included in the `pandas` library enables us to read a CSV file at any location that we can access. In this case, I have read a CSV file that is stored on Github (so that you can also access the file without needing to download anything!). The `read_csv` function will take care of the hard work of finding our header row, importing the headers as column names, will attempt to identify the delimiter (and typically will succeed if you used tabs or commas as your delimiter), and will determine the type of information that is stored in each row. We can then use the `head` method to check that the first rows of our Data Frame match our expectations:


```python
# Retrieving the first 10 rows of our data using the head method
data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Albania</td>
      <td>1</td>
      <td>FK Partizani Tiranë</td>
      <td>2.986</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>2</td>
      <td>KF Tiranë</td>
      <td>2.308</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>3</td>
      <td>KF Skënderbeu Korçë</td>
      <td>1.833</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Albania</td>
      <td>4</td>
      <td>KS Flamurtari Vlorë</td>
      <td>1.624</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albania</td>
      <td>5</td>
      <td>KF Teuta Durrës</td>
      <td>0.889</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Albania</td>
      <td>6</td>
      <td>KS Kastrioti Krujë</td>
      <td>0.865</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Albania</td>
      <td>7</td>
      <td>FK Kukësi</td>
      <td>0.633</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Albania</td>
      <td>8</td>
      <td>KF Laçi</td>
      <td>0.656</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Albania</td>
      <td>9</td>
      <td>KS Luftëtari Gjirokastër</td>
      <td>0.694</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Albania</td>
      <td>10</td>
      <td>FC Kamza</td>
      <td>0.760</td>
      <td>2019</td>
    </tr>
  </tbody>
</table>
</div>



The data looks like it has been imported correctly!

### Reading Excel Data

Reading Excel data is almost identical to reading data from a CSV. We can even [choose which sheet to read into a Data Frame, or choose to create a dictionary of data frames from multiple sheets](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html). The function is compatible with both `.xls` and `.xlsx` formatted files.


```python
# If you get an error, you might need to install the xlrd library using the line below
# !pip install xlrd # Uncomment this line if needed

# Read some Excel data into a Data Frame (will overwrite the previous Data Frame)
data = pd.read_excel("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/SportsLeagues.xlsx")

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>League</th>
      <th>Founded</th>
      <th>Folded</th>
      <th>Duration</th>
      <th>Sport</th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>National Association of Baseball Players (NABP)</td>
      <td>1857</td>
      <td>1870.0</td>
      <td>5110</td>
      <td>Baseball</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>National Association of Professional Baseball ...</td>
      <td>1871</td>
      <td>1875.0</td>
      <td>1825</td>
      <td>Baseball</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>National League of Professional Baseball Clubs...</td>
      <td>1876</td>
      <td>NaN</td>
      <td>52925</td>
      <td>Baseball</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>American Association (Merged with NL)</td>
      <td>1882</td>
      <td>1891.0</td>
      <td>3650</td>
      <td>Baseball</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Western League of Professional Baseball Clubs ...</td>
      <td>1885</td>
      <td>1899.0</td>
      <td>5475</td>
      <td>Baseball</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### Using SQL to Extract Data

Connecting to a SQL Server provides another opportunity for us to be able to retrieve information. Python has connectors that will allow it to work with nearly any type of SQL server, as well as with NoSQL and other flavors of database. We can use the `read_sql` function built into `pandas` together with a connector to be able to access data stored in this fashion.



```python
# Import SQLite3 connector library
import sqlite3

# Establish a connection to a database that was downloaded from Github 
#     (https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/exampleDatabase.db)
conn = sqlite3.connect("exampleDatabase.db")

# Write a SQL statement to select data from the database
select = "SELECT * FROM acs LIMIT 100"

# Read some data into a Data Frame (will overwrite the previous Data Frame)
# Note that we need to provide both a select statement as well as a database connection!
data = pd.read_sql(select, conn)

# Look at the first 5 rows
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>cpi99</th>
      <th>region</th>
      <th>statefip</th>
      <th>countyfips</th>
      <th>metro</th>
      <th>city</th>
      <th>citypop</th>
      <th>farm</th>
      <th>...</th>
      <th>labforce</th>
      <th>occ2010</th>
      <th>ind1990</th>
      <th>inctot</th>
      <th>ftotinc</th>
      <th>incwage</th>
      <th>incbus00</th>
      <th>incss</th>
      <th>incwelfr</th>
      <th>incinvst</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16873974</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>6515</td>
      <td>60</td>
      <td>50000</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16873975</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16873976</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16873977</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16873978</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 61 columns</p>
</div>



The requirements for connecting to databases will vary depending on the type of database that you are attempting to access, and covering all possibilities is outside of the scope of this course. In this case, we downloaded (and uploaded to Mimir) a `.db` file containing a small SQLite3 database. We then connected to that database using the `sqlite3` library.

Once we were connected, we could use SQL syntax to extract data from the table of interest and read the returned values into a Data Frame. At this point, we would be able to treat the extracted data **exactly** the same as data that we read from a CSV. The `pandas` library takes data from **many** different file types, and the resulting data is always in a Data Frame, with all of the functionality that we will explore below.

### Creating Data Frames from Scratch

Another option that we have is to create a Data Frame from scratch, which may be useful when collecting data from simulations or web scraping. Below, we will create a Data Frame, name the columns, and enter data using a dictionary:


```python
# Create the actual records for the Data Frame
records = {
    'Name' : ['Dusty', 'Mindy'],
    'Age' : [32, 30],
    'Education' : ['Doctorate', 'Bachelor']
}

# Creating an empty Data Frame (will overwrite the previous Data Frame)
data = pd.DataFrame(data = records)

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Age</th>
      <th>Education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Dusty</td>
      <td>32</td>
      <td>Doctorate</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Mindy</td>
      <td>30</td>
      <td>Bachelor</td>
    </tr>
  </tbody>
</table>
</div>



## Navigating Data Frames

It's also important to be able to navigate a Data Frame in order to find specific subsets of data, or to find observations that meet predetermined conditions. This will allow us to choose the data that fits our research question or model specification by selecting variables *or* observations.

### Finding a Single Column

Selecting a column can be done in several ways. The quickest way to select columns is to use slicing syntax similar to the way that we choose subsets of dictionaries or lists:


```python
# Import data
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/footballAttendance.csv")

# Select a single variable from the data frame
data['Team']
```




    0               FK Partizani Tiranë
    1                         KF Tiranë
    2               KF Skënderbeu Korçë
    3               KS Flamurtari Vlorë
    4                   KF Teuta Durrës
    5                KS Kastrioti Krujë
    6                         FK Kukësi
    7                           KF Laçi
    8          KS Luftëtari Gjirokastër
    9                          FC Kamza
    10              KF Skënderbeu Korçë
    11              KF Vllaznia Shkodër
    12              KS Flamurtari Vlorë
    13              FK Partizani Tiranë
    14         KS Luftëtari Gjirokastër
    15                        FK Kukësi
    16                         FC Kamza
    17                  KF Teuta Durrës
    18                          KF Laçi
    19                       KS Lushnja
    20              KF Skënderbeu Korçë
    21              KS Flamurtari Vlorë
    22                        KF Tiranë
    23              FK Partizani Tiranë
    24              KF Vllaznia Shkodër
    25                        FK Kukësi
    26         KS Luftëtari Gjirokastër
    27                          KF Laçi
    28                  KF Teuta Durrës
    29               KS Korabi Peshkopi
                        ...            
    22001              Holywell Town FC
    22002                CPD Bae Cemaes
    22003              Cwmbran Town AFC
    22004                  Afan Lido FC
    22005    Briton Ferry Llansawel AFC
    22006             Llansantffraid FC
    22007             Inter Cardiff AFC
    22008             Llanelli Town AFC
    22009                Ton Pentre AFC
    22010                 Ebbw Vale AFC
    22011               CP Dinas Bangor
    22012          CPD Tref Aberystwyth
    22013                      CPD Rhyl
    22014                   Newtown AFC
    22015         Fflint Town United FC
    22016                Ton Pentre AFC
    22017         Barry Town United AFC
    22018                   CPD Caersws
    22019                CPD Porthmadog
    22020              Holywell Town FC
    22021                  Afan Lido FC
    22022             The New Saints FC
    22023              Connah's Quay FC
    22024         Bwrdeisstref Conwy FC
    22025             Llanelli Town AFC
    22026              Cwmbran Town AFC
    22027             Mold Alexandra FC
    22028                 Ebbw Vale AFC
    22029             Inter Cardiff AFC
    22030              Maesteg Park AFC
    Name: Team, Length: 22031, dtype: object




```python
# Select more than one variable
data[['Team', 'Country']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Team</th>
      <th>Country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>FK Partizani Tiranë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>1</th>
      <td>KF Tiranë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>2</th>
      <td>KF Skënderbeu Korçë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>3</th>
      <td>KS Flamurtari Vlorë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KF Teuta Durrës</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>5</th>
      <td>KS Kastrioti Krujë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>6</th>
      <td>FK Kukësi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>7</th>
      <td>KF Laçi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>8</th>
      <td>KS Luftëtari Gjirokastër</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>9</th>
      <td>FC Kamza</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>10</th>
      <td>KF Skënderbeu Korçë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>11</th>
      <td>KF Vllaznia Shkodër</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>12</th>
      <td>KS Flamurtari Vlorë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>13</th>
      <td>FK Partizani Tiranë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>14</th>
      <td>KS Luftëtari Gjirokastër</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>15</th>
      <td>FK Kukësi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>16</th>
      <td>FC Kamza</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>17</th>
      <td>KF Teuta Durrës</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>18</th>
      <td>KF Laçi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>19</th>
      <td>KS Lushnja</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>20</th>
      <td>KF Skënderbeu Korçë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>21</th>
      <td>KS Flamurtari Vlorë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>22</th>
      <td>KF Tiranë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>23</th>
      <td>FK Partizani Tiranë</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>24</th>
      <td>KF Vllaznia Shkodër</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>25</th>
      <td>FK Kukësi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>26</th>
      <td>KS Luftëtari Gjirokastër</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>27</th>
      <td>KF Laçi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>28</th>
      <td>KF Teuta Durrës</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>29</th>
      <td>KS Korabi Peshkopi</td>
      <td>Albania</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>22001</th>
      <td>Holywell Town FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22002</th>
      <td>CPD Bae Cemaes</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22003</th>
      <td>Cwmbran Town AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22004</th>
      <td>Afan Lido FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22005</th>
      <td>Briton Ferry Llansawel AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22006</th>
      <td>Llansantffraid FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22007</th>
      <td>Inter Cardiff AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22008</th>
      <td>Llanelli Town AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22009</th>
      <td>Ton Pentre AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22010</th>
      <td>Ebbw Vale AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22011</th>
      <td>CP Dinas Bangor</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22012</th>
      <td>CPD Tref Aberystwyth</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22013</th>
      <td>CPD Rhyl</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22014</th>
      <td>Newtown AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22015</th>
      <td>Fflint Town United FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22016</th>
      <td>Ton Pentre AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22017</th>
      <td>Barry Town United AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22018</th>
      <td>CPD Caersws</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22019</th>
      <td>CPD Porthmadog</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22020</th>
      <td>Holywell Town FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22021</th>
      <td>Afan Lido FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22022</th>
      <td>The New Saints FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22023</th>
      <td>Connah's Quay FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22024</th>
      <td>Bwrdeisstref Conwy FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22025</th>
      <td>Llanelli Town AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22026</th>
      <td>Cwmbran Town AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22027</th>
      <td>Mold Alexandra FC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22028</th>
      <td>Ebbw Vale AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22029</th>
      <td>Inter Cardiff AFC</td>
      <td>Wales</td>
    </tr>
    <tr>
      <th>22030</th>
      <td>Maesteg Park AFC</td>
      <td>Wales</td>
    </tr>
  </tbody>
</table>
<p>22031 rows × 2 columns</p>
</div>



### Selecting a Subset of Data with Names

We can also select data using `pandas`-specific syntax that allows us to select both columns and rows based on names or conditions. Again, the syntax will look very similar to slicing syntax. In this case, however, we will specify that we are slicing our Data Frame using the `.loc` method:


```python
# Selecting the records of teams from Germany
data.loc[data['Country']=='Germany',:]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>8053</th>
      <td>Germany</td>
      <td>1</td>
      <td>BV 09 Borussia Dortmund</td>
      <td>80.841</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8054</th>
      <td>Germany</td>
      <td>2</td>
      <td>FC Bayern München</td>
      <td>75.000</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8055</th>
      <td>Germany</td>
      <td>3</td>
      <td>FC Schalke 04</td>
      <td>60.941</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8056</th>
      <td>Germany</td>
      <td>4</td>
      <td>VfB Stuttgart</td>
      <td>54.551</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8057</th>
      <td>Germany</td>
      <td>5</td>
      <td>SG Eintracht Frankfurt</td>
      <td>49.765</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8058</th>
      <td>Germany</td>
      <td>6</td>
      <td>VfL Borussia Mönchengladbach</td>
      <td>49.668</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8059</th>
      <td>Germany</td>
      <td>7</td>
      <td>Hertha BSC Berlin</td>
      <td>49.259</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8060</th>
      <td>Germany</td>
      <td>8</td>
      <td>TSV Fortuna 95 Düsseldorf</td>
      <td>43.857</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8061</th>
      <td>Germany</td>
      <td>9</td>
      <td>SV Werder Bremen</td>
      <td>41.256</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8062</th>
      <td>Germany</td>
      <td>10</td>
      <td>1. FC Nürnberg</td>
      <td>40.372</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8063</th>
      <td>Germany</td>
      <td>11</td>
      <td>RB Leipzig</td>
      <td>38.380</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8064</th>
      <td>Germany</td>
      <td>12</td>
      <td>Hannoverscher SV 96</td>
      <td>38.365</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8065</th>
      <td>Germany</td>
      <td>13</td>
      <td>FC Augsburg</td>
      <td>28.618</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8066</th>
      <td>Germany</td>
      <td>14</td>
      <td>TSG 1899 Hoffenheim</td>
      <td>28.456</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8067</th>
      <td>Germany</td>
      <td>15</td>
      <td>Bayer 04 Leverkusen</td>
      <td>27.990</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8068</th>
      <td>Germany</td>
      <td>16</td>
      <td>1. FSV Mainz 05</td>
      <td>26.246</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8069</th>
      <td>Germany</td>
      <td>17</td>
      <td>VfL Wolfsburg</td>
      <td>24.481</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8070</th>
      <td>Germany</td>
      <td>18</td>
      <td>SC Freiburg</td>
      <td>23.894</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8071</th>
      <td>Germany</td>
      <td>1</td>
      <td>BV 09 Borussia Dortmund</td>
      <td>79.496</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8072</th>
      <td>Germany</td>
      <td>2</td>
      <td>FC Bayern München</td>
      <td>75.000</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8073</th>
      <td>Germany</td>
      <td>3</td>
      <td>FC Schalke 04</td>
      <td>61.197</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8074</th>
      <td>Germany</td>
      <td>4</td>
      <td>VfB Stuttgart</td>
      <td>56.045</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8075</th>
      <td>Germany</td>
      <td>5</td>
      <td>VfL Borussia Mönchengladbach</td>
      <td>50.986</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8076</th>
      <td>Germany</td>
      <td>6</td>
      <td>Hamburger SV</td>
      <td>50.656</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8077</th>
      <td>Germany</td>
      <td>7</td>
      <td>SG Eintracht Frankfurt</td>
      <td>49.159</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8078</th>
      <td>Germany</td>
      <td>8</td>
      <td>1. FC Köln</td>
      <td>48.776</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8079</th>
      <td>Germany</td>
      <td>9</td>
      <td>Hertha BSC Berlin</td>
      <td>45.319</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8080</th>
      <td>Germany</td>
      <td>10</td>
      <td>Hannoverscher SV 96</td>
      <td>42.706</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8081</th>
      <td>Germany</td>
      <td>11</td>
      <td>RB Leipzig</td>
      <td>39.397</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>8082</th>
      <td>Germany</td>
      <td>12</td>
      <td>SV Werder Bremen</td>
      <td>38.726</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9029</th>
      <td>Germany</td>
      <td>3</td>
      <td>Hamburger SV</td>
      <td>34.933</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9030</th>
      <td>Germany</td>
      <td>4</td>
      <td>Karlsruher SC</td>
      <td>32.000</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9031</th>
      <td>Germany</td>
      <td>5</td>
      <td>1. FC Köln</td>
      <td>31.933</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9032</th>
      <td>Germany</td>
      <td>6</td>
      <td>1. FC Nürnberg</td>
      <td>30.533</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9033</th>
      <td>Germany</td>
      <td>7</td>
      <td>VfB Stuttgart</td>
      <td>30.133</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9034</th>
      <td>Germany</td>
      <td>8</td>
      <td>TSV München 1860</td>
      <td>28.933</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9035</th>
      <td>Germany</td>
      <td>9</td>
      <td>SV Werder Bremen</td>
      <td>27.267</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9036</th>
      <td>Germany</td>
      <td>10</td>
      <td>FC Schalke 04</td>
      <td>26.467</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9037</th>
      <td>Germany</td>
      <td>11</td>
      <td>BV 09 Borussia Dortmund</td>
      <td>24.800</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9038</th>
      <td>Germany</td>
      <td>12</td>
      <td>1. FC Kaiserslautern</td>
      <td>24.200</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9039</th>
      <td>Germany</td>
      <td>13</td>
      <td>Meidericher SV 02 Duisburg</td>
      <td>22.800</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9040</th>
      <td>Germany</td>
      <td>14</td>
      <td>SG Eintracht Frankfurt</td>
      <td>22.300</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9041</th>
      <td>Germany</td>
      <td>15</td>
      <td>Braunschweiger TSV Eintracht</td>
      <td>21.867</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9042</th>
      <td>Germany</td>
      <td>16</td>
      <td>Borussia VfB Neunkirchen</td>
      <td>21.333</td>
      <td>1965</td>
    </tr>
    <tr>
      <th>9043</th>
      <td>Germany</td>
      <td>1</td>
      <td>VfB Stuttgart</td>
      <td>39.000</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9044</th>
      <td>Germany</td>
      <td>2</td>
      <td>Hertha BSC Berlin</td>
      <td>35.460</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9045</th>
      <td>Germany</td>
      <td>3</td>
      <td>Hamburger SV</td>
      <td>34.667</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9046</th>
      <td>Germany</td>
      <td>4</td>
      <td>TSV München 1860</td>
      <td>32.267</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9047</th>
      <td>Germany</td>
      <td>5</td>
      <td>1. FC Köln</td>
      <td>31.900</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9048</th>
      <td>Germany</td>
      <td>6</td>
      <td>Karlsruher SC</td>
      <td>31.667</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9049</th>
      <td>Germany</td>
      <td>7</td>
      <td>1. FC Nürnberg</td>
      <td>28.600</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9050</th>
      <td>Germany</td>
      <td>8</td>
      <td>Meidericher SV 02 Duisburg</td>
      <td>28.400</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9051</th>
      <td>Germany</td>
      <td>9</td>
      <td>SG Eintracht Frankfurt</td>
      <td>26.400</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9052</th>
      <td>Germany</td>
      <td>10</td>
      <td>FC Schalke 04</td>
      <td>23.867</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9053</th>
      <td>Germany</td>
      <td>11</td>
      <td>BV 09 Borussia Dortmund</td>
      <td>23.133</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9054</th>
      <td>Germany</td>
      <td>12</td>
      <td>SC Preußen Münster</td>
      <td>22.267</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9055</th>
      <td>Germany</td>
      <td>13</td>
      <td>1. FC Kaiserslautern</td>
      <td>22.133</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9056</th>
      <td>Germany</td>
      <td>14</td>
      <td>Braunschweiger TSV Eintracht</td>
      <td>21.467</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9057</th>
      <td>Germany</td>
      <td>15</td>
      <td>SV Werder Bremen</td>
      <td>20.733</td>
      <td>1964</td>
    </tr>
    <tr>
      <th>9058</th>
      <td>Germany</td>
      <td>16</td>
      <td>1. FC Saarbrücken</td>
      <td>18.067</td>
      <td>1964</td>
    </tr>
  </tbody>
</table>
<p>1006 rows × 5 columns</p>
</div>



We can use logical statements to determine the rows or columns that we wish to extract. Within the square brackets (`[` and `]`), we first declare the rows we want to select. We place a comma (`,`) and then declare the columns that we want to select. In the example above, we used the logical statement `data['Country']=='Germany'` to pick our rows. This statement requires that any row have a `Country` value equal to "Germany" in order to be included in the subset of the data.

For the columns, we used the colon (`:`) to indicate that we would like all columns for the specified rows. We could instead provide a column name, a list of column names, or even a logical condition through which we would like to select columns.

The `.loc` method can easily be adapted to select columns as we did with the slicing syntax:


```python
data.loc[:,'Country']
```




    0        Albania
    1        Albania
    2        Albania
    3        Albania
    4        Albania
    5        Albania
    6        Albania
    7        Albania
    8        Albania
    9        Albania
    10       Albania
    11       Albania
    12       Albania
    13       Albania
    14       Albania
    15       Albania
    16       Albania
    17       Albania
    18       Albania
    19       Albania
    20       Albania
    21       Albania
    22       Albania
    23       Albania
    24       Albania
    25       Albania
    26       Albania
    27       Albania
    28       Albania
    29       Albania
              ...   
    22001      Wales
    22002      Wales
    22003      Wales
    22004      Wales
    22005      Wales
    22006      Wales
    22007      Wales
    22008      Wales
    22009      Wales
    22010      Wales
    22011      Wales
    22012      Wales
    22013      Wales
    22014      Wales
    22015      Wales
    22016      Wales
    22017      Wales
    22018      Wales
    22019      Wales
    22020      Wales
    22021      Wales
    22022      Wales
    22023      Wales
    22024      Wales
    22025      Wales
    22026      Wales
    22027      Wales
    22028      Wales
    22029      Wales
    22030      Wales
    Name: Country, Length: 22031, dtype: object



If we want, we can add multiple logical statements to our `.loc` statement to find very specific subsets. We can, for example, use our current data to find the top team (in terms of attendance) in the EPL for each year in our data:


```python
data.loc[(data['Country']=='England') & (data['Position']==1), :]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4189</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>74.498</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>4209</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.290</td>
      <td>2017</td>
    </tr>
    <tr>
      <th>4229</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.286</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>4249</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.335</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>4269</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.207</td>
      <td>2014</td>
    </tr>
    <tr>
      <th>4289</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.530</td>
      <td>2013</td>
    </tr>
    <tr>
      <th>4309</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.387</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>4329</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.109</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>4349</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>74.864</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>4369</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.304</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>4389</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.691</td>
      <td>2008</td>
    </tr>
    <tr>
      <th>4409</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>75.826</td>
      <td>2007</td>
    </tr>
    <tr>
      <th>4429</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>68.765</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>4451</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>67.748</td>
      <td>2005</td>
    </tr>
    <tr>
      <th>4471</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>67.641</td>
      <td>2004</td>
    </tr>
    <tr>
      <th>4491</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>67.602</td>
      <td>2003</td>
    </tr>
    <tr>
      <th>4511</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>67.558</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>4531</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>67.490</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>4551</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>58.014</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>4571</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>55.188</td>
      <td>1999</td>
    </tr>
    <tr>
      <th>4591</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>55.164</td>
      <td>1998</td>
    </tr>
    <tr>
      <th>4611</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>55.081</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>4631</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>41.683</td>
      <td>1996</td>
    </tr>
    <tr>
      <th>4651</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>43.683</td>
      <td>1995</td>
    </tr>
    <tr>
      <th>4673</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>44.244</td>
      <td>1994</td>
    </tr>
    <tr>
      <th>4695</th>
      <td>England</td>
      <td>1</td>
      <td>Liverpool FC</td>
      <td>37.009</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>4717</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>45.389</td>
      <td>1992</td>
    </tr>
    <tr>
      <th>4739</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>43.242</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>4759</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester United</td>
      <td>39.331</td>
      <td>1990</td>
    </tr>
    <tr>
      <th>4779</th>
      <td>England</td>
      <td>1</td>
      <td>Liverpool FC</td>
      <td>38.706</td>
      <td>1989</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>6096</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>37.545</td>
      <td>1922</td>
    </tr>
    <tr>
      <th>6118</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>41.265</td>
      <td>1921</td>
    </tr>
    <tr>
      <th>6140</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>42.615</td>
      <td>1920</td>
    </tr>
    <tr>
      <th>6162</th>
      <td>England</td>
      <td>1</td>
      <td>Manchester City FC</td>
      <td>20.205</td>
      <td>1915</td>
    </tr>
    <tr>
      <th>6184</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>37.105</td>
      <td>1914</td>
    </tr>
    <tr>
      <th>6204</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>33.555</td>
      <td>1913</td>
    </tr>
    <tr>
      <th>6224</th>
      <td>England</td>
      <td>1</td>
      <td>Tottenham Hotspur FC</td>
      <td>25.030</td>
      <td>1912</td>
    </tr>
    <tr>
      <th>6244</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>25.055</td>
      <td>1911</td>
    </tr>
    <tr>
      <th>6264</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>28.545</td>
      <td>1910</td>
    </tr>
    <tr>
      <th>6284</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>29.300</td>
      <td>1909</td>
    </tr>
    <tr>
      <th>6304</th>
      <td>England</td>
      <td>1</td>
      <td>Chelsea FC</td>
      <td>31.965</td>
      <td>1908</td>
    </tr>
    <tr>
      <th>6324</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>33.235</td>
      <td>1907</td>
    </tr>
    <tr>
      <th>6344</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>22.765</td>
      <td>1906</td>
    </tr>
    <tr>
      <th>6364</th>
      <td>England</td>
      <td>1</td>
      <td>Newcastle United FC</td>
      <td>21.605</td>
      <td>1905</td>
    </tr>
    <tr>
      <th>6382</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>20.035</td>
      <td>1904</td>
    </tr>
    <tr>
      <th>6400</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>19.790</td>
      <td>1903</td>
    </tr>
    <tr>
      <th>6418</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>19.580</td>
      <td>1902</td>
    </tr>
    <tr>
      <th>6436</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>17.530</td>
      <td>1901</td>
    </tr>
    <tr>
      <th>6454</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>18.765</td>
      <td>1900</td>
    </tr>
    <tr>
      <th>6472</th>
      <td>England</td>
      <td>1</td>
      <td>Aston Villa FC</td>
      <td>23.045</td>
      <td>1899</td>
    </tr>
    <tr>
      <th>6490</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>17.390</td>
      <td>1898</td>
    </tr>
    <tr>
      <th>6506</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>15.840</td>
      <td>1897</td>
    </tr>
    <tr>
      <th>6522</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>16.080</td>
      <td>1896</td>
    </tr>
    <tr>
      <th>6538</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>17.420</td>
      <td>1895</td>
    </tr>
    <tr>
      <th>6554</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>13.520</td>
      <td>1894</td>
    </tr>
    <tr>
      <th>6570</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>13.230</td>
      <td>1893</td>
    </tr>
    <tr>
      <th>6586</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>10.730</td>
      <td>1892</td>
    </tr>
    <tr>
      <th>6600</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>11.375</td>
      <td>1891</td>
    </tr>
    <tr>
      <th>6612</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>10.110</td>
      <td>1890</td>
    </tr>
    <tr>
      <th>6624</th>
      <td>England</td>
      <td>1</td>
      <td>Everton FC</td>
      <td>7.260</td>
      <td>1889</td>
    </tr>
  </tbody>
</table>
<p>119 rows × 5 columns</p>
</div>



### Selecting a Subset of Data with Numbers

While less common, we may on occasion want to reference our data by numeric position, rather than by logical conditions or text-based names. In these situations, we have the `.iloc` method to help us. In structure, it is very similar to the `.loc` method, but it is entirely integer based in its selections. This makes it the truest `pandas` analog of list and array slicing.


```python
data.iloc[:10,:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Albania</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Albania</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albania</td>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Albania</td>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Albania</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Albania</td>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Albania</td>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Albania</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>



In the example above, I extract the first 10 rows of the data, along with the first two columns of the data. The syntax for doing each of those things is identical to list slicing. We can even use the same expanded syntax for pandas to skip every other row or find other integer-based subsets of our data:


```python
# Select every other row through the first 20 rows of the data
#   and the first two columns
data.iloc[:20:2,:2]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Albania</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albania</td>
      <td>5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Albania</td>
      <td>7</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Albania</td>
      <td>9</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Albania</td>
      <td>1</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Albania</td>
      <td>3</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Albania</td>
      <td>5</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Albania</td>
      <td>7</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Albania</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



### Sampling a Data Frame

Another excellent method built into Data Frames is the ability to quickly and easily sample our data. If we have a very large dataset, and want to work with a smaller subset without losing generality, a random subsample is a great option. The `.sample()` method does just that:


```python
# Sample 10 random rows from our data
data.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>13469</th>
      <td>Luxembourg</td>
      <td>9</td>
      <td>FC Victoria Rosport</td>
      <td>0.318</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>14649</th>
      <td>Netherland</td>
      <td>1</td>
      <td>PSV</td>
      <td>21.453</td>
      <td>1988</td>
    </tr>
    <tr>
      <th>18325</th>
      <td>Scotland</td>
      <td>10</td>
      <td>Falkirk FC</td>
      <td>5.516</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>5881</th>
      <td>England</td>
      <td>6</td>
      <td>West Bromwich Albion FC</td>
      <td>24.459</td>
      <td>1932</td>
    </tr>
    <tr>
      <th>9739</th>
      <td>Greece</td>
      <td>9</td>
      <td>GS Apollon Smyrni Athina</td>
      <td>5.750</td>
      <td>1979</td>
    </tr>
    <tr>
      <th>17029</th>
      <td>Portugal</td>
      <td>1</td>
      <td>FC Porto</td>
      <td>36.038</td>
      <td>2005</td>
    </tr>
    <tr>
      <th>1441</th>
      <td>Belgium</td>
      <td>4</td>
      <td>KRC Genk</td>
      <td>21.968</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>18595</th>
      <td>Serbia</td>
      <td>2</td>
      <td>FK Partizan Beograd</td>
      <td>5.200</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>7577</th>
      <td>France</td>
      <td>17</td>
      <td>FC Lorient</td>
      <td>11.988</td>
      <td>2016</td>
    </tr>
    <tr>
      <th>16142</th>
      <td>Poland</td>
      <td>8</td>
      <td>KS Polonia Bytom</td>
      <td>5.047</td>
      <td>2010</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sample .1% of our data
data.sample(frac=0.001)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>18707</th>
      <td>Serbia</td>
      <td>12</td>
      <td>FK Mogren Budva</td>
      <td>1.183</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>2527</th>
      <td>Bulgaria</td>
      <td>9</td>
      <td>PFK Rodopa Smolyan</td>
      <td>2.966</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>13251</th>
      <td>Lithuania</td>
      <td>4</td>
      <td>FK Šiauliai</td>
      <td>0.964</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>20831</th>
      <td>Switzerland</td>
      <td>10</td>
      <td>FC Zürich</td>
      <td>3.731</td>
      <td>1996</td>
    </tr>
    <tr>
      <th>22007</th>
      <td>Wales</td>
      <td>18</td>
      <td>Inter Cardiff AFC</td>
      <td>0.147</td>
      <td>1996</td>
    </tr>
    <tr>
      <th>21540</th>
      <td>Ukraine</td>
      <td>13</td>
      <td>FK Goverla Uzhgorod</td>
      <td>5.624</td>
      <td>2008</td>
    </tr>
    <tr>
      <th>10965</th>
      <td>Iceland</td>
      <td>1</td>
      <td>KR Reykjavík</td>
      <td>2.148</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>15332</th>
      <td>North Ireland</td>
      <td>8</td>
      <td>Cliftonville Belfast F&amp;AC</td>
      <td>0.817</td>
      <td>2010</td>
    </tr>
    <tr>
      <th>1043</th>
      <td>Belarus</td>
      <td>3</td>
      <td>FK Dinamo 1927 Minsk</td>
      <td>2.509</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>21647</th>
      <td>Ukraine</td>
      <td>10</td>
      <td>FK Vorskla Poltava</td>
      <td>6.846</td>
      <td>2001</td>
    </tr>
    <tr>
      <th>1716</th>
      <td>Belgium</td>
      <td>9</td>
      <td>RFC Liège</td>
      <td>6.529</td>
      <td>1991</td>
    </tr>
    <tr>
      <th>14492</th>
      <td>Netherland</td>
      <td>6</td>
      <td>NAC Breda</td>
      <td>12.383</td>
      <td>1997</td>
    </tr>
    <tr>
      <th>12788</th>
      <td>Kazakhstan</td>
      <td>6</td>
      <td>FK Irtysh Pavlodar</td>
      <td>4.037</td>
      <td>2007</td>
    </tr>
    <tr>
      <th>897</th>
      <td>Azerbaijan</td>
      <td>12</td>
      <td>MOİK Bakı</td>
      <td>0.396</td>
      <td>2011</td>
    </tr>
    <tr>
      <th>84</th>
      <td>Albania</td>
      <td>9</td>
      <td>KF Tiranë</td>
      <td>1.269</td>
      <td>2012</td>
    </tr>
    <tr>
      <th>12024</th>
      <td>Italy</td>
      <td>6</td>
      <td>ACF Fiorentina</td>
      <td>35.037</td>
      <td>1999</td>
    </tr>
    <tr>
      <th>6675</th>
      <td>Estonia</td>
      <td>10</td>
      <td>Paide Linnameeskond</td>
      <td>0.181</td>
      <td>2015</td>
    </tr>
    <tr>
      <th>5667</th>
      <td>England</td>
      <td>12</td>
      <td>Birmingham City FC</td>
      <td>38.453</td>
      <td>1949</td>
    </tr>
    <tr>
      <th>7320</th>
      <td>Finland</td>
      <td>2</td>
      <td>HJK Helsinki</td>
      <td>3.243</td>
      <td>1983</td>
    </tr>
    <tr>
      <th>10712</th>
      <td>Hungary</td>
      <td>14</td>
      <td>FC Tatabánya Bányász</td>
      <td>4.765</td>
      <td>1979</td>
    </tr>
    <tr>
      <th>17095</th>
      <td>Portugal</td>
      <td>13</td>
      <td>FC Paços de Ferreira</td>
      <td>3.529</td>
      <td>2002</td>
    </tr>
    <tr>
      <th>2226</th>
      <td>Bosnia</td>
      <td>14</td>
      <td>FK Drina Zvornik</td>
      <td>0.673</td>
      <td>2011</td>
    </tr>
  </tbody>
</table>
</div>



While the defaut is to sample **without** replacement, we can also sample with replacement. This is particularly valuable if we attempt to perform any bootstrap-based statistical procedures.


```python
# Sample 10 rows with replacement
data.sample(n=10, replace=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2115</th>
      <td>Bosnia</td>
      <td>7</td>
      <td>FK Sloboda Tuzla</td>
      <td>1.450</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>14446</th>
      <td>Netherland</td>
      <td>14</td>
      <td>Sparta Rotterdam</td>
      <td>7.071</td>
      <td>2000</td>
    </tr>
    <tr>
      <th>5217</th>
      <td>England</td>
      <td>2</td>
      <td>Liverpool FC</td>
      <td>47.348</td>
      <td>1969</td>
    </tr>
    <tr>
      <th>5696</th>
      <td>England</td>
      <td>19</td>
      <td>Derby County FC</td>
      <td>27.044</td>
      <td>1948</td>
    </tr>
    <tr>
      <th>10823</th>
      <td>Hungary</td>
      <td>7</td>
      <td>Vasas SC</td>
      <td>6.100</td>
      <td>1972</td>
    </tr>
    <tr>
      <th>15517</th>
      <td>Norway</td>
      <td>9</td>
      <td>FC Lyn Oslo</td>
      <td>6.643</td>
      <td>2008</td>
    </tr>
    <tr>
      <th>8003</th>
      <td>Georgia</td>
      <td>1</td>
      <td>FC Zestafoni</td>
      <td>4.360</td>
      <td>2006</td>
    </tr>
    <tr>
      <th>12248</th>
      <td>Italy</td>
      <td>16</td>
      <td>Ascoli Picchio FC</td>
      <td>14.421</td>
      <td>1987</td>
    </tr>
    <tr>
      <th>3407</th>
      <td>Czech R.</td>
      <td>3</td>
      <td>FC Baník Ostrava</td>
      <td>7.822</td>
      <td>2009</td>
    </tr>
    <tr>
      <th>6603</th>
      <td>England</td>
      <td>4</td>
      <td>Notts County FC</td>
      <td>7.580</td>
      <td>1891</td>
    </tr>
  </tbody>
</table>
</div>



## Cleaning Data

Once we have the data that we want, we are ready to clean our data and prepare it for analysis. This is the reason that `pandas` is so powerful. Not only can we import data from pretty much any source and select a subset of the data that is relevant for our work, we can also process the data to make it more helpful. We will explore some of the ways that we can clean data below.

### Changing the Index

You might have noticed already, but when we imported our data, `pandas` created an *index* that uniquely identifies each row in our data. This is common practice, and the index is used in various contexts. For example, some libraries (like the Facebook `Prophet` library for time series analysis) will check the index as part of the data validation process.

If we want to change the index of our data, we can do so by telling our Data Frame which column in our data should be treated as the index. One example might be if we had our SQL data from earlier. In that data set, each individual who was surveyed was assigned a unique identifier. We may want to change our Data Frame so that the `id` column becomes the index:


```python
# Example SQL query from above
conn = sqlite3.connect("exampleDatabase.db")
select = "SELECT * FROM acs LIMIT 100"
data = pd.read_sql(select, conn)

# Set the 'id' column as the index
data.index = data['id']

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>year</th>
      <th>cpi99</th>
      <th>region</th>
      <th>statefip</th>
      <th>countyfips</th>
      <th>metro</th>
      <th>city</th>
      <th>citypop</th>
      <th>farm</th>
      <th>...</th>
      <th>labforce</th>
      <th>occ2010</th>
      <th>ind1990</th>
      <th>inctot</th>
      <th>ftotinc</th>
      <th>incwage</th>
      <th>incbus00</th>
      <th>incss</th>
      <th>incwelfr</th>
      <th>incinvst</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16873974</th>
      <td>16873974</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>6515</td>
      <td>60</td>
      <td>50000</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873975</th>
      <td>16873975</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873976</th>
      <td>16873976</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873977</th>
      <td>16873977</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873978</th>
      <td>16873978</td>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 61 columns</p>
</div>



We can see above that the index is now identical to the `id` column. We can, at this point, remove the id column from our Data Frame if we so choose:


```python
data = data.drop('id', axis=1)

data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>year</th>
      <th>cpi99</th>
      <th>region</th>
      <th>statefip</th>
      <th>countyfips</th>
      <th>metro</th>
      <th>city</th>
      <th>citypop</th>
      <th>farm</th>
      <th>ownershp</th>
      <th>...</th>
      <th>labforce</th>
      <th>occ2010</th>
      <th>ind1990</th>
      <th>inctot</th>
      <th>ftotinc</th>
      <th>incwage</th>
      <th>incbus00</th>
      <th>incss</th>
      <th>incwelfr</th>
      <th>incinvst</th>
    </tr>
    <tr>
      <th>id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16873974</th>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>2</td>
      <td>6515</td>
      <td>60</td>
      <td>50000</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873975</th>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>1</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873976</th>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873977</th>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16873978</th>
      <td>2012</td>
      <td>0.726</td>
      <td>22</td>
      <td>31</td>
      <td>55</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>2</td>
      <td>...</td>
      <td>0</td>
      <td>9920</td>
      <td>0</td>
      <td>0</td>
      <td>50000</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 60 columns</p>
</div>



Note that we must manipulate **and** store our updated Data Frame if we would like to keep the updated version. This protects us against unintended overwriting of important data, and provides a way for us to test commands without altering our root data. To store the data in its updated form, we can simply assign the new Data Frame to the same variable name as was used by the previous version of the data.

### Processing Datetimes

When importing data from databases or spreadsheets, dates and times are typically treated as strings, since they are a mix of characters (like the month, or separators such as `/`,`-`, or `:`) and numbers (the days, years, hours, minutes, etc.). Fortunately, `pandas` provides powerful functionality to transform these values (we will call them **datetimes** from now on) from strings into meaningful data. Doing so is exceptionally simple:


```python
# Import data with datetime column (conveniently named 'datetime')
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/pollutionBeijing.csv")

# Transform the column from a string to a pandas datetime
data['datetime'] = pd.to_datetime(data['datetime'])

data['datetime'].head()
```




    0   2010-01-01 00:00:00
    1   2010-01-01 01:00:00
    2   2010-01-01 02:00:00
    3   2010-01-01 03:00:00
    4   2010-01-01 04:00:00
    Name: datetime, dtype: datetime64[ns]



You can see above that our column now has the `dtype` (meaning **data type**) of datetime64. Our column is now ready to use. Sometimes, though, our data is not formatted nicely, and `pandas` will not know how to parse the data on its own. In that case, we can use the following syntax to explicitly define where each relevant piece of date or time information is in our string:


```python
# Import data with datetime column (conveniently named 'datetime')
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/pollutionBeijing.csv")

# Transform the column from a string to a pandas datetime
#   using EXPLICIT declaration
data['datetime'] = pd.to_datetime(data['datetime'], format = "%Y-%m-%d %H:%M:%S")
```

In this case, we use [date and time syntax](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) to indicate the location of the year, month, day, hour, minute, and second of our record, and we include the location of separators such as `-`, `:`, and whitespace (` `).

### Datetime Tools

Once we have our datetimes arranged, we can do all sorts of cool transformations. The `pandas` datetime tools provide immediate access to a large array of date-related information that we can explore with just a few lines of code. We can see all of the available converstions by using the code `dir(data['datetime'].dt)` to view all methods (and attributes!) associated with datetime columns. Some of the most helpful methods are
- `.day()`
- `.day_name()`
- `.month()`
- `.month_name()`
- `.hour()`
- `.minute()`
- `.second()`
- `.year()`


```python
# Sample 10 observations, and find the month in which the observations occurred
data['datetime'].sample(10).dt.month_name()
```




    28203       March
    17227    December
    37278       April
    34804    December
    31640      August
    43520    December
    4523         July
    4549         July
    34099    November
    31190        July
    Name: datetime, dtype: object



### Creating New Columns

As we transform data, it is often profitable to migrate data from a single column to one or more new columns that have been processed and prepared for analysis. Creating new columns is straightforward, and can be done using code that closely resembles the slicing syntax for column selection:


```python
# Create a column from datetime that contains the day of the week
data['day'] = data['datetime'].dt.day_name()

# Sample the new column to show values
data['day'].sample(10)
```




    4599        Sunday
    5566        Friday
    2834      Thursday
    37663     Saturday
    8890      Thursday
    24143      Tuesday
    3165     Wednesday
    27716     Thursday
    19695     Saturday
    6806        Monday
    Name: day, dtype: object



We can also create many columns at once from a single column using the `get_dummies()` method:


```python
# Create dummy columns
new_cols = pd.get_dummies(data['day'])

new_cols.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Friday</th>
      <th>Monday</th>
      <th>Saturday</th>
      <th>Sunday</th>
      <th>Thursday</th>
      <th>Tuesday</th>
      <th>Wednesday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>727</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16223</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16575</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17380</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>30483</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9410</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16133</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>8991</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16714</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>38737</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



Now that we have dummy variables, we can use the `concat()` method to attach these columns to our original data:


```python
# Concatenate our two data sets
data = pd.concat([data, new_cols], axis=1)

data.sample(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>pm2.5</th>
      <th>DEWP</th>
      <th>TEMP</th>
      <th>PRES</th>
      <th>cbwd</th>
      <th>Iws</th>
      <th>Is</th>
      <th>Ir</th>
      <th>datetime</th>
      <th>day</th>
      <th>Friday</th>
      <th>Monday</th>
      <th>Saturday</th>
      <th>Sunday</th>
      <th>Thursday</th>
      <th>Tuesday</th>
      <th>Wednesday</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20143</th>
      <td>85.0</td>
      <td>10</td>
      <td>13.0</td>
      <td>1012.0</td>
      <td>SE</td>
      <td>4.02</td>
      <td>0</td>
      <td>0</td>
      <td>2012-04-19 07:00:00</td>
      <td>Thursday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>22649</th>
      <td>7.0</td>
      <td>20</td>
      <td>23.0</td>
      <td>1006.0</td>
      <td>NE</td>
      <td>4.92</td>
      <td>0</td>
      <td>13</td>
      <td>2012-08-01 17:00:00</td>
      <td>Wednesday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>35410</th>
      <td>66.0</td>
      <td>-17</td>
      <td>-2.0</td>
      <td>1033.0</td>
      <td>NW</td>
      <td>12.07</td>
      <td>0</td>
      <td>0</td>
      <td>2014-01-15 10:00:00</td>
      <td>Wednesday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1922</th>
      <td>90.0</td>
      <td>-3</td>
      <td>6.0</td>
      <td>1011.0</td>
      <td>NE</td>
      <td>0.89</td>
      <td>0</td>
      <td>0</td>
      <td>2010-03-22 02:00:00</td>
      <td>Monday</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1557</th>
      <td>76.0</td>
      <td>-9</td>
      <td>-3.0</td>
      <td>1034.0</td>
      <td>SE</td>
      <td>12.07</td>
      <td>0</td>
      <td>0</td>
      <td>2010-03-06 21:00:00</td>
      <td>Saturday</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16612</th>
      <td>118.0</td>
      <td>-10</td>
      <td>-6.0</td>
      <td>1029.0</td>
      <td>NW</td>
      <td>0.89</td>
      <td>0</td>
      <td>0</td>
      <td>2011-11-24 04:00:00</td>
      <td>Thursday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15078</th>
      <td>57.0</td>
      <td>6</td>
      <td>10.0</td>
      <td>1016.0</td>
      <td>NW</td>
      <td>11.63</td>
      <td>0</td>
      <td>0</td>
      <td>2011-09-21 06:00:00</td>
      <td>Wednesday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2314</th>
      <td>114.0</td>
      <td>-5</td>
      <td>12.0</td>
      <td>1024.0</td>
      <td>cv</td>
      <td>1.79</td>
      <td>0</td>
      <td>0</td>
      <td>2010-04-07 10:00:00</td>
      <td>Wednesday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16179</th>
      <td>69.0</td>
      <td>7</td>
      <td>8.0</td>
      <td>1027.0</td>
      <td>SE</td>
      <td>0.89</td>
      <td>0</td>
      <td>0</td>
      <td>2011-11-06 03:00:00</td>
      <td>Sunday</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>43087</th>
      <td>13.0</td>
      <td>-22</td>
      <td>-5.0</td>
      <td>1032.0</td>
      <td>NW</td>
      <td>255.26</td>
      <td>0</td>
      <td>0</td>
      <td>2014-12-01 07:00:00</td>
      <td>Monday</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Mapping Functions

In order to perform functions across an entire column, we can take advantage of the built in `map` method for `pandas` Series objects (a Series is the `pandas` term for a single column extracted from a Data Frame). Say that we want to multiply attendance figures from our football data by 1000 so that attendance is not measured in thousands but in individual attendees. We can use the `map` method to do so:


```python
# Import data
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/footballAttendance.csv")

# Use a lambda function to multiply each record's attendance number by 1000
data['Average Attendance'] = data['Average Attendance'].map(lambda x: x*1000)

# Show the first rows of the updated data
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Albania</td>
      <td>1</td>
      <td>FK Partizani Tiranë</td>
      <td>2986.0</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Albania</td>
      <td>2</td>
      <td>KF Tiranë</td>
      <td>2308.0</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Albania</td>
      <td>3</td>
      <td>KF Skënderbeu Korçë</td>
      <td>1833.0</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Albania</td>
      <td>4</td>
      <td>KS Flamurtari Vlorë</td>
      <td>1624.0</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Albania</td>
      <td>5</td>
      <td>KF Teuta Durrës</td>
      <td>889.0</td>
      <td>2019</td>
    </tr>
  </tbody>
</table>
</div>



We can also use the `apply` method to aggregate within a Data Frame by row or column:


```python
# Calculates the difference between the min and max of the attendance and year columns
data[['Average Attendance', 'Year']].apply(lambda x: x.max() - x.min())
```




    Average Attendance    949962.0
    Year                     130.0
    dtype: float64



### Missing Values

Pandas provides tools for us to fill in missing values when appropriate. We can choose from several different methods of filling in our missing values, but we will always do so by using the `.fillna()` method.

**Forward Fill (Pad)** - Use the most recent (previous) valid entry in the column to fill in the missing value

`data.fillna(method='ffill')`

**Backfill** - Use the next valid entry (looking forward) in the column to fill in the missing value

`data.fillna(method='bfill')`

While it is not always ideal to fill in missing observations (sometimes it is best to just drop observations with missing data), there are times when it is handy, and `pandas` makes it very easy for us!

### Using PandaSQL

Some data manipulations are still difficult to implement in `pandas`, despite the abundant tools provided through the library. In these cases, it is often simpler to transform the data using SQL queries. While the ability to use SQL queries is not directly built into `pandas`, it is still possible to use an outside library to transform data *within* `pandas` through the `pandasql` library:


```python
# Install the pandasql library if needed
# !pip install pandasql

# Import the library and prepare it for use with data
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

# Import data
data = pd.read_csv("https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/footballAttendance.csv")

# Transform data using the imported pysqldf function

select = "SELECT * FROM data WHERE Country = 'Wales' LIMIT 10"
pysqldf(select)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>Position</th>
      <th>Team</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Wales</td>
      <td>1</td>
      <td>CPD Tref Caernarfon</td>
      <td>0.872</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Wales</td>
      <td>2</td>
      <td>Barry Town United AFC</td>
      <td>0.477</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wales</td>
      <td>3</td>
      <td>The New Saints FC</td>
      <td>0.326</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Wales</td>
      <td>4</td>
      <td>CPD Tref Aberystwyth</td>
      <td>0.302</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Wales</td>
      <td>5</td>
      <td>Llanelli Town AFC</td>
      <td>0.290</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wales</td>
      <td>6</td>
      <td>CPD Tref Caerfyrddin</td>
      <td>0.287</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Wales</td>
      <td>7</td>
      <td>Cefn Druids AFC</td>
      <td>0.285</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Wales</td>
      <td>8</td>
      <td>Connah's Quay FC</td>
      <td>0.280</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Wales</td>
      <td>9</td>
      <td>Newtown AFC</td>
      <td>0.274</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Wales</td>
      <td>10</td>
      <td>CPY Bala Town</td>
      <td>0.270</td>
      <td>2019</td>
    </tr>
  </tbody>
</table>
</div>



In the cases where transformations are simpler in SQL, `pandasql` provides a powerful tool to extend our Data Frames and make them even easier to use.

## Summary Statistics

To help us understand how to use our data frames in a scientific context, it is useful to see that we can create a summary statistics table to emulate all of your favorite research papers using just one line of code and a `pandas` Data Frame. This will combine what we know about Data Frames with a few new functions:


```python
data.describe().T[['mean','std','min','max','count']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Position</th>
      <td>8.407290</td>
      <td>4.973896</td>
      <td>1.000</td>
      <td>25.0</td>
      <td>22031.0</td>
    </tr>
    <tr>
      <th>Average Attendance</th>
      <td>10.947123</td>
      <td>14.098543</td>
      <td>0.038</td>
      <td>950.0</td>
      <td>22031.0</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>1995.052608</td>
      <td>22.798657</td>
      <td>1889.000</td>
      <td>2019.0</td>
      <td>22031.0</td>
    </tr>
  </tbody>
</table>
</div>



What just happened? We used the built in `describe()` method, and then we made some transformations. Let's walk through it. Here is what we get if we just use the `describe()` method on our Data Frame:


```python
data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Position</th>
      <th>Average Attendance</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>22031.000000</td>
      <td>22031.000000</td>
      <td>22031.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>8.407290</td>
      <td>10.947123</td>
      <td>1995.052608</td>
    </tr>
    <tr>
      <th>std</th>
      <td>4.973896</td>
      <td>14.098543</td>
      <td>22.798657</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.038000</td>
      <td>1889.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
      <td>2.362500</td>
      <td>1986.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>8.000000</td>
      <td>5.964000</td>
      <td>2001.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>12.000000</td>
      <td>15.160000</td>
      <td>2011.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>950.000000</td>
      <td>2019.000000</td>
    </tr>
  </tbody>
</table>
</div>



Helpful, but noisy, and not properly formatted based on academic research expectations (typically we would expect our variables to be represented by rows, and the summary statistics to be columns). In order to make that happen, we can use the `.T` attribute of our Data Frame. This attribute represents the **transposed** version of our Data Frame, in which rows are switched for columns, and vice versa.


```python
data.describe().T
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>25%</th>
      <th>50%</th>
      <th>75%</th>
      <th>max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Position</th>
      <td>22031.0</td>
      <td>8.407290</td>
      <td>4.973896</td>
      <td>1.000</td>
      <td>4.0000</td>
      <td>8.000</td>
      <td>12.00</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>Average Attendance</th>
      <td>22031.0</td>
      <td>10.947123</td>
      <td>14.098543</td>
      <td>0.038</td>
      <td>2.3625</td>
      <td>5.964</td>
      <td>15.16</td>
      <td>950.0</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>22031.0</td>
      <td>1995.052608</td>
      <td>22.798657</td>
      <td>1889.000</td>
      <td>1986.0000</td>
      <td>2001.000</td>
      <td>2011.00</td>
      <td>2019.0</td>
    </tr>
  </tbody>
</table>
</div>



Now we are getting closer. At this point, we just want to choose the columns that we want, in the order that we want. We do that with slicing syntax to make our code easier to write.


```python
data.describe().T[['mean','std','min','max','count']]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>mean</th>
      <th>std</th>
      <th>min</th>
      <th>max</th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Position</th>
      <td>8.407290</td>
      <td>4.973896</td>
      <td>1.000</td>
      <td>25.0</td>
      <td>22031.0</td>
    </tr>
    <tr>
      <th>Average Attendance</th>
      <td>10.947123</td>
      <td>14.098543</td>
      <td>0.038</td>
      <td>950.0</td>
      <td>22031.0</td>
    </tr>
    <tr>
      <th>Year</th>
      <td>1995.052608</td>
      <td>22.798657</td>
      <td>1889.000</td>
      <td>2019.0</td>
      <td>22031.0</td>
    </tr>
  </tbody>
</table>
</div>



Done! It is worth mentioning at this point that we can also use many summary statistic methods on individual columns. We have access to `.min()`, `.max()`, `.mean()`, `.std()`, and more for numeric columns, as well as `.value_count()` and `.unique()` for all columns (though they become especially useful for categorical or text data).


```python
data['Average Attendance'].mean()
```




    10.947123099269211




```python
data['Country'].value_counts()
```




    England          2447
    Netherland       1126
    Greece           1014
    Italy            1014
    Germany          1006
    Belgium           873
    Hungary           808
    Poland            802
    Sweden            676
    Norway            642
    Finland           617
    Portugal          614
    Switzerland       610
    Austria           566
    Spain             544
    Denmark           528
    Russia            442
    Ukraine           438
    Czech R.          416
    France            394
    Kazakhstan        386
    Iceland           362
    Croatia           358
    Slovenia          325
    Serbia            319
    Slovakia          316
    Romania           311
    Bulgaria          296
    Belarus           269
    Cyprus            262
    Lithuania         262
    Luxembourg        254
    Scotland          238
    Bosnia            232
    Wales             225
    Ireland           204
    Israel            182
    Turkey            180
    Georgia           158
    Latvia            156
    Estonia           148
    Azerbaijan        147
    Albania           140
    Montenegro        140
    North Ireland     132
    Moldova           128
    Macedonia         122
    Armenia           102
    Faroe Islands     100
    Name: Country, dtype: int64



**Solve it**:

Your assignment for this session is to import and clean a data source. The data you will be working with relates to data for predicting whether or not a room is occupied using light and atmospheric measurements. The data can be found [here](https://github.com/dustywhite7/pythonMikkeli/raw/master/exampleData/roomOccupancy.csv).

To complete the assignment, you will do the following:

1. Import the data into a Data Frame called `occupancy`. (1 point)
2. Transform the timestamps in the data into columns called `day_of_week`, `hour`, and `minute`, containing the text name of the day of week, the number value of the hour contained in the timestamp, and the number value of the minute contained in the timestamp, respectively. (2 points)
3. Create a column called `bright` that takes the value of `1` when the column `Light` has a value above its average, and `0` otherwise. (1 point)
4. Create a column called `steamy` that takes the value of `1` when the column `Humidity` has a a value above its average AND the column `Temperature` has a value above its average (with avalue of `0` otherwise). (1 point)

NOTE: Please write ALL necessary code to complete the problem in the single blue cell below. Any code outside of the blue cell will not contribute to your scoring. Additionally, please note that spelling must be precise (and is case sensitive). Python doesn't know how to recognize variables unless they have *identical* spelling and capitalization.

