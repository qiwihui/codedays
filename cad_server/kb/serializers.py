from rest_framework import serializers
from kb.models import Problem, Solution, Tag, Category


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ['content', 'level']


class SolutionsSerializer(serializers.Serializer):

    solutions = serializers.ListField(
        child = SolutionSerializer()
    )

class ProblemSerializer(serializers.ModelSerializer):

    solutions = SolutionSerializer(many=True)
    category = CategorySerializer()
    tags = TagSerializer(many=True)

    updated_time = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Problem
        fields = '__all__'

    def create(self, validated_data):
        solutions_data = validated_data.pop('solutions')
        problem = Problem.objects.create(**validated_data)
        for solution_data in solutions_data:
            Solution.objects.create(album=problem, **solution_data)
        return problem
