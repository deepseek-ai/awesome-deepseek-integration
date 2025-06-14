# DeepSeek Content Moderation Tool

## Overview

This project provides a Python tool for detecting potentially sensitive content in text. It uses a configurable list of keywords and phrases across various categories to analyze input text and flag any matches. This tool is intended as a basic building block for more complex content moderation systems.

## Features

-   **Configurable Categories**: Define your own categories of sensitive content and the keywords/phrases for each.
-   **JSON Configuration**: Sensitive word lists are managed in an easy-to-edit `config.json` file.
-   **Regex-Based Matching**: Uses regular expressions for case-insensitive, whole-word matching.
-   **Returns Matched Categories and Words**: Provides a dictionary of categories that were triggered and the specific words found.
-   **Extensible**: Designed to be integrated into larger applications or workflows.

## Project Structure

```
deepseek_content_moderation/
├── __init__.py
├── config.json
├── moderator.py
├── README.md
└── tests/
    ├── __init__.py
    └── test_moderator.py
```

## Setup and Installation

1.  **Prerequisites**:
    *   Python 3.7+
    *   `pytest` (for running tests): `pip install pytest`

2.  **Configuration (`config.json`)**:
    The `config.json` file stores the categories and lists of sensitive words. You can edit this file to add, remove, or modify categories and their associated terms.

    Example structure:
    ```json
    {
      "Profanity": ["example_swear", "another_bad_word"],
      "HateSpeech": ["example_slur", "derogatory_term"],
      // ... other categories
    }
    ```
    *Initially, the file contains a predefined set of categories and example terms based on common types of sensitive content.*

## Usage

The core functionality is provided by the `Moderator` class in `moderator.py`.

```python
from deepseek_content_moderation.moderator import Moderator

# Initialize the moderator (it will load from config.json by default)
# You can also provide a custom path to a config file:
# moderator = Moderator(config_path="path/to/your/custom_config.json")
moderator = Moderator()

text_to_analyze = "This text contains an example_swear and a derogatory_term."
analysis_result = moderator.analyze_text(text_to_analyze)

if analysis_result:
    print("Sensitive content found:")
    for category, words in analysis_result.items():
        print(f"  Category: {category}, Words: {', '.join(words)}")
else:
    print("No sensitive content detected.")

# Example Output:
# Sensitive content found:
#   Category: Profanity, Words: example_swear
#   Category: HateSpeech, Words: derogatory_term
```

### `analyze_text(text: str) -> dict`

-   **Input**: A string of text to analyze.
-   **Output**: A dictionary where keys are the names of sensitive categories found in the text. The value for each key is a list of unique words/phrases from the input text that matched the sensitive terms in that category. If no sensitive content is found, an empty dictionary is returned.

## Running Tests

To run the unit tests, navigate to the parent directory of `deepseek_content_moderation` and run:

```bash
python -m pytest
```
Or, navigate into the `deepseek_content_moderation` directory and run `pytest`. Ensure `pytest` is installed.

## Disclaimer

This tool provides basic keyword-based detection. It is not a comprehensive solution for content moderation, which often requires more sophisticated NLP techniques, contextual understanding, and human oversight. The initial lists of sensitive words in `config.json` are illustrative and will likely need significant expansion and refinement for any practical application.

## Contributing

Feel free to expand upon this project. Suggestions for improvement include:
- More sophisticated matching algorithms (e.g., Levenshtein distance for typos).
- Support for multiple languages.
- Integration with machine learning models for nuanced detection.
- More granular reporting.
```
