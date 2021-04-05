from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
# pk_9bfaacd5afab418fb4289b4dbaebdf02
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=sk_7a542870823044e9b32551a6008e3e61")
        try:
            api = json.loads(api_request.content)
        except Exception as e :
            api = e
        return render(request,'home.html',{'api':api})
    else:
        return render(request,'home.html',{'ticker':'Enter something'})


def addstock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("Stock is added"))
            return redirect('addstock')
    else:
        ticker = Stock.objects.all()
        output = []
        for tick in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(tick) + "/quote?token=sk_7a542870823044e9b32551a6008e3e61")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e :
                api = e
        return render(request, 'addstock.html',{'ticker':ticker,'output':output})

def delete(request, list_id):
    item = Stock.objects.get(pk=list_id)
    item.delete()
    messages.success(request,('Stock is deleted'))
    return redirect(addstock)
    
