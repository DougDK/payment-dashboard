import json
import random
import uuid
from datetime import datetime, timedelta

how_many_transactions = 10000

# Sample customer and product data to vary the dataset
customers = [
    {"name": "John Doe", "email": "johndoe@example.com", "age": 28},
    {"name": "Jane Smith", "email": "janesmith@example.com", "age": 35},
    {"name": "Emily Clark", "email": "emilyclark@example.com", "age": 40},
    {"name": "Michael Brown", "email": "michaelbrown@example.com", "age": 45},
    {"name": "Chris Evans", "email": "chrisevans@example.com", "age": 33},
    {"name": "Robert C Martin", "email": "unclebob@example.com", "age": 60},
    {"name": "Robert Downey Jr.", "email": "ironman@example.com", "age": 60},
    {"name": "Sarah Johnson", "email": "sarahjohnson@example.com", "age": 27},
    {"name": "David Lee", "email": "davidlee@example.com", "age": 38},
    {"name": "Laura Wilson", "email": "laurawilson@example.com", "age": 32},
    {"name": "Daniel Miller", "email": "danielmiller@example.com", "age": 41},
    {"name": "Jessica Taylor", "email": "jessicataylor@example.com", "age": 29},
    {"name": "Matthew Anderson", "email": "matthewanderson@example.com", "age": 36},
    {"name": "Karen Thomas", "email": "karenthomas@example.com", "age": 44},
    {"name": "Joshua Martinez", "email": "joshuamartinez@example.com", "age": 31},
    {"name": "Nancy Hernandez", "email": "nancyhernandez@example.com", "age": 37},
    {"name": "Kevin Jackson", "email": "kevinjackson@example.com", "age": 39},
    {"name": "Linda White", "email": "lindawhite@example.com", "age": 42},
    {"name": "Steven Harris", "email": "stevenharris@example.com", "age": 34},
    {"name": "Barbara Lewis", "email": "barbaralewis@example.com", "age": 46},
    {"name": "Thomas Robinson", "email": "thomasrobinson@example.com", "age": 29},
    {"name": "Susan Walker", "email": "susanwalker@example.com", "age": 38},
    {"name": "Paul Young", "email": "paulyoung@example.com", "age": 35},
    {"name": "Karen Hall", "email": "karenhall@example.com", "age": 41},
    {"name": "Mark Allen", "email": "markallen@example.com", "age": 33},
    {"name": "Michelle King", "email": "michelleking@example.com", "age": 36},
    {"name": "Charles Wright", "email": "charleswright@example.com", "age": 47},
    {"name": "Patricia Scott", "email": "patriciascott@example.com", "age": 39},
    {"name": "Christopher Green", "email": "christophergreen@example.com", "age": 32},
    {"name": "Ashley Baker", "email": "ashleybaker@example.com", "age": 28},
    {"name": "Andrew Adams", "email": "andrewadams@example.com", "age": 43},
    {"name": "Rebecca Nelson", "email": "rebeccanelson@example.com", "age": 30},
    {"name": "Justin Hill", "email": "justinhill@example.com", "age": 37},
    {"name": "Laura Ramirez", "email": "lauraramirez@example.com", "age": 34},
    {"name": "Brian Campbell", "email": "briancampbell@example.com", "age": 40},
    {"name": "Amy Mitchell", "email": "amymitchell@example.com", "age": 31},
    {"name": "Edward Roberts", "email": "edwardroberts@example.com", "age": 45},
    {"name": "Samantha Carter", "email": "samanthacarter@example.com", "age": 29},
    {"name": "Jason Phillips", "email": "jasonphillips@example.com", "age": 38},
    {"name": "Angela Turner", "email": "angelaturner@example.com", "age": 36},
    {"name": "Brandon Parker", "email": "brandonparker@example.com", "age": 33},
    {"name": "Melissa Evans", "email": "melissaevans@example.com", "age": 42},
    {"name": "Aaron Edwards", "email": "aaronedwards@example.com", "age": 39},
    {"name": "Stephanie Collins", "email": "stephaniecollins@example.com", "age": 35},
    {"name": "Jonathan Stewart", "email": "jonathanstewart@example.com", "age": 41},
    {"name": "Megan Sanchez", "email": "megansanchez@example.com", "age": 27},
    {"name": "Gregory Morris", "email": "gregorymorris@example.com", "age": 46},
    {"name": "Rachel Rogers", "email": "rachelrogers@example.com", "age": 30},
    {"name": "Patrick Reed", "email": "patrickreed@example.com", "age": 44},
    {"name": "Emma Cook", "email": "emmacook@example.com", "age": 33},
    {"name": "Scott Morgan", "email": "scottmorgan@example.com", "age": 37},
    {"name": "Victoria Bell", "email": "victoriabell@example.com", "age": 32},
    {"name": "Benjamin Murphy", "email": "benjaminmurphy@example.com", "age": 29},
    {"name": "Kimberly Bailey", "email": "kimberlybailey@example.com", "age": 40},
    {"name": "Jeremy Rivera", "email": "jeremyrivera@example.com", "age": 35},
    {"name": "Olivia Cooper", "email": "oliviacooper@example.com", "age": 31},
    {"name": "Alexander Richardson", "email": "alexanderrichardson@example.com", "age": 43},
    {"name": "Laura Cox", "email": "lauracox@example.com", "age": 28},
    {"name": "Dylan Howard", "email": "dylanhoward@example.com", "age": 36},
    {"name": "Maria Ward", "email": "mariaward@example.com", "age": 39},
    {"name": "Ethan Peterson", "email": "ethanpeterson@example.com", "age": 34},
    {"name": "Victoria Gray", "email": "victoriagray@example.com", "age": 38},
    {"name": "Nathan James", "email": "nathanjames@example.com", "age": 42},
    {"name": "Amber Watson", "email": "amberwatson@example.com", "age": 29},
    {"name": "Kyle Brooks", "email": "kylebrooks@example.com", "age": 31},
    {"name": "Danielle Kelly", "email": "daniellekelly@example.com", "age": 27},
    {"name": "Sean Sanders", "email": "seansanders@example.com", "age": 45},
    {"name": "Hannah Price", "email": "hannahprice@example.com", "age": 33},
    {"name": "Zachary Bennett", "email": "zacharybennett@example.com", "age": 30},
    {"name": "Lauren Wood", "email": "laurenwood@example.com", "age": 36},
    {"name": "Aaron Barnes", "email": "aaronbarnes@example.com", "age": 40},
    {"name": "Michelle Ross", "email": "michelleross@example.com", "age": 34},
    {"name": "Tyler Henderson", "email": "tylerhenderson@example.com", "age": 38},
    {"name": "Heather Coleman", "email": "heathercoleman@example.com", "age": 41},
    {"name": "Justin Jenkins", "email": "justinjenkins@example.com", "age": 29},
    {"name": "Katherine Perry", "email": "katherineperry@example.com", "age": 32},
    {"name": "Brandon Powell", "email": "brandonpowell@example.com", "age": 37},
    {"name": "Brittany Long", "email": "brittanylong@example.com", "age": 28},
    {"name": "Christian Patterson", "email": "christianpatterson@example.com", "age": 35},
    {"name": "Crystal Hughes", "email": "crystalhughes@example.com", "age": 39},
    {"name": "Shawn Flores", "email": "shawnflores@example.com", "age": 43},
    {"name": "Courtney Foster", "email": "courtneyfoster@example.com", "age": 31},
    {"name": "Cameron Butler", "email": "cameronbutler@example.com", "age": 44},
    {"name": "Erin Simmons", "email": "erinsimmons@example.com", "age": 30},
    {"name": "Austin Gonzales", "email": "austingonzales@example.com", "age": 42},
    {"name": "Julie Bryant", "email": "juliebryant@example.com", "age": 33},
    {"name": "Gabriel Alexander", "email": "gabrielalexander@example.com", "age": 29},
    {"name": "Victoria Russell", "email": "victoriarussell@example.com", "age": 36},
    {"name": "Evan Griffin", "email": "evangriffin@example.com", "age": 40},
    {"name": "Allison Diaz", "email": "allisondiaz@example.com", "age": 28},
    {"name": "Adam Hayes", "email": "adamhayes@example.com", "age": 37},
    {"name": "Kelsey Myers", "email": "kelseymyers@example.com", "age": 34},
    {"name": "Ian Ford", "email": "ianford@example.com", "age": 41},
    {"name": "Alexis Hamilton", "email": "alexishamilton@example.com", "age": 30},
    {"name": "Eric Graham", "email": "ericgraham@example.com", "age": 38},
    {"name": "Megan Sullivan", "email": "megansullivan@example.com", "age": 35},
    {"name": "Brandon Wallace", "email": "brandonwallace@example.com", "age": 32},
    {"name": "Natalie West", "email": "nataliewest@example.com", "age": 27},
    {"name": "Trevor Cole", "email": "trevorcole@example.com", "age": 39},
    {"name": "Kaitlyn Ortiz", "email": "kaitlynortiz@example.com", "age": 31},
    {"name": "Logan Bryant", "email": "loganbryant@example.com", "age": 29},
    {"name": "Rachel Jenkins", "email": "racheljenkins@example.com", "age": 36},
    {"name": "Dylan Stevens", "email": "dylanstevens@example.com", "age": 40},
    {"name": "Olivia Murray", "email": "oliviamurray@example.com", "age": 28},
    {"name": "Jordan Ford", "email": "jordanford@example.com", "age": 35},
    {"name": "Molly Stone", "email": "mollystone@example.com", "age": 33},
    {"name": "Chase Reynolds", "email": "chasereynolds@example.com", "age": 37},
    {"name": "Alyssa Nichols", "email": "alyssanichols@example.com", "age": 30},
    {"name": "Bryan Fisher", "email": "bryanfisher@example.com", "age": 42},
    {"name": "Katherine Ellis", "email": "katherineellis@example.com", "age": 34},
    {"name": "Garrett Lawson", "email": "garrettlawson@example.com", "age": 38},
    {"name": "Sydney Price", "email": "sydneyprice@example.com", "age": 29},
    {"name": "Ethan Reyes", "email": "ethanreyes@example.com", "age": 31},
    {"name": "Taylor Perry", "email": "taylorperry@example.com", "age": 27},
    {"name": "Ryan Bennett", "email": "ryanbennett@example.com", "age": 36},
    {"name": "Jasmine Barnes", "email": "jasminebarnes@example.com", "age": 32},
    {"name": "Brandon Jenkins", "email": "brandonjenkins@example.com", "age": 39},
    {"name": "Katie Powell", "email": "katiepowell@example.com", "age": 28},
    {"name": "Zachary Patterson", "email": "zacharypatterson@example.com", "age": 37},
    {"name": "Sierra Cox", "email": "sierracox@example.com", "age": 33},
    {"name": "Connor Brooks", "email": "connorbrooks@example.com", "age": 35},
    {"name": "Brooke Kelly", "email": "brookekelly@example.com", "age": 30},
    {"name": "Blake Sanders", "email": "blakesanders@example.com", "age": 40},
]

