from django.shortcuts import render

# Create your views here.
from app import forms
from django.core.files.storage import FileSystemStorage

def image(request):
    form=forms.Image()
    if request.method=='POST' and request.FILES:#checking method is POST and FILES
        form_data=forms.Image(request.POST,request.FILES)#collecting data u have enterd
        if form_data.is_valid():#form uploaded is valid or not
            img=form_data.cleaned_data['image']#collected image from cleaned data
            fs=FileSystemStorage()#created instance for FSS
            file=fs.save(img.name,img)#by using save method we are saving into media folder
            img_url=fs.url(file)
            return render(request,'display.html',context={'img_url':img_url})

    return render(request,'image.html',context={'form':form})
