from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {'form': form})
