
# -*- coding: utf-8 -*-
 
from django.shortcuts import render_to_response
from django.views.decorators import csrf
from . import task2
import time
from django.http import HttpResponse
from django.template import RequestContext
# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
       
        keywords = str(ctx['rlt'])
        keywords_sorted = task2.sort(keywords)
        ctx['key'] = keywords_sorted
        url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
        search = 'esearch.fcgi?db=pubmed&retmax=10&term='
        summary = 'esummary.fcgi?db=pubmed&id='
        listing = task2.List()
        tool = task2.Tool()
        Litera = task2.Literature(url,search,summary,keywords_sorted,tool)
        Id_num = Litera.get_uid()
        file_name = "/var/mysite/commonstatic/"+keywords_sorted+".txt"
        listing.create(file_name,Litera,Id_num)
        
    return render_to_response( "post.html", ctx)
def file_download(request):
    
    with open('/var/mysite/paper/static/1.txt',encoding='UTF-8') as f:
        c = f.read()
    return HttpResponse(c)
    
      
