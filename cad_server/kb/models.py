from django.db import models

class Category(models.Model):
    """分类
    """

    name = models.CharField(max_length=64)

    class Meta:
        app_label = "kb"
        db_table = "category"

    def __str__(self):
        return self.name


class Tag(models.Model):
    """标签
    """
    key = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    
    class Meta:
        app_label = "kb"
        db_table = "tag"

    def __str__(self):
        return f'{self.key} - {self.name}'


class Problem(models.Model):
    """问题
    """
    # title
    title = models.CharField(max_length=128)
    # 内容
    content = models.TextField()
    # 更新时间
    updated_time = models.DateTimeField(null=False, blank=True, auto_now=True)
    # 问题难度, 1,2,3
    difficulty = models.PositiveSmallIntegerField(default=1)
    # category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # tag
    tags = models.ManyToManyField(Tag, related_name='tags')

    class Meta:
        app_label = "kb"
        db_table = "problem"

    def __str__(self):
        return self.title


class Solution(models.Model):
    """答案
    """
    # 内容
    content = models.TextField()
    # 对应问题
    problem = models.ForeignKey(Problem, related_name='solutions', on_delete=models.CASCADE)
    # 答案等级
    level = models.PositiveSmallIntegerField(default=0)

    class Meta:
        app_label = "kb"
        db_table = "solution"
    
    def __str__(self):
        return f'{self.problem} - {self.id}'
