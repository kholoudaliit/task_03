from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    "my_list" : [
	    {"restaurant_name":"Section-B"  ,"food_type":"Burgers"}, 
	    {"restaurant_name":"Medd" ,"food_type":"Cafe"}, 
	    {"restaurant_name":"Meez" ,"food_type":"Middle East Food"}, 
    ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
		"my_object" : {"restaurant_name":"Section-B"  ,"food_type":"Burgers"},
    }
    return render(request, 'detail.html', context)
