from django.shortcuts import render

# Create your views here.
def home(request ):
    return render(request , 'enroll/home.html')
#def show_details(request , my_id):
#    sai ={'id':my_id}
#   return render(request , 'enroll/show.html' , sai)

def show_details(request , my_id):    
    if my_id == 1:
        sai ={'id':my_id , 'name':'Sai'}
    if my_id == 2:
        sai ={'id':my_id , 'name':'Rasika'}
    if my_id == 3:
        sai ={'id':my_id , 'name':'Mummy'}        
    return render(request , 'enroll/show.html' , sai)

def show_subdetails(request , my_id , my_subid):
    if my_id == 1 and my_subid == 4:
        sai ={'id':my_id , 'name':'Sai' , 'info':'Sub Details'}
    if my_id == 2 and my_subid == 5:
        sai ={'id':my_id , 'name':'Rasika' , 'info':'Sub Details'}
    if my_id == 3 and my_subid == 6:
        sai ={'id':my_id , 'name':'Mummy' , 'info':'Sub Details'}        
    return render(request , 'enroll/show.html' , sai)

