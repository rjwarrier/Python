import re  # Imports Python's regular expressions (regex) module
# In Python, importing modules allows you to use pre-built functionality without writing code from scratch

# Regex Simple Match – Search
text = "Hello World!"
pattern = r"World"  # Pattern to search for the word "World"
match = re.search(pattern, text)  # Searches for the pattern in the text
# Prints the matched text if found
print(match.group() if match else "No match found")

# Regex extract Email
text = "Contact us at support@example.com or info@example.org"
# Regex pattern to match email addresses
emails = re.findall(r"[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,}", text)
# Explanation of the regex pattern:
# [\w.%+-]+  -> Matches the local part of the email (letters, digits, underscore, dot, %, +, -)
# @           -> Matches the "@" symbol
# [\w.-]+    -> Matches the domain name (letters, digits, dot, hyphen)
# \.         -> Matches the dot before the TLD
# [a-zA-Z]{2,} -> Matches the top-level domain (at least two letters, e.g., com, org)
print(emails)  # Example usage

# Regex Split
text = "apple,banana;cherry|date"
# Matches commas, semicolons, or pipes as delimiters
delimiter_pattern = r"[,;|]"
# Splits the text based on the given delimiters
split_result = re.split(delimiter_pattern, text)
print(split_result)  # Example usage

# Regex Date Split
date1 = "2025-03-27"
date2 = "27/03/2025"
date_pattern = r"[-/.]"  # Matches hyphens, slashes, or dots as date separators
print(re.split(date_pattern, date1))  # Splits date1 based on the delimiters
print(re.split(date_pattern, date2))  # Splits date2 based on the delimiters
