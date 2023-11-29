from django.shortcuts import render

def home(request):
    return render(request, "arabic/home.html")



def phase1(request):
    return render(request, 'arabic/Phase_1.html')

def easy(request):
    return render(request, "Phase_1/Easy.html")

def easyquiz(request):
    return render(request, 'Phase_1/Easyquiz.html')

def medium(request):
    return render(request, "Phase_1/Medium.html")

def mediumquiz(request):
    return render(request, 'Phase_1/Mediumquiz.html')

def hard(request):
    return render(request, "Phase_1/Hard.html")

def hardquiz(request):
    return render(request, 'Phase_1/Hardquiz.html')

def phase2(request):
    return render(request, 'arabic/Phase_2.html')

def P2easy(request):
    return render(request, "Phase_2/Easy.html")

def P2easyquiz(request):
    return render(request, 'Phase_2/Easyquiz.html')

def P2medium(request):
    return render(request, "Phase_2/Medium.html")

def P2mediumquiz(request):
    return render(request, 'Phase_2/Mediumquiz.html')

def P2hard(request):
    return render(request, "Phase_2/Hard.html")

def P2hardquiz(request):
    return render(request, 'Phase_2/Hardquiz.html')
