"""Generate Lab_Action_Guide.pdf from Lab_Action_Guide.md using xhtml2pdf."""

import markdown
from xhtml2pdf import pisa
import io

CSS = """
@page {
    size: A4;
    margin: 18mm 16mm 18mm 16mm;
}

body {
    font-family: Arial, sans-serif;
    font-size: 10pt;
    color: #1a1a1a;
    line-height: 1.45;
}

h1 {
    font-size: 18pt;
    color: #0f4c81;
    border-bottom: 2px solid #0f4c81;
    padding-bottom: 4px;
    margin-top: 12pt;
}

h2 {
    font-size: 14pt;
    color: #0f4c81;
    border-bottom: 1px solid #0f4c81;
    padding-bottom: 2px;
    margin-top: 12pt;
}

h3 {
    font-size: 12pt;
    color: #0f4c81;
    margin-top: 10pt;
}

h4 {
    font-size: 10.5pt;
    color: #1a3a5c;
    margin-top: 8pt;
}

p {
    margin: 4pt 0;
}

ul, ol {
    margin: 4pt 0 4pt 18pt;
    padding: 0;
}

li {
    margin: 2pt 0;
}

pre {
    background-color: #eaf1fb;
    border-left: 3px solid #0f4c81;
    padding: 8pt 10pt;
    font-size: 8.5pt;
    font-family: Courier, monospace;
    margin: 6pt 0;
    white-space: pre-wrap;
    word-wrap: break-word;
}

code {
    font-family: Courier, monospace;
    font-size: 8.5pt;
    background-color: #f0f0f0;
    padding: 1pt 3pt;
}

pre code {
    background-color: transparent;
    padding: 0;
}

blockquote {
    background-color: #fff8e1;
    border-left: 3px solid #f0a500;
    padding: 6pt 10pt;
    margin: 6pt 0;
    font-size: 9.5pt;
}

table {
    border-collapse: collapse;
    width: 100%;
    table-layout: fixed;
    margin: 6pt 0;
    font-size: 9pt;
}

th {
    background-color: #0f4c81;
    color: white;
    padding: 4pt 6pt;
    text-align: left;
    font-size: 9pt;
    word-wrap: break-word;
}

td {
    border: 1px solid #cccccc;
    padding: 4pt 6pt;
    vertical-align: top;
    word-wrap: break-word;
}

tr:nth-child(even) td {
    background-color: #f5f8fd;
}

hr {
    border: none;
    border-top: 1px solid #cccccc;
    margin: 8pt 0;
}
"""

def convert(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    html_body = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "attr_list"]
    )

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""

    with open(pdf_path, "wb") as out:
        result = pisa.CreatePDF(io.StringIO(html), dest=out, encoding="utf-8")

    if result.err:
        print(f"PDF generation errors: {result.err}")
    else:
        print(f"PDF saved to: {pdf_path}")


if __name__ == "__main__":
    convert("Lab_Action_Guide.md", "Lab_Action_Guide.pdf")
