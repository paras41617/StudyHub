from django.shortcuts import render, redirect
from .models import Material, Category, Grade

def submit_material(request):
    if request.method == 'POST':
        # Get form data from request
        name = request.POST['name']
        file = request.FILES.get('file')
        url = request.POST['url']
        category = request.POST['category']
        new_category = request.POST.get('new_category', '')
        grade = request.POST['grade']
        new_grade = request.POST.get('new_grade', '')

        # Create or get Category and Grade objects based on user input
        if category == 'new' and new_category:
            category = Category.objects.create(name=new_category)
        else:
            category = Category.objects.get(pk=category)

        if grade == 'new' and new_grade:
            grade = Grade.objects.create(name=new_grade)
        else:
            grade = Grade.objects.get(pk=grade)

        # Create and save Material object
        material = Material(name=name, file=file, url=url, category=category, grade=grade)
        material.save()

        return redirect('material_list')

    # Get all categories and grades for rendering the template
    categories = Category.objects.all()
    grades = Grade.objects.all()
    return render(request, 'submit_material.html', {'categories': categories, 'grades': grades})

def material_list(request):
    # Get all materials, categories, and grades for rendering the template
    materials = Material.objects.all()
    categories = Category.objects.all()
    grades = Grade.objects.all()
    return render(request, 'material_list.html', {'materials': materials, 'categories': categories, 'grades': grades})

def material_category(request, category_id):
    # Get the Category object based on the category_id parameter
    category = Category.objects.get(pk=category_id)
    # Filter materials based on the category
    materials = Material.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'material_list.html', {'materials': materials, 'categories': categories})

def material_search(request):
    # Get search parameters from the request
    query = request.GET.get('q')
    category = request.GET.get('category')
    grade = request.GET.get('grade')

    # Get all categories and grades for rendering the template
    categories = Category.objects.all()
    grades = Grade.objects.all()

    # Get all materials initially
    materials = Material.objects.all()

    # Apply filters based on search parameters
    if query:
        materials = materials.filter(name__icontains=query)
    if category and category != "None":
        materials = materials.filter(category__name=category)
    if grade and grade != "None":
        materials = materials.filter(grade__name=grade)

    # Prepare context data for rendering the template
    context = {
        'materials': materials,
        'categories': categories, 
        'grades': grades
    }

    return render(request, 'material_list.html', context)
