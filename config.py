# config.py
# This is a dictionary where keys are investor names and values are lists of example prompts for that investor.
investor_specific_prompts = {
    "Tilman Fertitta": {
        "objectives": [
            "Expand the brand's reach by transforming three historical landmarks into luxury shopping destinations while preserving their heritage."
        ],
        "tasks": [
            "Select historical sites, conduct preservation studies, and liaise with local authorities for development permissions."
        ]
    },
    "InvestorB": {
        "objectives": ["Objective 1 for InvestorB", "Objective 2 for InvestorB", "Objective 3 for InvestorB"],
        "tasks": ["Task 1 for InvestorB", "Task 2 for InvestorB", "Task 3 for InvestorB"]
    },
    # Add more investors and their specific tasks as needed
}
# Default investor - change this before sending to a specific investor.
DEFAULT_INVESTOR = "Rick Caruso"