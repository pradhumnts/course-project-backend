from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic = models.CharField(max_length=100)
    topicAttribute = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topicAttribute

class System(models.Model):
    system = models.CharField(max_length=100)
    topic = models.ManyToManyField(Topic, related_name='system')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.system

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    system = models.ManyToManyField(System, related_name='subject', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Section(models.Model):
    section = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.section

class Course(models.Model):
    courseName = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sections = models.ManyToManyField(Section, related_name='course')
    subjects = models.ManyToManyField(Subject, related_name='course')
    systems = models.ManyToManyField(System, related_name='course')
    topics = models.ManyToManyField(Topic, related_name='course', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.courseName

class Answer(models.Model):
    choice = models.CharField(max_length=255)
    answerHeader = models.CharField(max_length=200, blank=True, null=True)
    choiceNumber = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.choice

class Question(models.Model):
    questionText = models.TextField(max_length=5000)
    explanationText = models.TextField(max_length=15000)
    questionHeader = models.CharField(max_length=100, blank=True, null=True)
    section = models.ForeignKey(Section, related_name='question', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='question', on_delete=models.CASCADE)
    system = models.ForeignKey(System, related_name='question', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='question', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='question', on_delete=models.CASCADE)
    isActive = models.BooleanField(default=True)
    hint = models.TextField(max_length=500, blank=True, null=True)
    highlights = models.TextField(max_length=1000, blank=True, null=True)
    correctAnswer = models.IntegerField()
    answerChoiceList = models.ManyToManyField(Answer, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk) + " - " + str(self.created_at) + " - " + str(self.updated_at)

class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(null=True, blank=True)
    subscriptionStartDate = models.DateTimeField(null=True, blank=True)
    subscriptionEndDate = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + " - " + self.course.courseName

class UserQuestion(models.Model):
    QUESTION_STATUS_CHOICES = [
        ('Incorrect', 'Incorrect'),
        ('Used', 'Used'),
        ('Correct', 'Correct'),
        ('Marked', 'Marked'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    status = models.CharField(max_length=40, choices=QUESTION_STATUS_CHOICES, default="Used")
    attemptTime = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username + ' ' + str(self.question.id)