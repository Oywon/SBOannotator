from flask import Flask, render_template, request
from llm_annotation import get_llm_suggestion
import requests
import json

app = Flask(__name__)

def fetch_sbo_terms():
    """
    Fetch SBO terms from the OLS API.
    """
    url = "https://www.ebi.ac.uk/ols/api/ontologies/sbo/terms"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "_embedded" not in data or "terms" not in data["_embedded"]:
            raise ValueError("Invalid response format: 'terms' not found in the response.")

        terms = data["_embedded"]["terms"]
        with open("sbo_terms.json", "w") as file:
            json.dump(terms, file, indent=4)
        return True
    except Exception as e:
        print(f"Error fetching SBO terms: {e}")
        return False

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the reaction description from the form
        reaction_description = request.form.get("reaction_description")

        # Fetch SBO terms
        fetch_success = fetch_sbo_terms()

        # Get LLM suggestions
        llm_suggestion = get_llm_suggestion(reaction_description) if fetch_success else None

        # Render the results
        return render_template("index.html", 
                              reaction_description=reaction_description,
                              fetch_success=fetch_success,
                              llm_suggestion=llm_suggestion)
    
    # Render the form for GET requests
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)