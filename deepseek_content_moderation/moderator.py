import json
import re

class Moderator:
    def __init__(self, config_path="config.json"):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self._compile_regexes()

    def _compile_regexes(self):
        self.category_regexes = {}
        for category, words in self.config.items():
            # Escape special characters in words and join with | for OR logic
            # Use  for whole word matching
            escaped_words = [re.escape(word) for word in words]
            regex_pattern = r"\b(" + "|".join(escaped_words) + r")\b"
            # Compile with IGNORECASE
            self.category_regexes[category] = re.compile(regex_pattern, re.IGNORECASE)

    def analyze_text(self, text: str) -> dict:
        found_sensitivities = {}
        if not text:
            return found_sensitivities

        for category, regex_pattern in self.category_regexes.items():
            matches = regex_pattern.findall(text)
            if matches:
                # Store unique matches
                found_sensitivities[category] = sorted(list(set(matches)))

        return found_sensitivities

if __name__ == '__main__':
    # Example Usage (optional, for basic testing)
    moderator = Moderator()

    test_text_1 = "This is a test with swearword1 and another bad term like HATEspeech_slur1."
    analysis_1 = moderator.analyze_text(test_text_1)
    print(f"Analysis for '{test_text_1}': {analysis_1}")

    test_text_2 = "This text is clean and should pass."
    analysis_2 = moderator.analyze_text(test_text_2)
    print(f"Analysis for '{test_text_2}': {analysis_2}")

    test_text_3 = "Another example with MEdiCaL_MiSiNfoRmAtiOn1 and suggestive_innuendo1."
    analysis_3 = moderator.analyze_text(test_text_3)
    print(f"Analysis for '{test_text_3}': {analysis_3}")

    test_text_4 = "Testing PII like personal_name_example here."
    analysis_4 = moderator.analyze_text(test_text_4)
    print(f"Analysis for '{test_text_4}': {analysis_4}")

    test_text_5 = "This has drug_use_term1 and also drug_use_term1 again."
    analysis_5 = moderator.analyze_text(test_text_5)
    print(f"Analysis for '{test_text_5}': {analysis_5}")
