from django.shortcuts import render

from .models import PDF
from .forms import PdfForm

from .llm import retrieve_data

def home(request):
    
    return render(request,"core/home.html")
    

def ChatPDF(request):
    if request.method=='POST':
        form=PdfForm(request.POST,request.FILES)
        if form.is_valid():
            pdfs=PDF.objects.all()
            for pdf in pdfs:
                pdf.delete()
            form.save()
        else:
            return(request,"core/base.html",{"form":form})
    context={'form':PdfForm(),"text":""}
    if request.method == 'GET':
        query=request.GET.get("data")
        obj=PDF.objects.all()[0]
        ans=retrieve_data(obj.pdf,query)
        context["text"]=ans
        return render(request,"core/base.html",context)
    return render(request,"core/base.html",context)
