from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

from django.contrib import auth
from django.http import HttpResponse
from django.template import loader

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required

#==================================

def pricing(request):
    return render(request, 'pricing.html', locals())

def feature(request):
	return render(request, 'plotly.html', locals())

@login_required(login_url='/accounts/login/')
def Comment(request):
	return render(request, 'Comment.html', locals())

@login_required(login_url='/accounts/login/')
def Chart(request):
	return render(request, 'Chart.html', locals())

@login_required(login_url='/accounts/login/')
def Renew(request):
	return render(request, 'Renew.html', locals())

#==================================

# Plotly + Django
# from django.shortcuts import render
# from plotly.offline import plot
# from plotly.graph_objs import Scatter

# import numpy as np
# import pandas as pd

# import plotly as py
# import plotly.graph_objs as go

# from plotly.offline import plot
# import plotly.figure_factory as ff
# from plotly.colors import DEFAULT_PLOTLY_COLORS
# from collections import Counter 
# import random
# from datetime import datetime
# import jieba.analyse
# from functools import reduce


# import pymongo
# import requests
# from pymongo import MongoClient
# import bs4

#=================================Plotly embedding==============================

# pyplt = py.offline.plot

# width = 1024
# height = 786

# list_phone_type = [
# "ZenFone 6",
# "ROG Phone",
# "ZenFone Max Pro" ,
# #"ZenFone Max M2",

# "iPhone 11",

# "Galaxy Note 10",
# "Galaxy A20",
# #"Galaxy A30s",
# "Galaxy A70",
# "Galaxy A50",

# #"AX5s",
# #"A9 2020",
# "Reno 2"
# ]


# def normalize(counts,max_count=100):
#     max_ = max(counts) 
#     min_ = min(counts)
#     counts = [int(((c-min_)/(max_-min_+1))*max_count)+1 for c in counts] 
#     return counts

# def line_break(text,span=100):
#    if not isinstance(text,str):
#        return text
#    texts = []
#    for i,t in enumerate(text.strip()):
#        texts.append(t)
#        if i%span==0 and i!=0:
#            texts.append("<br>")
#    return "".join(texts)

# def table_plot(df):
#     titles = [line_break(TITLE,span=20) for TITLE in df.TITLE ]
#     titles = ['<a href="%s">%s</a>'%(u,t) for u,t in zip(df.LINK,titles)] 
#     table = go.Table(
#         columnwidth = [0.09*width,0.28*width,0.49*width,0.07*width,0.07*width],
#         header=dict(
#           values=["<b>DATE</b>","<b>TITLE</b>","<b>TEXT</b>","<b>SOURCE</b>","<b>author</b>"],
#           fill = dict(color='#C2D4FF'),
#           align = 'left',
#           height = 30
#         ),
#         cells=dict(
#           values=[df.DATE,\
#                   titles,
#                   df.TEXT.apply(lambda x: x[:40]+'...'),\
#                   df.SOURCE.apply(lambda x: line_break(x,span=4))],
#           fill = dict(color='#F5F8FF'),
#           align = 'left',
#           height = 30
#         )
#     )
#     return plot([table], output_type='div',include_plotlyjs=False)

# def create_wordcount(df,xaxis='x1',yaxis='y1'):
#     df = df.assign(day=df.DATE.apply(lambda x:x.DATE()))
#     counts = df.groupby(['day']).size() 
#     days = sorted(list(set(df.day)))
#     data = go.Scatter(
#         x=days,
#         y=counts,
#         xaxis=xaxis, 
#         yaxis=yaxis, 
#     )  
#     return data 

# def create_wordcloud(df,most_count=30):
#     texts =[jieba.analyse.extract_tags(row) for row in df.TEXT]
#     texts = reduce(lambda x,y: x+y,texts) 
#     texts = Counter(texts)
#     texts = texts.most_common(most_count)
#     weights = [row[1] for row in texts]
#     weights = normalize(weights)
#     texts = [row[0] for row in texts]
#     colors = [DEFAULT_PLOTLY_COLORS[random.randrange(1, 10)] for i in range(most_count)]
#     data = go.Scatter(x=[random.uniform(5, 20) for i in range(most_count)],
#                       y=[random.uniform(5, 20) for i in range(most_count)],
#                       mode='text',
#                       text=texts,
#                       marker={'opacity': 0.3},
#                       textfont={'size': weights,
#                                 'color': colors}
#     )
#     return data 

# def count_plot(df):
#     wcount = create_wordcount(df)
#     layout = go.Layout(
#         width=width/2,
#         height=height,
#         #margin = dict(t=100),
#         #autosize=False,
#         #xaxis1=dict(
#         #    domain=[0, 0.5],
#         #),
#         #xaxis2=dict(
#         #    domain=[0.55, 1],
#         #),
#     )
#     fig = go.Figure(data=[wcount], layout=layout)
#     return  plot(fig,output_type='div',include_plotlyjs=False) 

# def cloud_plot(df):
#     wcloud = create_wordcloud(df)
#     layout = go.Layout(
#         xaxis=dict(
#             showline=False,
#             showgrid=False,
#             showticklabels=False,
#             zeroline=False
#         ),
#         yaxis=dict(
#             showline=False,
#             showgrid=False,
#             showticklabels=False,
#             zeroline=False
#         ),
#         width=width/2,
#         height=height
#     )
#     fig = go.Figure(data=[wcloud], layout=layout)
#     return  plot(fig,output_type='div',include_plotlyjs=False) 

# def table_plot1(df):
#     colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]
#     LINKs = df.LINK
#     df = df.drop(["id","LINK"],axis=1)
#     df["TEXT"] = df["TEXT"].apply(line_break)
#     df = df.iloc[:5]
#     figure = ff.create_table(df,height_constant=200, colorscale=colorscale)
#     plot_table = plot(figure, output_type='div',include_plotlyjs=False)
#     return plot_table

#=================================Use Plotly====================================
# class Chart_Plot:
#     def __init__(self):
#         pass

#     def cloud_graph(self):

#         client = pymongo.MongoClient("mongodb+srv://yuehhung_hsieh:a25641850,@database-version1-eh1vv.gcp.mongodb.net/test?retryWrites=true&w=majority")
#         db = client.test
#         df = pd.DataFrame(list(db.ck101.find()))
#         df = df[[
#                         "SOURCE",      
#                         "BRAND",
#                         "TYPE",
#                         "DATE", 
#                         "TITLE",
#                         "TEXT",
#                         "LINK",
#                         "REPLY_NUM",
#                         "GOOD",
#                         "BAD",
#                         "SHARE_TIMES",

#         ]]

#         return cloud_plot(df)

# def index(request):

# 	chart = Chart_Plot()

# 	plot_div = chart.cloud_graph()

# 	return render(request, "plotly.html", context={'plot_div': plot_div})


#=============================================================================
