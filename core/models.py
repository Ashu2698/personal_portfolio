from django.db import models

class MetaData(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    logo_charecter = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'

class Hero(models.Model):
    greeting = models.CharField(max_length=255, default="Hello I'm", null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            Hero.objects.exclude(pk=self.pk).update(is_active=False)
        super(Hero, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.greeting} {self.full_name} {self.title}'
    
class About(models.Model):
    about = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            About.objects.exclude(pk=self.pk).update(is_active=False)
        super(About, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.about[:50]}...'
    
class Project(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    demo_url = models.URLField(null=True, blank=True)
    source_url = models.URLField(default='https://github.com/', null=True, blank=True)
    skill = models.ManyToManyField('Skill', blank=True)
    is_active = models.BooleanField(default=True)
    ordering_index = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['ordering_index', '-created']
    
    def __str__(self):
        return f'{self.title}'

class SlkillGroup(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'

class Skill(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    group = models.ForeignKey(SlkillGroup, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'

class Process(models.Model):
    description = models.TextField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.description[:50]}'
    
class Step(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    process = models.ForeignKey(Process, related_name='steps', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'
    
class GetInTouch(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'
    
class InfoItem(models.Model):
    key = models.CharField(max_length=255, null=True, blank=True)
    value = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    get_in_touch = models.ForeignKey(GetInTouch, related_name='info_items', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.key}'
    
class SocialLink(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    icon = models.TextField(null=True, blank=True)
    get_in_touch = models.ForeignKey(GetInTouch, related_name='social_links', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.title}'
    
class Sections(models.Model):
    '''visible or hide section'''
    about_me = models.BooleanField(default=True)
    projects = models.BooleanField(default=True)
    skills = models.BooleanField(default=True)
    process = models.BooleanField(default=True)
    get_in_touch = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sections'
        verbose_name_plural = 'Sections'

class Message(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'