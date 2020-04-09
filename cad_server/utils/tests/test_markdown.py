from django.test import TestCase
from utils.markdown import markdownify

class MarkdownifyTestCase(TestCase):

    def test_markdownify(self):

        self.assertTrue('<code>' in markdownify("```\nimport os\n```"))
