from django.shortcuts import render

# Create your views here.
def index(request):
    """
    A functional based view for the landing page view
    """

    return render(request, "index.html")
