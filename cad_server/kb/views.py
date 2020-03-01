from django.forms import model_to_dict
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from kb import models
from kb import serializers

class Problems(APIView):

    permission_class = (IsAdminUser, )

    def get(self, request):

        problems = models.Problem.objects.values()

        return Response(data={"data": problems}, status=status.HTTP_200_OK)
    

    def post(self, request):

        problem_ser = serializers.ProblemSerializer(request.data)
        if problem_ser.is_valid():
            new_problem = problem_ser.save()
            return Response(data={'id': new_problem.id}, status=status.HTTP_201_CREATED)
        else:
            data = {
                "errors": "创建失败"
            }
            return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Problem(APIView):

    permission_class = (IsAdminUser, )
    
    def get(self, request, pk):

        try:
            problem = models.Problem.objects.get(id=pk)
        except models.Problem.DoesNotExist as e:
            return Response(data={"data": {}})

        data = serializers.ProblemSerializer(problem).data
        return Response(data=data, status=status.HTTP_200_OK)


class Solutions(APIView):

    permission_class = (IsAdminUser, )

    pass


class Solution(APIView):

    permission_class = (IsAdminUser, )
    
    pass
