from pathlib import Path
from tempfile import TemporaryDirectory

from fast_zero.schemas import Html


def test_html_content_property():
    # Create a temporary directory and file
    with TemporaryDirectory() as temp_dir:
        temp_file = Path(temp_dir) / "test.html"
        test_content = "<html><body><h1>Test</h1></body></html>"
        temp_file.write_text(test_content)

        # Create Html instance
        html = Html(file=temp_file)

        # Test content property
        assert html.content == test_content
