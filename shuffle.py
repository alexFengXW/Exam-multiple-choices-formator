import random

# List of choice contents
contents = ["Putin", "Xi", "Trump", "Biden", "Dr. Pearson"]

# Randomize the order of the contents
random.shuffle(contents)

# Prepare LaTeX code for the tabular environment
latex_code = r"\begin{tabular}{|*{5}{c|}}" + "\n" + r"\hline" + "\n"
latex_code += " & ".join([f"\\tikz \\node[draw, rectangle, inner sep=5pt, align=center, minimum height=10mm] {{{chr(65+i)}: {content}}};"
                          for i, content in enumerate(contents)]) + r" \\" + "\n" + r"\hline" + "\n"
latex_code += r"\end{tabular}"

# Write the LaTeX code to choices.tex
with open("choices.tex", "w") as file:
    file.write(latex_code)
