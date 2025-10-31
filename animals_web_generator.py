import html
import data_fetcher

def serialize_animal(animal):
    name = html.escape(animal.get("name", "No name"))
    ch = animal.get("characteristics", {}) or {}
    diet = html.escape(ch.get("diet", "Unknown"))
    locations = animal.get("locations") or ["Unknown"]
    location = html.escape(locations[0])

    return f"""
    <li class="cards__item">
      <div class="card__title">{name}</div>
      <p class="card__text">
        <strong>Diet:</strong> {diet} <br/>
        <strong>Location:</strong> {location} <br/>
      </p>
    </li>
    """

def generate_html(content_html: str, output_path: str):
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Zootopia</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Arial, sans-serif; padding: 24px; }}
    .cards {{ list-style: none; padding: 0; display: grid; gap: 12px; }}
    .cards__item {{ border: 1px solid #ddd; padding: 12px; border-radius: 10px; }}
    .card__title {{ font-weight: 700; margin-bottom: 6px; }}
    .empty {{ margin-top: 16px; padding: 16px; border: 1px dashed #aaa; border-radius: 10px; background: #fafafa; }}
  </style>
</head>
<body>
  <h1>Zootopia</h1>
  {content_html}
</body>
</html>"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(page)

def main():
    animal_name = input("Enter a name of an animal: ").strip()
    data = data_fetcher.fetch_data(animal_name)

    if not data:
        safe = html.escape(animal_name or "—")
        msg = f'<div class="empty"><h2>The animal "{safe}" doesn\'t exist.</h2><p>Please try another name.</p></div>'
        generate_html(msg, "animals.html")
        print('No results – generated a friendly message to animals.html')
        return

    cards = "".join(serialize_animal(a) for a in data)
    generate_html(f'<ul class="cards">{cards}</ul>', "animals.html")
    print("Website was successfully generated to animals.html")

if __name__ == "__main__":
    main()
