#Libraries
from pandas_datareader import data
import datetime
from bokeh.plotting figure,show, output_file

#Time variables
start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)
hours_12=12*60*60*1000

#Price variables
date_increase=df.index[df.Close > df.Open]
date_decrease=df.index[df.Close < df.Open]

#Data pulling and Graph rendering
df=data.DataReader(name="APPL",data_source="google",start=start,end=end)
p=figure(x_axis_type='datatime', width=1000, height=300)
p.title.text= "Candlestick Chart"

#Open and Close price logic
def in_dec(c, o):
    if c > o:
        value="Increase"
    elif c < o:
        value="Decrease"
    else: value="Equal"
    return value

#Dataframe variables 
df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close, df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Close-df.Open)

#Open, Close price visual rendering logic
p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],[df.Close > df.Open],(df.Open_df.Close)/2,df.Height[df.Status=="Increase"],
fill_color="green",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],[df.Close < df.Open],(df.Open_df.Close)/2,df.Height[df.Status=="Decrease"],
fill_color="red",line_color="black")

output_file("CS.html")
show(p)
