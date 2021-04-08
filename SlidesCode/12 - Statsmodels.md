---
marp: true
title: Week 12 - Statsmodels and Sklearn
theme: default
class: default
size: 4:3
---

# Week 12 - Modeling through Statsmodels, Sklearn

---

# Customization vs Rapid Development

<br>

Building our own models is great!
- Understand the assumptions
- Get EXACTLY what you need

<br>

Unfortunately, it takes a LOT of time!


---

# Statsmodels

Let's make statistics in Python easy!

---

# Importing Statsmodels

We can import `statsmodels` in one of two ways:

1) With support for R-style formulas:

```python
import statsmodels.formula.api as sm
```

2) Using pre-built numpy arrays as inputs:

```python
import statsmodels.api as sm
```

We will focus on option (1) for now


---


# Preparing a Dataset

When using formulas, we prepare our dataset by importing the data into a Pandas `DataFrame`. We should take care that each of our variables has a name with 
1) **No spaces**
2) No symbols
3) Made up of letters and numbers (also can't have a number as the first character)


---


# Preparing a Dataset

Our code so far might look something like:

```python
import statsmodels.formula.api as smf
import pandas as pd, numpy as np

data = pd.read_csv("https://github.com/dustywhite7/Econ8320/blob/"
		+ "master/AssignmentData/assignment8Data.csv?raw=true")
```


---

# Regression Equations

`statsmodels` incorporates `R`-style regression equations by using the `patsy` library behind the scenes:

<br>

```independent variable ~ dependent variable + another dependent variable + any other dependent variables```

---


# Implementing a Model

The first thing we might try is a simple linear regression:

```python
reg = smf.ols("hhincome ~ year", data=data).fit()
print(reg.summary())
```

Or, I might want to try regressing year on the logged average household incomes:

```python
reg = smf.ols("np.log(hhincome) ~ year", data=data).fit()
print(reg.summary())
```

---


# Advancing our Model

It might be useful to create state-level fixed effects by including dummy variables for the states in our `statefip` column.

```python
reg = smf.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
print(reg.summary())
```
The `C()` command indicates that we would like to consider the `statefip` variable as a **C**ategorical variable, not a numeric variable.


---

# Additional Transformations

Sometimes we want to include transformed variables in our model:

```python
# Square a variable using the I() function for
#   mathematical transformations
reg = smf.ols("np.log(hhincome) ~ age + I(age**2)", 
	data=data).fit()
```

```python
# Combine variables using the I() function for
#   mathematical transformations
reg = smf.ols("np.log(hhincome) ~ I(age-education-5)", 
	data=data).fit()
```


---

# Robust Modeling

If we want to utilize robust standard errors, we can update our regression results:

```python
reg = smf.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
# Use White's (1980) Standard Error
reg.get_robustcov_results(cov_type='HC0')
print(reg.summary())
```

---

# More robust modeling

```python
reg = smf.ols("np.log(hhincome) ~ year + C(statefip)", 
	data=data).fit()
# Use Cluster-robust Standard Errors
reg.get_robustcov_results(cov_type='cluster', 
	groups=data['statefip']) # Need to specify groups
print(reg.summary())
```

---

# Robust Modeling

Below are some of the [covariance options](http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.get_robustcov_results.html) that we have:
1) `HC0`: White's (1980) Heteroskedasticity robust standard errors
2) `HC1`, `HC2`, `HC3`: MacKinnon and White's (1985) alternative robust standard errors, with `HC3` being designed for improved performance in small samples
3) `cluster`: Cluster robust standard errors
4) `hac-panel`: Panel robust standard errors

---

# Time Series Models

We have multiple time series options available.

