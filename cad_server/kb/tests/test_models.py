from django.test import TestCase
from kb.models import Tag, Category, Problem, Solution


def create_tag(key, name):
    return Tag.objects.create(key=key, name=name)


def create_category(name):
    return Category.objects.create(name=name)


def create_problem(title, content, category, tag):
    return Problem.objects.create(
            title=title, content=content, category=category, tag=tag)


def create_solution(content, problem):
    return Solution.objects.create(content=content, problem=problem)


class TagTestCase(TestCase):

    def test_tag_creation(self):
        w = create_tag('list', "List")
        self.assertTrue(isinstance(w, Tag))
        self.assertEqual(w.__str__(), 'list - List')


class CategoryTestCase(TestCase):

    def test_category_creation(self):
        w = create_category("算法")
        self.assertTrue(isinstance(w, Category))
        self.assertEqual(w.__str__(), '算法')


class ProblemTestCase(TestCase):

    def test_problem_creation(self):
        tag = create_tag('list', "List")
        category = create_category("算法")

        problem = create_problem(
            title="问题1", content="问题主体", category=category, tag=tag)
        self.assertTrue(isinstance(problem, Problem))
        self.assertEqual(problem.__str__(), f'{problem.order}. {problem.title}')


class SolutionTestCase(TestCase):

    def test_solution_creation(self):
        tag = create_tag('list', "List")
        category = create_category("算法")

        problem = create_problem(
            title="问题1", content="问题主体", category=category, tag=tag)

        solution = create_solution("答案", problem=problem)
        self.assertTrue(isinstance(solution, Solution))
        self.assertEqual(solution.__str__(), f'{solution.problem} {solution.id}')
