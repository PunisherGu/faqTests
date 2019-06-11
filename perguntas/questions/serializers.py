from rest_framework import serializers
from questions.models import Question
from django.contrib.auth.models import User

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text', 'answer', 'ordem')
        owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.answer = validated_data.get('answer', instance.answer)
        instance.ordem = validated_data.get('ordem', instance.ordem)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'questions')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='question-highlight', format='html')

    class Meta:
        model = Question
        fields = ('url', 'id', 'highlight', 'owner',
                  'text', 'answer', 'ordem')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    questions = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'questions')
