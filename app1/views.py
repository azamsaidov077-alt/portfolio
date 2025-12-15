# app1/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Profile, ContactMessage, Skill, Service, Project, Experience, Education, SocialLink
from .forms import ContactForm
import os


# app1/views.py - DEBUG bilan
def home(request):
    """
    Home page view - faqat database'dagi ma'lumotlar
    """
    try:
        from .models import Profile, Skill, Service, Project, Experience, Education, SocialLink

        # 1. Profile
        profile = Profile.objects.first()

        if not profile:
            profile = Profile.objects.create(
                name="Your Name",
                title="Your Title",
                bio="Add your bio here",
                email="your@email.com",
                phone="",
                location=""
            )

        skills = Skill.objects.filter(profile=profile).order_by('order')
        projects = Project.objects.filter(profile=profile).order_by('-created_at')
        services = Service.objects.filter(profile=profile).order_by('order')
        experiences = Experience.objects.filter(profile=profile).order_by('-start_date')
        educations = Education.objects.filter(profile=profile)
        social_links = SocialLink.objects.filter(profile=profile).order_by('order')

    except Exception as e:
        print(f"Error: {e}")
        profile = None
        skills = []
        projects = []
        services = []
        experiences = []
        educations = []
        social_links = []

    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
        'services': services,
        'experiences': experiences,
        'educations': educations,
        'social_links': social_links,
    }

    return render(request, 'app1/index.html', context)


from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # 1. Database ga saqlash
        contact_msg = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )


        try:

            send_mail(
                subject=f"📨 Portfolio Contact: {subject}",
                message=f"""
                👤 Ism: {name}
                📧 Email: {email}
                📋 Mavzu: {subject}
                💬 Xabar: {message}

                🕐 Vaqt: {contact_msg.created_at}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['azamsaidov077@gmail.com'],
                fail_silently=False,
            )


            send_mail(
                subject=f"✅ Xabaringiz qabul qilindi: {subject}",
                message=f"""
                Hurmatli {name},

                Xabaringiz muvaffaqiyatli qabul qilindi.
                Tez orada siz bilan aloqaga chiqamiz.

                Hurmat bilan,
                {settings.DEFAULT_FROM_EMAIL}
                """,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
                fail_silently=True,
            )

            messages.success(request, '✅ Xabaringiz yuborildi! Email orqali ham xabar oldiz.')

        except Exception as e:
            messages.warning(request, f'⚠️ Xabar saqlandi, lekin email yuborishda xatolik: {str(e)}')


        return redirect('/#contact')


    return redirect('home')


def download_portfolio(request):
    """
    Download CV/Portfolio
    """
    profile = Profile.objects.first()

    if profile and profile.cv_file:
        try:
            file_path = profile.cv_file.path
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    response = HttpResponse(f.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{profile.name}_CV.pdf"'
                    return response
        except Exception as e:
            print(f"Error downloading CV: {e}")

    messages.warning(request, 'CV file is not available yet. Please contact me for a copy.')
    return redirect('home')


def admin_login(request):
    """
    Redirect to Django admin login
    """
    return redirect('/admin/')


from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from .models import Profile


def cv_page(request):
    """CV uchun alohida sahifa"""
    profile = Profile.objects.first()

    if not profile:
        raise Http404("Profile topilmadi")

    context = {
        'profile': profile,
        'skills': profile.skill_set.all() if hasattr(profile, 'skill_set') else [],
        'experiences': profile.experience_set.all() if hasattr(profile, 'experience_set') else [],
        'educations': profile.education_set.all() if hasattr(profile, 'education_set') else [],
        'projects': profile.project_set.all() if hasattr(profile, 'project_set') else [],
    }

    return render(request, 'app1/cv.html', context)


from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
import os


def download_portfolio_pdf(request):
    """
    Butun portfolio sahifasini PDF qilib yuklab olish
    """
    try:
        # Barcha ma'lumotlarni olish (home view'dagidek)
        from .models import Profile, Skill, Service, Project, Experience, Education, SocialLink

        profile = Profile.objects.first()

        if not profile:
            profile = Profile.objects.create(
                name="Azam Saidov",
                title="Full Stack Django Developer",
                description="10+ month experience in Django, PostgreSQL",
                bio="I'm a passionate Full Stack Developer specializing in Django.",
                email="azamsaidov077@gmail.com",
                phone="+998 93 620 62 22",
                address="Bukhara, Uzbekistan"
            )

        skills = Skill.objects.filter(profile=profile).order_by('order')
        services = Service.objects.filter(profile=profile).order_by('order')
        projects = Project.objects.filter(profile=profile).order_by('-created_at')
        experiences = Experience.objects.filter(profile=profile).order_by('-start_date')
        educations = Education.objects.filter(profile=profile)
        social_links = SocialLink.objects.filter(profile=profile).order_by('order')


        context = {
            'profile': profile,
            'skills': skills,
            'projects': projects,
            'services': services,
            'experiences': experiences,
            'educations': educations,
            'social_links': social_links,
            'is_pdf': True,  # PDF uchun flag
        }

        # HTML template'ni render qilish
        html_string = render_to_string('app1/portfolio_pdf.html', context)

        # WeasyPrint bilan PDF yaratish
        html = HTML(string=html_string)

        # PDF yaratish
        pdf_file = html.write_pdf()

        # Response yaratish
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{profile.name}_Portfolio.pdf"'

        return response

    except Exception as e:

        return HttpResponse(f"Xatolik: {str(e)}. WeasyPrint o'rnatish kerak: pip install weasyprint")