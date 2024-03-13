from django.shortcuts import render ,redirect,reverse
from django.http import HttpResponse, HttpResponseRedirect

from . import models
from . forms import ReviewForm


# Create your views here.
# def simple_view(request):
#     return HttpResponse("Hello, this is the first view of my_lib app")
#
# articles = {
#     'stories': 'This is my stroy page',
#     'Novels': 'This is my novel page',
#     'Politics': 'This is my Politis page'
# }
# def lib_news(request, topic):
#     return HttpResponse(articles[topic])
#
# def journolism(request, event):
#     return HttpResponse(name[event])
#
# name = {
#     'Zentv':'Involed in my story',
#     'Mtv': 'Identity for incedian'
# }
#
#  example for path converter -- django documents

# def add_views(request,num1,num2):
#     # domain.com/my_library/num1/num2
#     add_res = num1 + num2
#     result = f"{num1}+{num2} = {add_res}"
#     return HttpResponse(str(result))

# def template_simple_view(request):
#      my_library/templates/my_library/example.html
#   return render(request,"my_library/example.html")

# def variable_view(request):
#    my_var = {'first_name': 'roselind','last_name':'franklin',
#              #'some_list':[2,4,6,2,8],
#              #'some_dict':{'my_key':'my_value'},
#              'user_logged_in':True,
#              #'user_logged_in':False
#              }
#    return render(request,'my_library/variable.html', context=my_var)
#
# def thank_you(request):
#    return render(request,'my_library/thank_you.html')

def list_customers(request):
    all_customers = models.Customers.objects.all()
    context_list = {'Customers': all_customers}
    return render(request,'Library/list.html', context=context_list)

def add(request):
    # print(request.POST)
    if request.POST:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        models.Customers.objects.create(first_name=first_name,last_name=last_name,age=age)
        return redirect(reverse('Library:list_customers'))
    else:
        return render(request, 'Library/add.html')

def delete(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Customers.objects.get(pk='pk').delete()
            return redirect(reverse('Library:list_customers'))
        except:
            print("pk id not found")
            return redirect(reverse('Library:list_customers'))
    else:
        return render(request, 'Library/delete.html')


def rental_review(request):
    #POST request ---->  form contents-----> thank you
    if request.method =='POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            #form.save()
            return redirect(reverse('my_library:thank_you'))
    else:
        form = ReviewForm()
        return render(request,'my_library/rental_review.html',context={'form': form})

def thank_you(request):
    return render(request,'my_library/thank_you.html')