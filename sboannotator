import requests

def fetch_sbo_terms():
    url = "https://www.ebi.ac.uk/ols/api/ontologies/sbo/terms"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        terms = data["_embedded"]["terms"]
        for term in terms:
            print(f"ID: {term['obo_id']}, Label: {term['label']}")
    else:
        print(f"Failed to fetch SBO terms. Status code: {response.status_code}")

fetch_sbo_terms()