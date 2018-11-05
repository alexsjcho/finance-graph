#Libraries
import datetime
from pandas_datareader import data
from bokeh.plotting import figure,show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

#Time variables
start=datetime.datetime(2016,3,1)
end=datetime.datetime(2016,3,10)
hours_12=12*60*60*1000

#Price variables
date_increase=df.index[df.Close > df.Open]
date_decrease=df.index[df.Close < df.Open]

#Data pulling and Graph rendering
df=data.DataReader(name="APPL",data_source="google",start=start,end=end)
p=figure(x_axis_type='datatime', width=1000, height=300, sizing_mode="scale_width")
p.title.text= "Candlestick Chart"
p.grid.grid_line_alpha=0.3

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
p.segment(df.index,df.High, df.index, df.Low, color="Black")

p.rect(df.index[df.Status=="Increase"],df.Middle[df.Status=="Increase"],[df.Close > df.Open],(df.Open_df.Close)/2,df.Height[df.Status=="Increase"],
fill_color="green",line_color="black")

p.rect(df.index[df.Status=="Decrease"],df.Middle[df.Status=="Decrease"],[df.Close < df.Open],(df.Open_df.Close)/2,df.Height[df.Status=="Decrease"],
fill_color="red",line_color="black")

#Frontend variables
script1, div1, = components(p)
cdn_js=CDN.js_files[0]
cdn_css=CDN.css_files[0]
return render_template("plot.html",
script1=script1, div1=div1,
cdn_css=cdn_css, cdn_js=cdn_js)

#Call scripts
#output_file("CS.html")
#show(p)
