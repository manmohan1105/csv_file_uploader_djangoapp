import logging
from django.shortcuts import render,HttpResponse
from django.contrib import messages
import pandas as pd
# Create your views here.
def index(request):
    data=[]
    if request.method == 'GET':
        return render(request, 'index.html')
    if request.method=='POST':
            csv_file = request.FILES["csv_file"]
            print("1")
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'File is not CSV type')
                return render(request,'index.html',{'data':data})
            print("1")
            # if csv_file.multiple_chunks():
            #     messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
            #     return render(request,'index.html',{'data':data})
            print("1")
           	
            df=pd.read_csv(csv_file,encoding='latin1')
            print(df)
            print("1")
            table_object=df.to_html()
  
            return HttpResponse(table_object)
            # lines = file_data.split("\n")

            # for line in lines:						
            #     fields = line.split(",")
            #     data_dict = {}
            #     data_dict["name"] = fields[0]
            #     data_dict["no"] = fields[1]
            #     data_dict["address"] = fields[2]
            #     data_dict["company"] = fields[3]
            #     data.append(data_dict)
            # return render(request,'index.html',{'data':data})
    return render(request,'index.html',{'data':data})
