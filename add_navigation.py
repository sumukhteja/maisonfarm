import os
import re

# Navigation HTML to add
navigation_html = '''
        <nav>
            <ul class="nav-links">
                <li><a href="index.html#ingredients" class="nav-link">Ingredients</a></li>
                <li><a href="index.html#recipes" class="nav-link">Recipes</a></li>
                <li><a href="index.html#tips" class="nav-link">Tips</a></li>
            </ul>
        </nav>
'''

# CSS styles to add for navigation
navigation_css = '''
        /* Navigation Styles */
        nav {
            margin-bottom: 40px;
        }

        .nav-links {
            display: flex;
            justify-content: center;
            gap: 40px;
            list-style: none;
            padding: 0;
            margin: 0;
        }

        .nav-links a {
            text-decoration: none;
            color: #4A3728;
            font-family: 'Inter', sans-serif;
            font-size: 16px;
            font-weight: 500;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: color 0.3s ease;
        }

        .nav-links a:hover,
        .nav-links a.active {
            color: #B8860B;
        }
'''

# Mobile CSS update
mobile_css_addition = '''
            .nav-links {
                flex-direction: row;
                gap: 20px;
                justify-content: center;
            }
'''

# Get list of all HTML files (ingredient pages)
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and f != 'index1.html']

for filename in html_files:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Add navigation CSS to the existing styles
        # Find the closing </style> tag and add before it
        css_pattern = r'(\s+</style>)'
        content = re.sub(css_pattern, navigation_css + r'\1', content)
        
        # Add mobile navigation CSS to existing mobile styles
        # Find the mobile media query section and add navigation styles
        mobile_pattern = r'(@media \(max-width: 768px\) \{[^}]*\})'
        
        def add_nav_to_mobile(match):
            mobile_block = match.group(1)
            # Insert navigation CSS before the closing }
            mobile_block = mobile_block[:-1] + mobile_css_addition + '        }'
            return mobile_block
        
        content = re.sub(mobile_pattern, add_nav_to_mobile, content, flags=re.DOTALL)
        
        # Add navigation HTML after the </header> tag
        header_pattern = r'(</header>)'
        content = re.sub(header_pattern, r'\1' + navigation_html, content)
        
        # Write the updated content back
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        
        print(f"Updated {filename}")
    
    except Exception as e:
        print(f"Error updating {filename}: {e}")

print(f"\nUpdated navigation for {len(html_files)} ingredient pages!")