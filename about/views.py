from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    """
    Display the about page with information about the blog.
    
    **Context**

    ``about``
        An instance of :model:`about.About`.
        
    **Template:**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )