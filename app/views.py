from django.shortcuts import render, redirect
from .forms import MaterialForm
from .models import Material, Category, Grade

from django.shortcuts import render, redirect
from .models import Material, Category, Grade

def submit_material(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.FILES.get('file')
        url = request.POST['url']
        category = request.POST['category']
        new_category = request.POST.get('new_category', '')
        grade = request.POST['grade']
        new_grade = request.POST.get('new_grade', '')

        if category == 'new' and new_category:
            category = Category.objects.create(name=new_category)
        else:
            category = Category.objects.get(pk=category)

        if grade == 'new' and new_grade:
            grade = Grade.objects.create(name=new_grade)
        else:
            grade = Grade.objects.get(pk=grade)

        material = Material(name=name, file=file, url=url, category=category, grade=grade)
        material.save()

        return redirect('material_list')

    categories = Category.objects.all()
    grades = Grade.objects.all()
    return render(request, 'submit_material.html', {'categories': categories, 'grades': grades})

def material_list(request):
    materials = Material.objects.all()
    categories = Category.objects.all()
    grades = Grade.objects.all()
    return render(request, 'material_list.html', {'materials': materials, 'categories': categories, 'grades': grades})

def material_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    materials = Material.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'material_list.html', {'materials': materials, 'categories': categories})

def material_search(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    grade = request.GET.get('grade')
    categories = Category.objects.all()
    grades = Grade.objects.all()


    materials = Material.objects.all()

    if query:
        materials = materials.filter(name__icontains=query)
    if category and category != "None":
        materials = materials.filter(category__name=category)
    if grade and grade != "None":
        materials = materials.filter(grade__name=grade)

    context = {
        'materials': materials,
        'categories': categories, 
        'grades': grades
    }

    return render(request, 'material_list.html', context)