import data_fetcher

def serialize_animal(animal):
    name = animal.get("name", "No name")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    locations = animal.get("locations", ["Unknown"])
    location = locations[0]

    return f"""
    <li class="cards__item">
        <div class="card__title">{name}</div>
        <p class="card__text">
            <strong>Diet:</strong> {diet} <br/>
            <strong>Location:</strong> {location} <br/>
        </p>
    </li>
    """

def generate_html(cards_html, output_path):
    template = f"""
<!DOCTYPE html>
<html>
<head>
<title>Zootopia</title>
</head>
<body>
<h1>Zootopia</h1>
<ul class="cards">
{cards_html}
</ul>
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template)

def main():
    animal_name = input("Enter a name of an animal: ")

    data = data_fetcher.fetch_data(animal_name)

    if not data:
        cards_html = f'<h2>The animal "{animal_name}" does not exist.</h2>'
    else:
        cards_html = "".join(serialize_animal(a) for a in data)

    output_path = "animals.html"
    generate_html(cards_html, output_path)
    print("Website was successfully generated to the file animals.html.")

if __name__ == "__main__":
    main()