products = [
    {"product_id": 101, "product_name": "Wireless Mouse", "category": "Electronics", "price": 29.99},
    {"product_id": 102, "product_name": "Keyboard", "category": "Electronics", "price": 49.99},
    {"product_id": 103, "product_name": "Smartphone", "category": "Electronics", "price": 599.99},
    {"product_id": 104, "product_name": "Laptop", "category": "Electronics", "price": 999.99},
    {"product_id": 105, "product_name": "Headphones", "category": "Electronics", "price": 199.99},
    {"product_id": 106, "product_name": "Bluetooth Speaker", "category": "Electronics", "price": 89.99},
    {"product_id": 107, "product_name": "Smartwatch", "category": "Electronics", "price": 249.99},
    {"product_id": 108, "product_name": "Tablet", "category": "Electronics", "price": 399.99},
    {"product_id": 109, "product_name": "Gaming Console", "category": "Electronics", "price": 499.99},
    {"product_id": 110, "product_name": "4K TV", "category": "Electronics", "price": 1199.99},
    {"product_id": 111, "product_name": "Digital Camera", "category": "Electronics", "price": 549.99},
    {"product_id": 112, "product_name": "External Hard Drive", "category": "Electronics", "price": 129.99},
    {"product_id": 113, "product_name": "Wireless Charger", "category": "Electronics", "price": 39.99},
    {"product_id": 114, "product_name": "Gaming Headset", "category": "Electronics", "price": 79.99},
    {"product_id": 115, "product_name": "Smart Thermostat", "category": "Home Appliances", "price": 229.99},
    {"product_id": 116, "product_name": "Robot Vacuum", "category": "Home Appliances", "price": 399.99},
    {"product_id": 117, "product_name": "Air Fryer", "category": "Home Appliances", "price": 149.99},
    {"product_id": 118, "product_name": "Electric Kettle", "category": "Home Appliances", "price": 59.99},
    {"product_id": 119, "product_name": "Blender", "category": "Home Appliances", "price": 89.99},
    {"product_id": 120, "product_name": "Coffee Maker", "category": "Home Appliances", "price": 129.99},
    {"product_id": 121, "product_name": "Smart Light Bulbs", "category": "Home Appliances", "price": 49.99},
    {"product_id": 122, "product_name": "Microwave Oven", "category": "Home Appliances", "price": 179.99},
    {"product_id": 123, "product_name": "Electric Toothbrush", "category": "Health & Personal Care", "price": 99.99},
    {"product_id": 124, "product_name": "Hair Dryer", "category": "Health & Personal Care", "price": 79.99},
    {"product_id": 125, "product_name": "Fitness Tracker", "category": "Health & Personal Care", "price": 149.99},
    {"product_id": 126, "product_name": "Electric Shaver", "category": "Health & Personal Care", "price": 119.99},
    {"product_id": 127, "product_name": "Smart Scale", "category": "Health & Personal Care", "price": 59.99},
    {"product_id": 128, "product_name": "Air Purifier", "category": "Home Appliances", "price": 299.99},
    {"product_id": 129, "product_name": "Dehumidifier", "category": "Home Appliances", "price": 249.99},
    {"product_id": 130, "product_name": "Instant Camera", "category": "Electronics", "price": 69.99},
    {"product_id": 131, "product_name": "VR Headset", "category": "Electronics", "price": 399.99},
    {"product_id": 132, "product_name": "Drone", "category": "Electronics", "price": 799.99},
    {"product_id": 133, "product_name": "Smart Doorbell", "category": "Home Appliances", "price": 149.99},
    {"product_id": 134, "product_name": "Security Camera", "category": "Home Appliances", "price": 199.99},
    {"product_id": 135, "product_name": "Laptop Stand", "category": "Electronics", "price": 39.99},
    {"product_id": 136, "product_name": "Portable Projector", "category": "Electronics", "price": 299.99},
    {"product_id": 137, "product_name": "Electric Scooter", "category": "Outdoors", "price": 599.99},
    {"product_id": 138, "product_name": "Smart Water Bottle", "category": "Health & Personal Care", "price": 49.99},
    {"product_id": 139, "product_name": "Portable Power Bank", "category": "Electronics", "price": 79.99},
    {"product_id": 140, "product_name": "Noise-Cancelling Earbuds", "category": "Electronics", "price": 159.99},
    {"product_id": 141, "product_name": "Smart Alarm Clock", "category": "Home Appliances", "price": 89.99},
    {"product_id": 142, "product_name": "Electric Bike", "category": "Outdoors", "price": 1299.99},
    {"product_id": 143, "product_name": "Action Camera", "category": "Electronics", "price": 299.99},
    {"product_id": 144, "product_name": "Smart Mirror", "category": "Home Appliances", "price": 349.99},
    {"product_id": 145, "product_name": "Massage Gun", "category": "Health & Personal Care", "price": 199.99},
    {"product_id": 146, "product_name": "Electric Grill", "category": "Home Appliances", "price": 149.99},
    {"product_id": 147, "product_name": "UV Sanitizer", "category": "Health & Personal Care", "price": 69.99},
    {"product_id": 148, "product_name": "Cordless Vacuum", "category": "Home Appliances", "price": 299.99},
    {"product_id": 149, "product_name": "Solar Charger", "category": "Outdoors", "price": 99.99},
    {"product_id": 150, "product_name": "Electric Skateboard", "category": "Outdoors", "price": 499.99}
]


