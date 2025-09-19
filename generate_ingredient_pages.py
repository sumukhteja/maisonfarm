import csv
import os

# Read CSV data
csv_data = []
with open('ingredients_list_full.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        csv_data.append(row)

# HTML template function
def create_ingredient_page(ingredient_data):
    name = ingredient_data['Ingredient']
    serving_size = ingredient_data['Serving Size']
    calories = ingredient_data['Calories']
    fat = ingredient_data['Fat (g)']
    protein = ingredient_data['Protein (g)']
    net_carbs = ingredient_data['Net Carbs (g)']
    bulletproof_zone = ingredient_data['Bulletproof Zone']
    category = ingredient_data['Category']
    shelf_life = ingredient_data['Shelf Life']
    storage = ingredient_data['Storage']
    price_per_unit = ingredient_data['Price per unit']
    weekly_cost = ingredient_data['Weekly Cost']
    meal_usage = ingredient_data['Meal Usage']
    notes = ingredient_data['Notes']
    
    # Create filename (handle special characters)
    filename = name.lower().replace(' ', '-').replace('(', '').replace(')', '').replace('/', '-') + '.html'
    
    # Determine zone color
    zone_color = '#22C55E' if bulletproof_zone == 'Green' else '#EAB308' if bulletproof_zone == 'Yellow' else '#EF4444'
    
    # Create subtitle based on category
    subtitle_map = {
        'Vegetables': 'Nutrient-dense vegetable for optimal health',
        'Protein': 'High-quality protein for muscle and energy',
        'Fats & Oils': 'Premium healthy fat for optimal performance',
        'Spices': 'Flavorful spice with health benefits',
        'Pantry': 'Essential pantry staple for healthy cooking',
        'Starches': 'Strategic carbohydrate for energy',
        'Condiments': 'Flavorful condiment for healthy meals',
        'Beverage': 'Optimal beverage for performance',
        'Supplement': 'Performance supplement for optimization',
        'Fruit': 'Natural fruit with antioxidant benefits',
        'Herb': 'Fresh herb for flavor and health',
        'Nuts': 'Nutrient-dense nuts for healthy fats'
    }
    subtitle = subtitle_map.get(category, 'Premium ingredient for optimal health')
    
    # Split meal usage into tags
    usage_tags = []
    if meal_usage:
        usage_tags = [usage.strip() for usage in meal_usage.split(',')]
    
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Maison Vitalité</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600&family=Inter:wght@300;400;500&family=Crimson+Text:wght@400;600&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Crimson Text', serif;
            background-color: #FAF8F5;
            color: #2D2D2D;
            line-height: 1.6;
            font-size: 18px;
        }}

        .container {{
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 60px;
            min-height: 100vh;
        }}

        header {{
            text-align: center;
            margin-bottom: 60px;
            border-bottom: 1px solid #D4D4D4;
            padding-bottom: 40px;
        }}

        .logo {{
            font-family: 'Playfair Display', serif;
            font-size: 32px;
            font-weight: 600;
            letter-spacing: 2px;
            margin-bottom: 8px;
            color: #3C2E1F;
        }}

        .breadcrumb {{
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            color: #666;
            text-align: center;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .breadcrumb a {{
            color: #B8860B;
            text-decoration: none;
            transition: color 0.3s ease;
        }}

        .breadcrumb a:hover {{
            color: #4A3728;
        }}

        .ingredient-hero {{
            text-align: center;
            margin-bottom: 60px;
        }}

        .ingredient-title {{
            font-family: 'Playfair Display', serif;
            font-size: 48px;
            font-weight: 400;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }}

        .ingredient-subtitle {{
            font-size: 20px;
            color: #666;
            font-style: italic;
            margin-bottom: 30px;
        }}

        .bulletproof-zone {{
            display: inline-block;
            padding: 8px 20px;
            background: {zone_color};
            color: white;
            border-radius: 20px;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 30px;
        }}

        .ingredient-content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            margin-bottom: 60px;
        }}

        .nutrition-section,
        .details-section {{
            background: rgba(255, 255, 255, 0.6);
            padding: 40px;
            border-radius: 8px;
            border: 1px solid #E8E8E8;
        }}

        .section-title {{
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 400;
            margin-bottom: 25px;
            text-align: center;
            position: relative;
            color: #4A3728;
        }}

        .section-title::after {{
            content: '';
            display: block;
            width: 60px;
            height: 1px;
            background-color: #B8860B;
            margin: 15px auto 0;
        }}

        .nutrition-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-bottom: 20px;
        }}

        .nutrition-item {{
            text-align: center;
            padding: 15px;
            background: rgba(184, 134, 11, 0.05);
            border-radius: 6px;
        }}

        .nutrition-value {{
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            font-weight: 600;
            color: #B8860B;
            display: block;
        }}

        .nutrition-label {{
            font-family: 'Inter', sans-serif;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #666;
            margin-top: 5px;
        }}

        .serving-info {{
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-bottom: 20px;
            font-style: italic;
        }}

        .details-list {{
            list-style: none;
            padding: 0;
        }}

        .details-list li {{
            margin-bottom: 15px;
            padding-left: 25px;
            position: relative;
            font-size: 20px;
        }}

        .details-list li::before {{
            content: '•';
            color: #B8860B;
            font-size: 20px;
            position: absolute;
            left: 0;
            top: -2px;
        }}

        .detail-label {{
            font-weight: 600;
            color: #4A3728;
        }}

        .usage-section {{
            background: rgba(184, 134, 11, 0.05);
            padding: 40px;
            border-radius: 8px;
            border: 1px solid rgba(184, 134, 11, 0.2);
            margin-bottom: 40px;
            text-align: center;
        }}

        .usage-title {{
            font-family: 'Playfair Display', serif;
            font-size: 24px;
            margin-bottom: 20px;
            color: #4A3728;
        }}

        .usage-tags {{
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .usage-tag {{
            background: #4A3728;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 400;
        }}

        .back-button {{
            display: inline-block;
            padding: 15px 30px;
            background: #4A3728;
            color: white;
            text-decoration: none;
            border-radius: 4px;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: background 0.3s ease;
            margin-bottom: 40px;
        }}

        .back-button:hover {{
            background: #B8860B;
        }}

        .notes-section {{
            background: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 8px;
            border-left: 4px solid #B8860B;
            margin-bottom: 40px;
        }}

        .notes-title {{
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            margin-bottom: 15px;
            color: #4A3728;
        }}

        /* Footer Styles */
        footer {{
            margin-top: 80px;
            padding-top: 40px;
            border-top: 1px solid #D4D4D4;
            text-align: center;
        }}

        .footer-content {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            margin-bottom: 40px;
            text-align: left;
        }}

        .footer-section h4 {{
            font-family: 'Playfair Display', serif;
            font-size: 18px;
            font-weight: 400;
            margin-bottom: 20px;
            color: #4A3728;
            letter-spacing: 1px;
        }}

        .footer-section ul {{
            list-style: none;
            padding: 0;
        }}

        .footer-section li {{
            margin-bottom: 12px;
        }}

        .footer-section a {{
            color: #666;
            text-decoration: none;
            font-size: 16px;
            transition: color 0.3s ease;
        }}

        .footer-section a:hover {{
            color: #B8860B;
        }}

        .footer-newsletter {{
            background: rgba(255, 255, 255, 0.6);
            padding: 30px;
            border-radius: 8px;
            border: 1px solid #E8E8E8;
            margin-bottom: 40px;
            text-align: center;
        }}

        .footer-newsletter h4 {{
            font-family: 'Playfair Display', serif;
            font-size: 20px;
            margin-bottom: 15px;
            color: #4A3728;
        }}

        .footer-newsletter p {{
            margin-bottom: 20px;
            color: #666;
            font-size: 16px;
        }}

        .newsletter-form {{
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }}

        .newsletter-input {{
            padding: 12px 20px;
            border: 1px solid #D4D4D4;
            border-radius: 4px;
            background: #FAF8F5;
            font-family: 'Crimson Text', serif;
            font-size: 16px;
            min-width: 250px;
            flex: 1;
            max-width: 300px;
        }}

        .newsletter-input:focus {{
            outline: none;
            border-color: #B8860B;
        }}

        .newsletter-btn {{
            padding: 12px 30px;
            background: #4A3728;
            color: white;
            border: none;
            border-radius: 4px;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            cursor: pointer;
            transition: background 0.3s ease;
        }}

        .newsletter-btn:hover {{
            background: #B8860B;
        }}

        .footer-bottom {{
            padding-top: 30px;
            border-top: 1px solid #E8E8E8;
            color: #666;
            font-size: 14px;
            text-align: center;
        }}

        .footer-bottom p {{
            margin-bottom: 10px;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 30px 30px;
            }}
            
            .ingredient-content {{
                grid-template-columns: 1fr;
                gap: 30px;
            }}
            
            .nutrition-grid {{
                grid-template-columns: 1fr;
            }}
            
            .usage-tags {{
                justify-content: center;
            }}
            
            .footer-content {{
                grid-template-columns: 1fr;
                text-align: center;
                gap: 30px;
            }}
            
            .newsletter-form {{
                flex-direction: column;
                align-items: center;
            }}
            
            .newsletter-input {{
                min-width: 200px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="logo">Maison Vitalité</div>
            <div class="breadcrumb">
                <a href="index.html#ingredients">Ingredients</a> / {name}
            </div>
        </header>

        <div class="ingredient-hero">
            <h1 class="ingredient-title">{name}</h1>
            <p class="ingredient-subtitle">{subtitle}</p>
            <span class="bulletproof-zone">{bulletproof_zone} Zone</span>
        </div>

        <div class="ingredient-content">
            <div class="nutrition-section">
                <h2 class="section-title">Nutrition Facts</h2>
                <div class="serving-info">Per {serving_size}</div>
                
                <div class="nutrition-grid">
                    <div class="nutrition-item">
                        <span class="nutrition-value">{calories}</span>
                        <span class="nutrition-label">Calories</span>
                    </div>
                    <div class="nutrition-item">
                        <span class="nutrition-value">{fat}g</span>
                        <span class="nutrition-label">Fat</span>
                    </div>
                    <div class="nutrition-item">
                        <span class="nutrition-value">{protein}g</span>
                        <span class="nutrition-label">Protein</span>
                    </div>
                    <div class="nutrition-item">
                        <span class="nutrition-value">{net_carbs}g</span>
                        <span class="nutrition-label">Net Carbs</span>
                    </div>
                </div>
            </div>

            <div class="details-section">
                <h2 class="section-title">Details</h2>
                <ul class="details-list">
                    <li><span class="detail-label">Category:</span> {category}</li>
                    <li><span class="detail-label">Shelf Life:</span> {shelf_life}</li>
                    <li><span class="detail-label">Storage:</span> {storage}</li>
                    <li><span class="detail-label">Price per unit:</span> {price_per_unit}</li>
                    <li><span class="detail-label">Weekly Cost:</span> {weekly_cost}</li>
                </ul>
            </div>
        </div>

        {'<div class="usage-section"><h3 class="usage-title">Meal Usage</h3><div class="usage-tags">' + ''.join([f'<span class="usage-tag">{tag}</span>' for tag in usage_tags]) + '</div></div>' if usage_tags else ''}

        {f'<div class="notes-section"><h3 class="notes-title">Pro Tips</h3><p>{notes}</p></div>' if notes else ''}

        <a href="index.html#ingredients" class="back-button">← Back to Ingredients</a>

        <footer>
            <!-- Newsletter Signup -->
            <div class="footer-newsletter">
                <h4>Stay Optimized</h4>
                <p>Get weekly bulletproof nutrition tips and exclusive recipes delivered to your inbox</p>
                <form class="newsletter-form">
                    <input type="email" class="newsletter-input" placeholder="Enter your email address" required>
                    <button type="submit" class="newsletter-btn">Subscribe</button>
                </form>
            </div>

            <!-- Footer Content -->
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Nutrition</h4>
                    <ul>
                        <li><a href="#">Bulletproof Coffee Guide</a></li>
                        <li><a href="#">Intermittent Fasting</a></li>
                        <li><a href="#">Keto Fundamentals</a></li>
                        <li><a href="#">Supplement Stack</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Resources</h4>
                    <ul>
                        <li><a href="#">Meal Planning</a></li>
                        <li><a href="#">Food Quality Guide</a></li>
                        <li><a href="#">Biohacking Tools</a></li>
                        <li><a href="#">Scientific Research</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h4>Support</h4>
                    <ul>
                        <li><a href="#">Contact Us</a></li>
                        <li><a href="#">FAQ</a></li>
                        <li><a href="#">Consultation Booking</a></li>
                        <li><a href="#">Privacy Policy</a></li>
                    </ul>
                </div>
            </div>

            <!-- Footer Bottom -->
            <div class="footer-bottom">
                <p>&copy; 2025 Maison Vitalité. All rights reserved.</p>
                <p>Premium nutrition guidance for optimal human performance</p>
            </div>
        </footer>
    </div>

    <script>
        // Newsletter form submission
        document.querySelector('.newsletter-form').addEventListener('submit', function(e) {{
            e.preventDefault();
            const email = document.querySelector('.newsletter-input').value;
            alert(`Thank you for subscribing with email: ${{email}}`);
            document.querySelector('.newsletter-input').value = '';
        }});
    </script>
</body>
</html>'''
    
    return filename, html_content

# Generate all ingredient pages
for ingredient in csv_data:
    filename, html_content = create_ingredient_page(ingredient)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Created: {filename}")

print(f"\\nGenerated {len(csv_data)} ingredient pages!")