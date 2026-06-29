class ScenePromptGenerator:

    def generate_prompt(
        self,
        narration
    ):

        base_prompt = """

2D cartoon style.

Elderly defence pensioner Colonel Sharma.

Simple educational animation.

Large readable objects.

Friendly environment.

"""

        return (
            base_prompt
            + narration
        )