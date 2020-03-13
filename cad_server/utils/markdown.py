import markdown2
from pathlib import Path
from django.conf import settings
from premailer import transform
# Markdown 样式
with open(Path(settings.BASE_DIR) / "utils/static/css/default.css", 'r') as css_file:
    CSS_STYLE = css_file.read()


def markdownify(markdown_content: str, inline: bool=False) -> str:
    """markdown转网页
    
    Args:
        markdown_content (str): markdown原始文本
        inline (bool, optional): 是否需要将样式内联. Defaults to False.
    
    Returns:
        str: html
    """
    html_with_style = f'<style>{CSS_STYLE}</style>' + markdown2.markdown(markdown_content, extras=['fenced-code-blocks'])
    return transform(html_with_style) if inline else html_with_style
