from django.test import TestCase
from utils.markdown import markdownify

class MarkdownifyTestCase(TestCase):

    def test_markdownify(self):

        self.assertEqual('<code>' in markdownify("```\nimport os\n```"), True)
