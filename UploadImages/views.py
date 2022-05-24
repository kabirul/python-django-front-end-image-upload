from django.shortcuts import render, HttpResponse
from .forms import ImageForm

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            img_object = form.instance
            return render(request, 'upload.html', {'form': form, 'img_obj': img_object})
            #return HttpResponse('The file is saved')
    else:
        form = ImageForm()
        context = {
            'form':form,
        }
    return render(request,'upload.html', context)

