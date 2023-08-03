from django.shortcuts import render

# Create your views here.
def skill(request):
    dict={'Skill':'active'}
    return render(request,'edu/skill.html',dict)