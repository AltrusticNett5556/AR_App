# views.py
from django.shortcuts import render

def home(request):
    # Check if the 'click_counter' exists in the session, if not, initialize it
    if 'click_counter' not in request.session:
        request.session['click_counter'] = 0

    # Check if the request is a POST to increment the counter
    if request.method == 'POST':
        request.session['click_counter'] += 1

    # Pass the counter value to the template
    return render(request, 'core/index.html', {'click_counter': request.session['click_counter']})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def services(request):
    return render(request, 'core/services.html')

def blog(request):
    return render(request, 'core/blog.html')

def faq(request):
    return render(request, 'core/faq.html')

# New views
def gallery(request):
    return render(request, 'core/gallery.html')

def team(request):
    return render(request, 'core/team.html')

def pricing(request):
    return render(request, 'core/pricing.html')

def testimonials(request):
    return render(request, 'core/testimonials.html')

def terms_of_service(request):
    return render(request, 'core/terms_of_service.html')
