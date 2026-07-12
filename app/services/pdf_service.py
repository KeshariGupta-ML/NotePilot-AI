import markdown

from io import BytesIO
from datetime import datetime

from bs4 import BeautifulSoup

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Preformatted,
    Table,
    TableStyle
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.pagesizes import A4

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.enums import TA_CENTER



# -----------------------------
# Register Unicode Font
# -----------------------------

try:

    pdfmetrics.registerFont(
        TTFont(
            "NotoSans",
            "fonts/NotoSans-Regular.ttf"
        )
    )

    pdfmetrics.registerFont(
        TTFont(
            "NotoSans-Bold",
            "fonts/NotoSans-Bold.ttf"
        )
    )

    FONT = "NotoSans"

    BOLD_FONT = "NotoSans-Bold"


except Exception:

    FONT = "Helvetica"

    BOLD_FONT = "Helvetica-Bold"



# -----------------------------
# PDF Generator
# -----------------------------

def create_pdf(markdown_text: str):


    buffer = BytesIO()


    doc = SimpleDocTemplate(

        buffer,

        pagesize=A4,

        rightMargin=50,

        leftMargin=50,

        topMargin=60,

        bottomMargin=50

    )



    styles = getSampleStyleSheet()



    # Custom styles

    title_style = ParagraphStyle(

        "CustomTitle",

        parent=styles["Title"],

        fontName=BOLD_FONT,

        fontSize=22,

        alignment=TA_CENTER,

        spaceAfter=20

    )


    h2_style = ParagraphStyle(

        "CustomHeading2",

        parent=styles["Heading2"],

        fontName=BOLD_FONT,

        fontSize=16,

        spaceBefore=18,

        spaceAfter=10

    )


    h3_style = ParagraphStyle(

        "CustomHeading3",

        parent=styles["Heading3"],

        fontName=BOLD_FONT,

        fontSize=13,

        spaceBefore=12,

        spaceAfter=8

    )


    body_style = ParagraphStyle(

        "CustomBody",

        parent=styles["BodyText"],

        fontName=FONT,

        fontSize=11,

        leading=16,

        spaceAfter=8

    )


    bullet_style = ParagraphStyle(

        "Bullet",

        parent=body_style,

        leftIndent=15,

        bulletIndent=0

    )


    code_style = ParagraphStyle(

        "Code",

        fontName="Courier",

        fontSize=9,

        leading=12

    )



    # Convert Markdown -> HTML

    html = markdown.markdown(

        markdown_text,

        extensions=[

            "fenced_code",

            "tables",

            "nl2br"

        ]

    )


    soup = BeautifulSoup(

        html,

        "html.parser"

    )


    story = []



    # -----------------------------
    # Parse HTML
    # -----------------------------

    for element in soup.children:


        if element.name is None:

            continue



        # H1

        if element.name == "h1":

            story.append(

                Paragraph(

                    str(element),

                    title_style

                )

            )



        # H2

        elif element.name == "h2":

            story.append(

                Paragraph(

                    str(element),

                    h2_style

                )

            )



        # H3

        elif element.name == "h3":

            story.append(

                Paragraph(

                    str(element),

                    h3_style

                )

            )



        # Paragraph

        elif element.name == "p":

            story.append(

                Paragraph(

                    str(element),

                    body_style

                )

            )



        # Bullet list

        elif element.name == "ul":


            for li in element.find_all(
                "li",
                recursive=False
            ):

                story.append(

                    Paragraph(

                        "• " + li.decode_contents(),

                        bullet_style

                    )

                )



        # Number list

        elif element.name == "ol":


            count = 1


            for li in element.find_all(
                "li",
                recursive=False
            ):


                story.append(

                    Paragraph(

                        f"{count}. {li.decode_contents()}",

                        body_style

                    )

                )


                count += 1



        # Code block

        elif element.name == "pre":


            code = element.get_text()


            story.append(

                Preformatted(

                    code,

                    code_style

                )

            )



        # Table

        elif element.name == "table":


            data = []


            for row in element.find_all("tr"):


                cols = []


                for cell in row.find_all(
                    ["th","td"]
                ):

                    cols.append(

                        Paragraph(

                            cell.decode_contents(),

                            body_style

                        )

                    )


                data.append(cols)



            table = Table(
                data,
                repeatRows=1
            )


            table.setStyle(

                TableStyle(

                    [

                        (
                            "GRID",
                            (0,0),
                            (-1,-1),
                            0.5,
                            None
                        ),

                        (
                            "VALIGN",
                            (0,0),
                            (-1,-1),
                            "TOP"
                        )

                    ]

                )

            )


            story.append(table)



        story.append(
            Spacer(1,12)
        )



    # -----------------------------
    # Footer
    # -----------------------------

    def add_page_number(canvas, doc):

        canvas.saveState()


        canvas.setFont(
            FONT,
            9
        )


        canvas.drawCentredString(

            A4[0] / 2,

            25,

            f"AI Notes Maker | Page {doc.page}"

        )


        canvas.restoreState()



    doc.build(

        story,

        onFirstPage=add_page_number,

        onLaterPages=add_page_number

    )


    buffer.seek(0)


    return buffer.getvalue()