from rest_framework import serializers
from kb.models import Problem, Solution


class SolutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solution
        fields = ['content', 'level']


class ProblemSerializer(serializers.ModelSerializer):

    solutions = SolutionSerializer(many=True)

    class Meta:
        model = Problem
        fields = ['content', 'level','solutions']

    def create(self, validated_data):
        solutions_data = validated_data.pop('solutions')
        problem = Problem.objects.create(**validated_data)
        for solution_data in solutions_data:
            Solution.objects.create(album=problem, **solution_data)
        return problem
