from django.contrib.auth.models import User
from django.db import models


class License(models.Model):
    short_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.short_name


class ProgrammingLanguage(models.Model):
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.language


class ProjectProgrammingLanguage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.project} | {self.language} | {self.percentage}%"


class HostingPlatform(models.Model):
    hosting_platform = models.CharField(max_length=100)

    def __str__(self):
        return self.hosting_platform


class ProjectHostingPlatform(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    hosting_platform = models.ForeignKey(HostingPlatform, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return f"{self.project} | {self.hosting_platform}"


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    licenses = models.ManyToManyField(License)
    programming_languages = models.ManyToManyField(ProgrammingLanguage, through="ProjectProgrammingLanguage", related_name="projects")
    hosting_platform = models.ManyToManyField(HostingPlatform, through="ProjectHostingPlatform", related_name="projects")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} | {self.name}"
