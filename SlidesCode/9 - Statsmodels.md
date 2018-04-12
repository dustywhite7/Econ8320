<!--
$theme: gaia
template: invert
-->

### Week 9 - Statistical Modeling through Statsmodels

---

### Customization vs Rapid Development

<br>

Building our own models is great!
- Understand the assumptions
- Get EXACTLY what you need

<br>

Unfortunately, it takes a lot of time!


---


### Importing Statsmodels

We can import `statsmodels` in one of two ways:

1) With support for R-style formulas:

```python
import statsmodels.formula.api as sm
```

2) Using pre-built numpy arrays as inputs:

```python
import statsmodels.api as sm
```

We will focus on option (1)


---


### Preparing a Dataset

When using formulas, we prepare our dataset by importing the data into a Pandas `DataFrame`. We should take care that each of our variables has a name with 
1) **No spaces**
2) No symbols
3) Made up of letters and numbers (also can't have a number as the first character)


---


### Preparing a Dataset

Our code so far might look something like:

```python
import statsmodels.formula.api as sm
from sqlalchemy import create_engine
import pandas as pd, numpy as np

engine = create_engine(
  'mysql+mysqlconnector://viewer:@dadata.cba.edu:3306/ACS'
 	  )
      
SELECT = """SELECT AVG(hhincome) AS hhincome, year,
    statefip
  FROM ACS
  GROUP BY year, statefip 
  ORDER BY year, statefip"""

data = pd.read_sql(SELECT, engine)
```


---


### Implementing a Model

The first thing we might try is a simple linear regression:

```python
reg = sm.ols("hhincome ~ year", data=data).fit()
print(reg.summary())
```

Or, I might want to try regressing year on the logged average household incomes:

```python
reg = sm.ols("np.log(hhincome) ~ year", data=data).fit()
print(reg.summary())
```

---


### Advancing our Model

It might be useful to create state-level fixed effects by including dummy variables for the states in our `statefip` column.

```python
reg = sm.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
print(reg.summary())
```
The `C()` command indicates that we would like to consider the `statefip` variable as a **C**ategorical variable, not a numeric variable.


---

### Additional Transformations

Sometimes we want to include transformed variables in our model:

```python
# Square a variable using the I() function for
#   mathematical transformations
reg = sm.ols("np.log(hhincome) ~ age + I(age**2)", 
	data=data).fit()
```

```python
# Combine variables using the I() function for
#   mathematical transformations
reg = sm.ols("np.log(hhincome) ~ I(age-education-5)", 
	data=data).fit()
```


---

### Robust Modeling

If we want to utilize robust standard errors, we can update our regression results:

```python
reg = sm.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
# Use White's (1980) Standard Error
reg.get_robustcov_results(cov_type='HC0')
print(reg.summary())

--------------------------------------------------------

reg = sm.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
# Use Cluster-robust Standard Errors
reg.get_robustcov_results(cov_type='cluster', 
	groups=data['statefip']) # Need to specify groups
print(reg.summary())
```

---

### Robust Modeling

Below are some of the [covariance options](http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html) that we have:
1) `HC0`: White's (1980) Heteroskedasticity robust standard errors
2) `HC1`, `HC2`, `HC3`: MacKinnon and White's (1985) alternative robust standard errors, with `HC3` being designed for improved performance in small samples
3) `cluster`: Cluster robust standard errors
4) `hac-panel`: Panel robust standard errors

---

### Time Series Models

We have multiple time series options available.


To implement an ARIMA(1,1,0) model:

```python
from statsmodels.tsa.arima_model import ARIMA

y = data.loc[data['statefip']==31, ['hhincome','year']]
y.index=pd.to_datetime(y.year)
reg = ARIMA(y['hhincome'], order=(1,1,0)).fit()
print(reg.summary())
```


---


### Time Series Models

