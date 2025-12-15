
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Azam Saidov")
    title = models.CharField(max_length=200, default="Full Stack Django Developer")
    description = models.TextField(default="10+ month experience in Django, PostgreSQL")
    bio = models.TextField(default="I'm a passionate Full Stack Developer specializing in Django.")
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200, default="Bukhara, Uzbekistan")
    email = models.EmailField(default="azamsaidov077@gmail.com")
    phone = models.CharField(max_length=20, default="+998 93 620 62 22")
    freelance_status = models.CharField(max_length=20, default="Available", choices=[
        ('Available', 'Available'),
        ('Busy', 'Busy'),
        ('Not Available', 'Not Available')
    ])
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cvs/', blank=True, null=True)
    projects_completed = models.IntegerField(default=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills', blank=True, null=True)
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

class Service(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='services', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fas fa-code")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.TextField()
    features = models.TextField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # Validator olib tashlandi
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Experience(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiences', blank=True, null=True)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='educations', blank=True, null=True)
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class SocialLink(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='social_links', blank=True, null=True)
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=50)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.platform

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"