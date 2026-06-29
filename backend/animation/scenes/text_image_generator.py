from PIL import Image, ImageDraw, ImageFont
import textwrap
import os


class TextImageGenerator:

    def __init__(
        self,
        width=1280,
        height=720,
        font_size=42
    ):

        self.width = width
        self.height = height
        self.font_size = font_size

        font_path = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "fonts",
            "NotoSansDevanagari-Regular.ttf"
        )

        font_path = os.path.normpath(font_path)

        self.font = ImageFont.truetype(
            font_path,
            self.font_size
        )


    def _wrap_text(
        self,
        text,
        max_chars=28
    ):

        wrapper = textwrap.TextWrapper(
            width=max_chars
        )

        return "\n".join(
            wrapper.wrap(text)
        )


    def generate_step_image(
        self,
        hindi_text: str,
        step_number: int,
        output_path: str
    ):


        img = Image.new(
            "RGB",
            (self.width,self.height),
            (240,245,255)
        )

        draw = ImageDraw.Draw(img)


        # room background
        draw.rectangle(
            [(0,500),(1280,720)],
            fill=(220,220,220)
        )


        # character head
        draw.ellipse(
            [(180,170),(300,290)],
            fill=(255,220,177)
        )


        # body
        draw.rectangle(
            [(210,290),(270,450)],
            fill=(40,90,180)
        )


        # phone
        draw.rounded_rectangle(
            [(350,250),(450,420)],
            radius=15,
            fill=(50,50,50)
        )

        draw.rectangle(
            [(370,280),(430,380)],
            fill=(180,230,255)
        )


        # title
        title = f"Step {step_number}"

        draw.text(
            (40,40),
            title,
            font=self.font,
            fill=(0,0,0)
        )


        wrapped_text = self._wrap_text(
            hindi_text
        )


        draw.text(
            (600,250),
            wrapped_text,
            font=self.font,
            fill=(20,20,20)
        )


        os.makedirs(
            os.path.dirname(output_path),
            exist_ok=True
        )

        img.save(output_path)

        return output_path