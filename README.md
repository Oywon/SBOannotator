# SBOannotator: Automated SBO Term Annotation Tool

2.Description

SBOannotator is a Python-based tool that automatically assigns Systems Biology Ontology (SBO) terms to entities in SBML models. It dynamically fetches SBO terms from the OLS API and integrates enzymatic data from external sources like BRENDA.
3.Features 
- **Dynamic SBO Term Fetching**: Fetches SBO terms from the OLS API.
- **Enzymatic Data Integration**: Retrieves enzymatic data from BRENDA.
- **LLM-Based Suggestions**: Uses Large Language Models (LLMs) to recommend relevant SBO terms.
- **User-Friendly GUI**: Provides an intuitive interface for users.
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Oywon/SBOannotator.git
   cd SBOannotator
   ```

2. Create a virtual environment:
   ```bash
   python -m venv sboannotator-env
   source sboannotator-env/bin/activate  # On Windows: sboannotator-env\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install requests pandas flask
   ```
## Usage

To fetch and save SBO terms, run:
```bash
python fetch_sbo_terms.py
python fetch_brenda_data.py --ec_number 1.1.1.1


#### **6. Contributing**
- Explain how others can contribute to your project.
```markdown
## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Acknowledgments

- Thanks to the OLS API for providing SBO terms.
- Thanks to BRENDA for enzymatic data.