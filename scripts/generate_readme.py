import os

# Paths
icon_dir = "Icons"
readme_head = "readmehead.md"
readme_file = "README.md"
columns = 6  # Number of columns in the table

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

# Generate a Markdown table with 6 columns for the icons
def generate_markdown_table(icons):
    table = ""
    for category, icon_list in sorted(icons.items()):
        # Skip empty categories
        if not icon_list:
            continue
        
        # Add category name in a grouped cell
        table += f"| {category} ||||||\n"
        table += "|" + ":---:|" * columns + "\n"
        
        row_items = []
        for subcategory, icon_name in sorted(icon_list):
            icon_link = url_encode(f"./Icons/{category}/{subcategory}={icon_name}")
            icon_display_name = icon_name.replace(".png", "")
            icon_img = f"![{icon_display_name}]({icon_link})"
            icon_link_name = f"[{icon_display_name}]({icon_link})"
            row_items.extend([f"{icon_img}<br>{icon_link_name}"])
            
            # When we hit the column limit, write the row
            if len(row_items) == columns:
                table += "| " + " | ".join(row_items) + " |\n"
                row_items = []
        
        # Add remaining items in the row if any
        if row_items:
            # Pad the row with empty cells if it doesn't fill all columns
            while len(row_items) < columns:
                row_items.append(" ")
            table += "| " + " | ".join(row_items) + " |\n"
        
        table += "\n"
    return table

# Read the readme head
with open(readme_head, "r") as f:
    readme_content = f.read()

# Get icons and generate the Markdown table
icons = get_icons(icon_dir)
icon_table = generate_markdown_table(icons)

# Write the final README.md
with open(readme_file, "w") as f:
    f.write(readme_content + "\n## Icons\n\n" + icon_table)

print("README.md has been updated successfully!")
