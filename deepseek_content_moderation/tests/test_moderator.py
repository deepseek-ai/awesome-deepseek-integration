import pytest
import json
import os
from deepseek_content_moderation.moderator import Moderator # Adjusted import path

# Helper to create a temporary config file for testing
@pytest.fixture
def temp_config_file(tmp_path):
    config_data = {
        "Profanity": ["badword", "swear"],
        "HateSpeech": ["hateful_term", "slur"],
        "SpecificCategory": ["unique_term_for_test"]
    }
    config_file = tmp_path / "test_config.json"
    with open(config_file, 'w') as f:
        json.dump(config_data, f)
    return str(config_file) # Return path as string

@pytest.fixture
def moderator_instance(temp_config_file):
    # Ensure the moderator uses the temp config by passing the path
    return Moderator(config_path=temp_config_file)

def test_config_loading(moderator_instance):
    assert "Profanity" in moderator_instance.config
    assert "swear" in moderator_instance.config["Profanity"]
    assert "HateSpeech" in moderator_instance.category_regexes
    assert moderator_instance.category_regexes["Profanity"].pattern == r"\b(badword|swear)\b"

def test_analyze_text_no_sensitivities(moderator_instance):
    analysis = moderator_instance.analyze_text("This is a clean sentence.")
    assert analysis == {}

def test_analyze_text_single_category_single_word(moderator_instance):
    analysis = moderator_instance.analyze_text("This sentence contains a badword.")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["badword"]

def test_analyze_text_single_category_multiple_words(moderator_instance):
    analysis = moderator_instance.analyze_text("This sentence has badword and also swear.")
    assert "Profanity" in analysis
    assert sorted(analysis["Profanity"]) == sorted(["badword", "swear"])

def test_analyze_text_multiple_categories(moderator_instance):
    analysis = moderator_instance.analyze_text("A sentence with badword and a hateful_term.")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["badword"]
    assert "HateSpeech" in analysis
    assert analysis["HateSpeech"] == ["hateful_term"]

def test_analyze_text_case_insensitivity(moderator_instance):
    analysis = moderator_instance.analyze_text("This has a BADWORD and HATEFUL_TERM.")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["BADWORD"] # The regex returns the found casing
    assert "HateSpeech" in analysis
    assert analysis["HateSpeech"] == ["HATEFUL_TERM"]

def test_analyze_text_empty_string(moderator_instance):
    analysis = moderator_instance.analyze_text("")
    assert analysis == {}

def test_analyze_text_words_within_words_whole_word_matching(moderator_instance):
    # 'swear' is a keyword, 'swearinger' is not.
    analysis = moderator_instance.analyze_text("He is swearinger but not swear.")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["swear"]

    # Test with a word that is a substring of a sensitive word, but not a whole word match
    analysis_substring = moderator_instance.analyze_text("This is just a test, not a hateful_term at all.")
    assert "HateSpeech" in analysis_substring
    assert analysis_substring["HateSpeech"] == ["hateful_term"]

    analysis_no_match = moderator_instance.analyze_text("This sentence has a term but not the specific unique_term_for_testing.")
    assert "SpecificCategory" not in analysis_no_match


def test_analyze_text_repeated_words(moderator_instance):
    analysis = moderator_instance.analyze_text("This badword is a badword again badword.")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["badword"] # Should only list unique matches

def test_analyze_text_with_punctuation(moderator_instance):
    analysis = moderator_instance.analyze_text("Is this a badword? Yes, badword!")
    assert "Profanity" in analysis
    assert analysis["Profanity"] == ["badword"]

    analysis_slur = moderator_instance.analyze_text("No slur, okay?")
    assert "HateSpeech" in analysis_slur
    assert analysis_slur["HateSpeech"] == ["slur"]

# It's good practice to ensure the test file can be found and run.
# Create a dummy __init__.py in the parent directory of 'tests' if moderator.py is in the root
# and tests are in a subdirectory, to make Python treat 'deepseek-content-moderation' as a package.
# For this subtask, we assume the structure is:
# deepseek-content-moderation/
#   moderator.py
#   config.json
#   tests/
#     test_moderator.py

# To run these tests, navigate to the `deepseek-content-moderation` directory and run `pytest`.
# Ensure `pytest` is installed (`pip install pytest`).
# If `moderator.py` is in the root of `deepseek-content-moderation`, the import
# `from ..moderator import Moderator` is for when tests are run as part of a package.
# If running `pytest` directly from within the `tests` directory, or if `deepseek-content-moderation`
# is not treated as a package, a simple `from moderator import Moderator` might be needed,
# and `sys.path` manipulation or running pytest with `python -m pytest` from the root.

# For this tool, we will ensure the structure supports `from ..moderator import Moderator`.
# This requires an `__init__.py` in the `deepseek-content-moderation` directory.
