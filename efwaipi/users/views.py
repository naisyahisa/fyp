from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth, messages
#only login user could see profile page
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from blog.models import Vaksinasi
from .serializer import *
from .forms import UserRegisterForm #helpForm
from django.http import JsonResponse, response, HttpResponse
from rest_framework.response import Response
from collections import OrderedDict

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts

def register(request):
    currentUserDet = user_auth.models.User.objects.get(id=id)
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #including encryption for the password
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users_act/register.html', {'form': form}) 

# @ is to add functionalities to a function
@login_required
def profile(request):
    return render(request, 'users_act/profile.html')


@login_required
def dashboard(request):
    if request.method == 'GET':
        vac = Vaksinasi.objects.all()
        # ser = VacSerializer(vac, many=True)
        print("#########masuk view db")
        #[{"id": 1, "district": "Baling"}, {"id": 2, "district": "Sik"}...]
    
        district = []
        year = []
        vacAble = []
        vacDone = []
        percent = []
        #iterate objects.all
        for x in vac:
            perc = round((x.vac_done/x.vac_able)*100,2)
            context = {
                'id':x.id,
                'district':x.district,
                'year':x.year,
                'vac_able':x.vac_able,
                'vac_done':x.vac_done
            }
            #main lists
            district.append(x.district)
            year.append(x.year)
            vacDone.append(x.vac_done)
            vacAble.append(x.vac_able)
            percent.append(perc)
        # print(percent)
        #before jadi lable data kenaa classify ikut tahun
        labellist = []
        labeldata = []
        labelyear = []
        for i in range(len(year)):
            if year[i] == 2018:
                labellist.append(district[i])
                labeldata.append(percent[i])
                labelyear.append(year[i])
        # print(labellist)
        # print(labeldata)
        # print(labelyear)
        #from the lists, satu label data, satu data betul, 
        #jadi dict, ada key, from label
        #jadi key value array
        # dict['singlebardict'] = singlebardict
        # jadi unhashable dict
        singlebardict = {}
        # labellist = list untuk label data
        for key in labellist:
            #labeldata untuk data yg disimpan
            for value in labeldata:
                singlebardict[key] = value
                labeldata.remove(value)
                break
        # print(singlebardict)
        # {'Baling': 63.69, 'Sik': 89.91, 'Alor Setar': 66.04, 'Sungai Petani': 91.4, 'Kubang Pasu': 86.41, 
        # 'Langkawi': 90.54, 'Pendang': 89.82, 'Kulim': 98.16, 'Yan': 46.9, 'Padang Terap': 83.99, 
        # 'Pokok Sena': 84.47, 'Bandar Baharu': 89.71}
        # print("this is key value array")
        # dict = {}
        # context = dict['singlebardict'] = singlebardict
        # return JsonResponse(list, safe=False)
        # print("--------context")
        # print(context)
        chartConfig = OrderedDict()
        chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
        chartConfig["subCaption"] = "In MMbbl = One Million barrels"
        chartConfig["xAxisName"] = "Country"
        chartConfig["yAxisName"] = "Reserves (MMbbl)"
        chartConfig["numberSuffix"] = "K"
        chartConfig["theme"] = "fusion"
        
        dataSource = OrderedDict()

        dataSource["data"].append({"label": 'Venezuela', "value": '290'})
        dataSource["data"].append({"label": 'Saudi', "value": '290'})
        dataSource["data"].append({"label": 'Canada', "value": '180'})
        
        dataSource["chart"] = chartConfig
        
        # dataSource["data"] = [singlebardict]
        column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
        return render(request, 'users_act/dashboard.html', {'output': column2D.render()})
        # return render(request, 'users_act/dashboard.html', singlebardict)
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
def myFirstChart(request):
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  dataSource = OrderedDict()

# The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
  chartConfig["subCaption"] = "In MMbbl = One Million barrels"
  chartConfig["xAxisName"] = "Country"
  chartConfig["yAxisName"] = "Reserves (MMbbl)"
  chartConfig["numberSuffix"] = "K"
  chartConfig["theme"] = "fusion"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []

 # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
# Insert the data into the `dataSource['data']` list.
#   dataSource["data"].append({"label": 'Venezuela', "value": '290'})
#   dataSource["data"].append({"label": 'Saudi', "value": '290'})
#   dataSource["data"].append({"label": 'Canada', "value": '180'})
#   dataSource["data"].append({"label": 'Iran', "value": '140'})
#   dataSource["data"].append({"label": 'Russia', "value": '115'})
#   dataSource["data"].append({"label": 'Russia', "value": '115'})
#   dataSource["data"].append({"label": 'UAE', "value": '100'})
#   dataSource["data"].append({"label": 'US', "value": '30'})
#   dataSource["data"].append({"label": 'China', "value": '30'})
  
#   print(dataSource)
# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
#   column2D = FusionCharts("column2d", "myFirstChart", "600", "400", "myFirstchart-container", "json", dataSource)
#   return render(request, 'index.html', {
#     'output': column2D.render()
# })
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
@login_required
def helpdesk(request):
    return render(request, 'users_act/helpdesk.html')

# def form_view(request):
#     form = helpForm()
#     if request.method == 'POST':
#         form = helpForm(request.POST)
#         if form.is_valid():

# class BarChartView(TemplateView):
#     template_name = "users_act/chart-apex.html"
    
#     def chart(self):
#         return Vaksinasi.objects.all()

    #insert dynamic chart
    #create query set and pass to js
    # def get_context_data(self, **kwargs): 
    #     context = super().get_context_data(**kwargs)
    #     context["qs"] = Vaksinasi.objects.all()
    #     return context