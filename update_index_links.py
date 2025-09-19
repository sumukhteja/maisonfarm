import re

# Create mapping of ingredient names to filenames
def create_filename(ingredient_name):
    filename = ingredient_name.lower()
    filename = re.sub(r'[^a-z0-9]+', '-', filename)
    filename = filename.strip('-')
    return f"{filename}.html"

# Ingredient name mappings
ingredient_mappings = {
    'Zucchini (Green)': 'zucchini-green.html',
    'Zucchini (Yellow)': 'zucchini-yellow.html',
    'Spinach': 'spinach.html',
    'Organic Coconut Milk': 'organic-coconut-milk.html',
    'Bottle Gourd': 'bottle-gourd.html',
    'Ginger': 'ginger.html',
    'Egg': 'egg.html',
    'Chicken Breast': 'chicken-breast.html',
    'Rice Noodles': 'rice-noodles.html',
    'Oregano': 'oregano.html',
    'Sea Salt': 'sea-salt.html',
    'Ghee': 'ghee.html',
    'Turmeric': 'turmeric.html',
    'Fennel': 'fennel.html',
    'Cinnamon': 'cinnamon.html',
    'Mutton Mince': 'mutton-mince.html',
    'Cauliflower': 'cauliflower.html',
    'Asparagus': 'asparagus.html',
    'Sweet Potato': 'sweet-potato.html',
    'Beans (Green)': 'beans-green.html',
    'Madras Cucumber': 'madras-cucumber.html',
    'Lime': 'lime.html',
    'Coconut Oil': 'coconut-oil.html',
    'Coconut Flakes': 'coconut-flakes.html',
    'Cocoa Butter': 'cocoa-butter.html',
    'Jeera/Cumin': 'jeera-cumin.html',
    'Cloves': 'cloves.html',
    'Avocado Oil': 'avocado-oil.html',
    'Rice flour': 'rice-flour.html',
    'Pink Salt': 'pink-salt.html',
    'Vinegar': 'vinegar.html',
    'Basmati Rice': 'basmati-rice.html',
    'Coffee': 'coffee.html',
    'Fish (fatty)': 'fish-fatty.html',
    'MCT Oil': 'mct-oil.html',
    'Pumpkin': 'pumpkin.html',
    'Radish': 'radish.html',
    'Rice rava': 'rice-rava.html',
    'Electrolytes': 'electrolytes.html',
    'Raspberries': 'raspberries.html',
    'Cranberries': 'cranberries.html',
    'Blackberries': 'blackberries.html',
    'Pineapple': 'pineapple.html',
    'Cilantro': 'cilantro.html',
    'Celery': 'celery.html',
    'Olives': 'olives.html',
    'Brussels Sprouts': 'brussels-sprouts.html',
    'Stevia': 'stevia.html',
    'Pistachios': 'pistachios.html',
    'Macadamia Nuts': 'macadamia-nuts.html',
    'Broccoli': 'broccoli.html',
    'Mutton Curry Cut': 'mutton-curry-cut.html',
    'Blueberries': 'blueberries.html',
    'Meatigo Marinated Chicken (clean)': 'meatigo-marinated-chicken-clean.html'
}

# Read the current index.html
with open('index.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Function to wrap ingredient text with link
def add_link(ingredient_name, filename):
    link_html = f'<a href="{filename}" style="text-decoration: none; color: inherit; transition: color 0.3s ease;" onmouseover="this.style.color=\'#B8860B\'" onmouseout="this.style.color=\'inherit\'">{ingredient_name}</a>'
    return link_html

# Replace each ingredient with linked version
for ingredient_name, filename in ingredient_mappings.items():
    # Find pattern like: <li data-category="...">Ingredient Name</li>
    pattern = f'(<li data-category="[^"]*">){re.escape(ingredient_name)}(</li>)'
    replacement = f'\\g<1>{add_link(ingredient_name, filename)}\\g<2>'
    content = re.sub(pattern, replacement, content)

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Updated index.html with links to all ingredient pages!")