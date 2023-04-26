from django.shortcuts import render

from .models import Student,Markss

# Create your views here.



def home(request):
   return render(request,'tmain.html')



def cse(request):
   
   return render(request,'main/cse.html')


def chemical(request):
   
   return render(request,'main/chemical.html')


def civil(request):
   
   return render(request,'main/civil.html')


def entc(request):
   
   return render(request,'main/entc.html')


def mech(request):
   
   return render(request,'main/mech.html')


def electrical(request):
   
   return render(request,'main/electrical.html')


def it(request):
   
   return render(request,'main/it.html')


def production(request):
   
   return render(request,'main/production.html')


def textile(request):
   
   return render(request,'main/textile.html')


def instru(request):
   
   return render(request,'main/instru.html')
   




def savedata(request):
    n=""
    
    if(request.method=='POST'):
     Name=request.POST.get('name')
     RegNo=request.POST.get('regno')
     YearofJoining=request.POST.get('joinyear')
     PassingYear=request.POST.get('passyear')
     Mobno=request.POST.get('mbno')
     Email=request.POST.get('email')
     Add=request.POST.get('add')
     NoofTranscript=request.POST.get('not')



     np=Student(Name=Name,RegNo=RegNo,Year_of_Joining=YearofJoining,Email= Email, Phone_Number=Mobno, Passing_year=PassingYear,Address= Add ,  No_of_Transcript_R=NoofTranscript )
     np.save()
     n="data inserted suceessfully"
  
    return render(request,'main/cse.html',{'n':n})


def savedata2(request):
   o=""
   if (request.method=='POST'):

        sem1=request.POST.get('first_sem')
        sem2=request.POST.get('second_sem')
        sem3=request.POST.get('third_sem')
        sem4=request.POST.get('fourth_sem')
        sem5=request.POST.get('fifth_sem')
        sem6=request.POST.get('six_sem')
        sem7=request.POST.get('seventh_sem')
        sem8=request.POST.get('eight_sem')




        en=Markss(sem1=sem1,sem2=sem2,sem3=sem3,sem4=sem4,sem5=sem5,sem6=sem6,sem7=sem7,sem8=sem8)
        en.save()
      
        o="data inserted successfully"

   return render (request,'main/cse.html',{'o':o}) 









