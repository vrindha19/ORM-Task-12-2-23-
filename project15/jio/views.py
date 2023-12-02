from django.shortcuts import render


from .models import Studentinfo

def student_list(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        movie_obj=Studentinfo(title=title,year=year,description=desc)
        movie_obj.save()
    return render(request,"student_list.html")



# modelform command

# views.py

# from django.shortcuts import render, redirect
# from .forms import StudentForm

# def student_view(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             # Process the form data and save to the database
#             form.save()
#             return redirect('success_page')
#     else:
#         form = StudentForm()

#     return render(request, 'hello.html', {'form': form})
 