payment_methods = ["Credit Card", "PayPal", "Bank Transfer", "Pix", "Cash"]
statuses = ["Completed", "Pending", "Failed"]

def generate_transaction():
    customer = random.choice(customers)
    num_products = random.randint(1, 3)  # Choose 1 to 3 products
    selected_products = random.sample(products, num_products)
    
    transaction = {
        "transaction_id": str(uuid.uuid4()),  # Unique transaction ID
        "customer_name": customer["name"],
        "email": customer["email"],
        "age": customer["age"],
        "purchase_date": (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "products": [{
            "product_id": p["product_id"],
            "product_name": p["product_name"],
            "category": p["category"],
            "quantity": random.randint(1, 5),  # Random quantity between 1-5
            "price": p["price"]
        } for p in selected_products],
        "payment_method": random.choice(payment_methods),
        "currency": "USD",
        "status": random.choice(statuses)
    }
    
    total_amount = 0
    for product in transaction["products"]:
        total_amount += product["price"] * product["quantity"]
    transaction["total_amount"] = round(total_amount, 2)

    return transaction

# Generate transactions
transactions = [generate_transaction() for _ in range(how_many_transactions)]

# Output the result as JSON
with open('transactions.json', 'w') as f:
    json.dump(transactions, f, indent=4)

print(f"Generated {how_many_transactions} transactions in transactions.json")
