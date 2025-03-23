import requests
import json

def fetch_sbo_terms():
    url = "https://www.ebi.ac.uk/ols/api/ontologies/sbo/terms"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        terms = data["_embedded"]["terms"]
        
        with open("sbo_terms.json", "w") as file:
            json.dump(terms, file, indent=4)
        print("SBO terms saved to sbo_terms.json")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching SBO terms: {e}")

fetch_sbo_terms()