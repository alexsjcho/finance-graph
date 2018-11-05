from pandas_datareader import data
import datetime

start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)

df=data.DataReader(name="APPL",data_source="google",start=start,end=end)
