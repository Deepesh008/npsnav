import json
import os

# make sure output folder exists
os.makedirs("output", exist_ok=True)

data = {
    "status": "working",
    "message": "GitHub Actions can write JSON",
    "value": 123
}

with open("output/nps.json", "w") as f:
    json.dump(data, f, indent=2)

print("output/nps.json created")
