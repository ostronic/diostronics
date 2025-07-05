# Regenerate index.html with working background and functional 'Get in Touch' link to a survey form

# Define the placeholder survey/contact form link
contact_link = "https://example.com/your-survey-form"  # Replace with actual survey form URL

# Updated HTML content
html_content_v2 = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Archi</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: sans-serif;
            background-color: #000;
        }}
        .background {{
            background: url('images/subheader-1.jpg') no-repeat center center fixed;
            background-size: cover;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }}
        .logo {{
            max-width: 200px;
            margin-bottom: 10px;
        }}
        .cta h1 {{
            font-size: 3em;
            margin-bottom: 20px;
        }}
        .cta a {{
            display: inline-block;
            padding: 12px 30px;
            background-color: #fff;
            color: #000;
            text-decoration: none;
            font-weight: bold;
            border-radius: 4px;
            transition: background 0.3s;
        }}
        .cta a:hover {{
            background-color: #ddd;
        }}
    </style>
</head>
<body>
    <div class="background">
        <img src="images/logo.png" alt="Logo" class="logo">
        <div class="cta">
            <h1>Beautiful Architecture & Interior Designs</h1>
            <a href="{contact_link}" target="_blank" rel="noopener noreferrer">Get in Touch</a>
        </div>
    </div>
</body>
</html>
"""

# Save the updated HTML
index_html_v2_path = "index.html"
with open(index_html_v2_path, "w", encoding="utf-8") as f:
    f.write(html_content_v2)

index_html_v2_path
