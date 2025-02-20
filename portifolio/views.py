from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    my_projects = [
        {
            "name": "Attendance System",
            "description": "Automated QR-based student attendance system using Django.",
            "github_url": "https://github.com/vincentiano23/auto-generate-QR-attendance.git"
        },
        {
            "name": "AI Chatbot",
            "description": "A chatbot built with AI capabilities to assist users in inquiries.",
            "github_url": "https://github.com/yourusername/ai-chatbot"
        },
        {
            "name": "POS System",
            "description": "Point of Sale (POS) system with inventory management and payments.",
            "github_url": "https://github.com/vincentiano23/POS-.git"
        }
    ]
    
    return render(request, 'projects.html', {'projects': my_projects})

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to contact page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})