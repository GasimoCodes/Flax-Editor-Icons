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

# Convert the file path to a URL-friendly format (handles spaces and special characters)
def url_encode(path):
    return path.replace(" ", "%20")

# Generate a grid layout using HTML for the icons
def generate_grid(icons):
    grid = ""
    for category, icon_list in sorted(icons.items()):
        grid += f"### {category}\n\n"
        grid += '<div style="display: flex; flex-wrap: wrap;">\n'
        for subcategory, icon_name in sorted(icon_list):
            icon_link = url_encode(f"./Icons/{category}/{subcategory}={icon_name}")
            icon_display_name = icon_name.replace(".png", "")
            grid += f'''
<div style="width: 120px; text-align: center; margin: 10px;">
    <img src="{icon_link}" alt="{icon_display_name}" width="64" height="64"><br>
    <a href="{icon_link}">{icon_display_name}</a>
</div>
'''
        grid += '</div>\n\n'
    return grid

# Read the readme head
with open(readme_head, "r") as f:
    readme_content = f.read()

# Get icons and generate grid
icons = get_icons(icon_dir)
icon_grid = generate_grid(icons)

# Write the final README.md
with open(readme_file, "w") as f:
    f.write(readme_content + "\n" + icon_grid)

print("README.md has been updated successfully!")
