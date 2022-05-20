from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

class TopicSerializer(serializers.ModelSerializer):
    questions_length = serializers.SerializerMethodField("length_field")

    def length_field(self, obj):
        return Question.objects.filter(topic=obj).count()

    class Meta:
        model = Topic
        fields = ["id", "topic", "topicAttribute", "questions_length", "created_at"]
        depth = 4


class SystemSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True, many=True)
    questions_length = serializers.SerializerMethodField("length_field")

    def length_field(self, obj):
        return Question.objects.filter(system=obj).count()

    class Meta:
        model = System
        fields = ["id", "system", "topic", "questions_length", "created_at"]
        depth = 4


class SubjectSerializer(serializers.ModelSerializer):
    system = SystemSerializer(read_only=True, many=True)
    questions_length = serializers.SerializerMethodField("length_field")

    def length_field(self, obj):
        return Question.objects.filter(subject=obj).count()

    class Meta:
        model = Subject
        fields = ["id", "subject", "system", "questions_length", "created_at"]
        # depth = 4


class SectionSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True, many=True)
    questions_length = serializers.SerializerMethodField("length_field")

    def length_field(self, obj):
        return Question.objects.filter(section=obj).count()

    class Meta:
        model = Section
        fields = ["id", "section", "subject", "questions_length", "created_at"]
        depth = 4


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = "__all__"
        depth = 1


class CourseSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ["id", "courseName", "description",
                  "sections", "created_at", "updated_at"]
        depth = 4

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["password"]

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
    
        if password is not None:
            user.set_password(password)
            
        user.save()
        return user

    class Meta:
        model = User
        exclude = ["password"]

class UserCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCourse
        exclude = ["user"]
        depth = 1