import os

# Paths
icon_dir = "Icons"
readme_head = "readmehead.md"
readme_file = "README.md"

# Helper function to get all icons and their categories
def get_icons(icon_dir):
    icons = {}
    for root, _, files in os.walk(icon_dir):
        category = os.path.basename(root)
        if category not in icons:
            icons[category] = []
        for file in files:
            if file.endswith(".png") and not file.endswith("@4x.png"):
                subcategory, icon_name = file.split("=")
                icons[category].append((subcategory, icon_name))
    return icons

# Generate markdown table from icons
def generate_table(icons):
    table = ""
    for category, icon_list in sorted(icons.items()):
        table += f"### {category}\n\n"
        table += "| Icon | Name |\n|---|---|\n"
        for subcategory, icon_name in sorted(icon_list):
            icon_link = f"./Icons/{category}/{subcategory}={icon_name}"
            icon_display_name = icon_name.replace(".png", "")
            table += f"| ![icon]({icon_link}) | [{icon_display_name}]({icon_link}) |\n"
        table += "\n"
    return table

# Read the readme head
with open(readme_head, "r") as f:
    readme_content = f.read()

# Get icons and generate table
icons = get_icons(icon_dir)
icon_table = generate_table(icons)

# Write the final README.md
with open(readme_file, "w") as f:
    f.write(readme_content + "\n" + icon_table)

print("README.md has been updated successfully!")
