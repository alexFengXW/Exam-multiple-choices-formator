import json
import random

def generate_latex(choices_data):
    latex_content = ""
    for data in choices_data:
        question = data["prompt"]
        choices = data["choices"]
        random.shuffle(choices)  # Shuffle the choices to randomize their order

        # Start the MCQuestion environment
        latex_content += r"\begin{MCQuestion}{" + question + "}\n"

        # Generate choices string
        choices_str = " & ".join([f"{chr(65 + i)}: {choice}" for i, choice in enumerate(choices)])
        latex_content += choices_str + r" \\"  # End of the row

        # End the environment
        latex_content += r"\end{MCQuestion}\n\n"

    return latex_content

# Load questions from a JSON file
with open('questions.json', 'r') as file:
    questions = json.load(file)

# Generate LaTeX code for all questions
latex_code = generate_latex(questions)

# Write to choices.tex
with open("choices.tex", "w") as file:
    file.write(latex_code)
