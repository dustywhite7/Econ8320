import statsmodels.formula.api as sm
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
  'mysql+mysqlconnector://viewer:@dadata.cba.edu:3306/ACS'
 	  )
      
SELECT = """SELECT AVG(hhincome) AS hhincome, year,
    statefip
  FROM ACS
  GROUP BY year, statefip ORDER BY year, statefip"""

data = pd.read_sql(SELECT, engine)

reg = sm.ols("np.log(hhincome) ~ year", data=data).fit()
print(reg.summary())


#%%

reg = sm.ols("np.log(hhincome) ~ year + C(statefip)", data=data).fit()
print(reg.summary())

#%%

from statsmodels.tsa.arima_model import ARIMA

y = data.loc[data['statefip']==31, ['hhincome','year']]
y.index=pd.to_datetime(y.year)
reg = ARIMA(y['hhincome'], order=(1,1,0)).fit()
print(reg.summary())