- [ARIMA](http://www.statsmodels.org/dev/generated/statsmodels.tsa.arima_model.ARIMA.html) models
- [VAR](http://www.statsmodels.org/dev/generated/statsmodels.tsa.vector_ar.var_model.VAR.html) models
- [Exponential Smoothing](https://www.statsmodels.org/stable/tsa.html#exponential-smoothing) models


<!--

```python
from statsmodels.tsa.arima_model import ARIMA

y = data.loc[data['statefip']==31, ['hhincome','year']]
y.index=pd.to_datetime(y.year)
reg = ARIMA(y['hhincome'], order=(1,1,0)).fit()
print(reg.summary())
```


---


### Time Series Models

To implement a [VAR](http://www.statsmodels.org/dev/generated/statsmodels.tsa.vector_ar.var_model.VAR.html) model:

```python
from statsmodels.tsa.vector_ar.var_model import VAR

y = data.loc[data['statefip']==31, ['hhincome','year']]
y.index=pd.to_datetime(y.year)
reg = VAR(y['hhincome']).fit()
print(reg.summary())
```

The VAR model will optimize its own order (number of lags included) based on information criteria estimates.
-->

---


# Modeling Discrete Outcomes

If we have a binary dependent variable, we are able to use either [Logit]() or [Probit]() models to estimate the effect of exogenous variables on our outcome of interest. To fit a Logit model:

```python
import statsmodels.api as sm

myformula="married ~ hhincome + C(statefip) + C(year) + educ"
model= sm.Logit.from_formula(myformula, data=data).fit()
```

---

# Modeling Count Data

When modeling count data, we have options such as [Poisson](http://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.Poisson.html#statsmodels.discrete.discrete_model.Poisson) and [Negative Binomial](http://www.statsmodels.org/dev/generated/statsmodels.discrete.discrete_model.NegativeBinomial.html#statsmodels.discrete.discrete_model.NegativeBinomial) models.


```python
data = pd.read_csv("auto-mpg.csv")

myformula="nchild ~ hhincome + C(statefip) + C(year) + educ + married"
model= sm.Poisson.from_formula(myformula, data=data).fit()
```

---

# `patsy`: Using Regression Equations

Breaking out our regression equations!

---

# Why use `patsy`?

- We could just select our variables manually, and creating a column of ones is trivial (remember??)
- Patsy allows us to separate our endogenous and exogenous variables AND to
	- "Dummy out" categorical variables
	- Easily transform variables (square, or log transforms, etc.)
	- Use identical transformations on future data

---

# Why use `patsy` when `statsmodels` handles it for us?

By breaking out our regression equations, we can use the same data splits and processing steps for both `statsmodels` and for `sklearn` (which does not use `patsy`)!

---

# Getting Started

```python
import patsy as pt
import pandas as pd
import numpy as np

data = pd.read_csv("https://github.com/dustywhite7/Econ8320/blob/"
		+ "master/AssignmentData/assignment8Data.csv?raw=true")

# To create y AND x matrices
y, x = pt.dmatrices("hhincome ~ year + educ + married + age", 
		data = data)
        
# To create ONLY an x matrix
x = pt.dmatrix("~ year + educ + married + age", 
		data = data)
```

These regression equations automatically include an intercept term.

---

# Categorical Variables

```python
# To create y AND x matrices
eqn = "hhincome ~ C(year) + educ + married + age"
y, x = pt.dmatrices(eqn, data = data)
```

Categorical variables can be broken out into binary variables using the `C()` syntax inside of the regression equation. 

In this case, there would be binary variables for each unique value of `year`.

---

# Transforming Variables

```python
# To create y AND x matrices
eqn = "I(np.log(hhincome)) ~ C(year) + educ + married + age + I(age**2)"
y, x = pt.dmatrices(eqn, data = data)
```

We can transform variables using the `I()` syntax inside of the regression equation. We then use any numeric transformation that we choose to impose on our data. 

In this case, we logged our dependent variable, `hhincome`, and added the square of our `age` term.

---

# SUPER IMPORTANT $\rightarrow$ Same Transformation on New Data!

```python
# To create a new x matrix based on our previous version

xNew = pt.build_design_matrices([x.design_info], dataNew)
```

We can create a new matrix in the SAME SHAPE as our original `x` matrix by using the `build_design_matrices()` function in `patsy`. 

We pass a list containing the old design matrix information, as well as the new data from which to construct our new matrix.

---

# Why Does Recreating our `x` array Matter?

- Ensures that we always have the same number of categories
- Maintains consistency in our model
- Makes our work replicable
- AGAIN - :heart: streamlines the use of `statsmodels` and `sklearn` in the same workflow :heart:

---


# scikit-learn

see :robot: learn

learn, :robot:, learn!

---

# Predictive Modeling

What `statsmodels` does for regression analysis, `sklearn` does for predictive analytics and machine learning.

- Likely the most popular machine learning library today
- Has a standard API to make using the library VERY simple.


---

# Decision Tree Classification (and Regression)

[Classification](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier) and [Regression](http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor) Trees (CARTs) are the standard jumping-off point for exploring machine learning. They are very easy to implement in `sklearn`:

```python
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

pred = clf.pred(new_xs)

print(accuracy_score(new_ys, pred)
```

---

# Support Vector Machines

We also implement [Support Vector Machines](http://scikit-learn.org/stable/modules/svm.html#svm) for both [classification](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC) and [regression](http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR):

```python
from sklearn import svm
from sklearn.metrics import accuracy_score

clf = svm.SVC()
clf = clf.fit(x, y)

pred = clf.pred(new_xs)

print(accuracy_score(new_ys, pred)
```

Can you see the API pattern yet?

---

# Random Forest Models

Again, available in both [classification](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier) and [regression](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor) flavors, these models are aggregations of many randomized Decision Trees.

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

clf = RandomForestClassifier(n_estimators=50)
clf = clf.fit(x, y)

pred = clf.pred(new_xs)

print(accuracy_score(new_ys, pred)
```
There MUST be a pattern here...


---

# Data Preprocessing

Many other tools are also available to aid in the data cleaning process through `sklearn`. Some of these are:

- [Principal Component Analysis (PCA)](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA)
- [Factor Analysis](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.FactorAnalysis.html#sklearn.decomposition.FactorAnalysis)
- Many [Cross-Validation Algorithms](http://scikit-learn.org/stable/modules/cross_validation.html)
- [Hyperparameter Tuning](http://scikit-learn.org/stable/modules/grid_search.html)
   - Finding the correct parameters for a decision tree or random forest, for example
- [Model Evaluation Tools](http://scikit-learn.org/stable/modules/model_evaluation.html)



---

# Lab time!