"""
REGULAR EXPRESSIONS (re module)
===============================

Key Points:
- Pattern matching with regular expressions
- re module functions: search, match, findall, sub
- Common regex patterns and metacharacters
- Groups and capturing
- Flags for case-insensitive, multiline matching
- Practical applications: validation, extraction, replacement
"""

import re

print("=== BASIC REGEX OPERATIONS ===")

# Sample text for demonstrations
text = "Contact us at support@example.com or sales@company.org. Phone: 123-456-7890"

# re.search() - find first match
email_pattern = r'\S+@\S+\.\S+'
match = re.search(email_pattern, text)
if match:
    print(f"First email found: {match.group()}")
    print(f"Position: {match.start()}-{match.end()}")

# re.findall() - find all matches
all_emails = re.findall(email_pattern, text)
print(f"All emails: {all_emails}")

# re.match() - match from beginning of string
text2 = "support@example.com is our main contact"
match_from_start = re.match(email_pattern, text2)
if match_from_start:
    print(f"Email at start: {match_from_start.group()}")

print("\n=== COMMON REGEX PATTERNS ===")

patterns_examples = [
    (r'\d+', "123 and 456", "Digits"),
    (r'\w+', "hello_world 123", "Word characters"),
    (r'\s+', "hello   world", "Whitespace"),
    (r'[aeiou]', "hello world", "Vowels"),
    (r'[A-Z]', "Hello World", "Uppercase letters"),
    (r'[0-9]{3}', "Call 123-456-7890", "Exactly 3 digits"),
    (r'\b\w{4}\b', "This is a test", "4-letter words"),
    (r'^Hello', "Hello world", "Starts with 'Hello'"),
    (r'world$', "Hello world", "Ends with 'world'"),
]

for pattern, test_text, description in patterns_examples:
    matches = re.findall(pattern, test_text)
    print(f"{description:20} | Pattern: {pattern:10} | Text: '{test_text}' | Matches: {matches}")

print("\n=== METACHARACTERS ===")

metacharacters_info = """
Common regex metacharacters:

. (dot)     - Matches any character except newline
^ (caret)   - Matches start of string
$ (dollar)  - Matches end of string
* (asterisk)- Matches 0 or more repetitions
+ (plus)    - Matches 1 or more repetitions
? (question)- Matches 0 or 1 repetition
{n}         - Matches exactly n repetitions
{n,m}       - Matches n to m repetitions
[] (brackets)- Character class
| (pipe)    - OR operator
() (parens) - Grouping
\\ (backslash)- Escape character

Character classes:
\\d - Digits [0-9]
\\w - Word characters [a-zA-Z0-9_]
\\s - Whitespace [ \\t\\n\\r\\f\\v]
\\D - Non-digits
\\W - Non-word characters
\\S - Non-whitespace
"""

print(metacharacters_info)

print("\n=== PHONE NUMBER VALIDATION ===")

def validate_phone(phone):
    """Validate phone number formats"""
    patterns = [
        r'^\d{3}-\d{3}-\d{4}$',           # 123-456-7890
        r'^\(\d{3}\) \d{3}-\d{4}$',       # (123) 456-7890
        r'^\d{10}$',                      # 1234567890
        r'^\+1-\d{3}-\d{3}-\d{4}$',       # +1-123-456-7890
    ]
    
    for pattern in patterns:
        if re.match(pattern, phone):
            return True
    return False

# Test phone numbers
test_phones = [
    "123-456-7890",
    "(123) 456-7890", 
    "1234567890",
    "+1-123-456-7890",
    "123-45-6789",  # Invalid
    "abc-def-ghij"  # Invalid
]

print("Phone number validation:")
for phone in test_phones:
    is_valid = validate_phone(phone)
    print(f"  {phone:15} - {'Valid' if is_valid else 'Invalid'}")

print("\n=== EMAIL VALIDATION ===")

def validate_email(email):
    """Validate email address"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Test emails
test_emails = [
    "user@example.com",
    "test.email+tag@domain.co.uk",
    "invalid.email",
    "@domain.com",
    "user@",
    "valid_email@test-domain.org"
]

print("Email validation:")
for email in test_emails:
    is_valid = validate_email(email)
    print(f"  {email:30} - {'Valid' if is_valid else 'Invalid'}")

print("\n=== GROUPS AND CAPTURING ===")

# Extract parts of a date
date_text = "Today is 2024-03-15 and tomorrow is 2024-03-16"
date_pattern = r'(\d{4})-(\d{2})-(\d{2})'

# Find all dates with groups
dates = re.findall(date_pattern, date_text)
print("Extracted date parts:")
for date in dates:
    year, month, day = date
    print(f"  Year: {year}, Month: {month}, Day: {day}")

# Using named groups
named_pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
match = re.search(named_pattern, date_text)
if match:
    print(f"Named groups: {match.groupdict()}")

print("\n=== TEXT SUBSTITUTION ===")

# Replace patterns with new text
original_text = "Call us at 123-456-7890 or email support@example.com"

# Replace phone numbers
phone_replaced = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE]', original_text)
print(f"Phone replaced: {phone_replaced}")

# Replace emails
email_replaced = re.sub(r'\S+@\S+\.\S+', '[EMAIL]', phone_replaced)
print(f"Email replaced: {email_replaced}")

# Using groups in replacement
text_with_names = "Hello John Smith and Jane Doe"
name_pattern = r'(\w+) (\w+)'
formatted = re.sub(name_pattern, r'\2, \1', text_with_names)
print(f"Name format changed: {formatted}")

print("\n=== FLAGS ===")

# Case-insensitive matching
text_mixed_case = "Hello WORLD hello world"
pattern = r'hello'

# Without flag
matches_normal = re.findall(pattern, text_mixed_case)
print(f"Normal search: {matches_normal}")

# With IGNORECASE flag
matches_ignore_case = re.findall(pattern, text_mixed_case, re.IGNORECASE)
print(f"Case-insensitive: {matches_ignore_case}")

# Multiline flag
multiline_text = """First line
Second line with PATTERN
Third line"""

# Without MULTILINE flag
pattern_start = r'^Second'
matches_no_multiline = re.findall(pattern_start, multiline_text)
print(f"Without MULTILINE: {matches_no_multiline}")

# With MULTILINE flag
matches_multiline = re.findall(pattern_start, multiline_text, re.MULTILINE)
print(f"With MULTILINE: {matches_multiline}")

print("\n=== PRACTICAL APPLICATIONS ===")

def extract_urls(text):
    """Extract URLs from text"""
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    return re.findall(url_pattern, text)

def extract_hashtags(text):
    """Extract hashtags from social media text"""
    hashtag_pattern = r'#\w+'
    return re.findall(hashtag_pattern, text)

def clean_html_tags(text):
    """Remove HTML tags from text"""
    html_pattern = r'<[^>]+>'
    return re.sub(html_pattern, '', text)

def extract_numbers(text):
    """Extract all numbers (including decimals)"""
    number_pattern = r'-?\d+\.?\d*'
    return re.findall(number_pattern, text)

# Test practical functions
sample_text = """
Visit our website at https://example.com or https://test.org
Follow us on social media! #python #programming #coding
<p>This is <b>HTML</b> content</p>
Prices: $19.99, $25.50, and $100
Temperature: -5.5°C to 25.3°C
"""

print("URL extraction:")
urls = extract_urls(sample_text)
for url in urls:
    print(f"  {url}")

print("\nHashtag extraction:")
hashtags = extract_hashtags(sample_text)
print(f"  {hashtags}")

print("\nHTML tag removal:")
clean_text = clean_html_tags("<p>This is <b>HTML</b> content</p>")
print(f"  '{clean_text}'")

print("\nNumber extraction:")
numbers = extract_numbers(sample_text)
print(f"  {numbers}")

print("\n=== COMPILED PATTERNS ===")

# Compile patterns for better performance when used multiple times
email_compiled = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
phone_compiled = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')

test_text = "Contact: john@example.com, phone: 123-456-7890"

# Use compiled patterns
email_match = email_compiled.search(test_text)
phone_match = phone_compiled.search(test_text)

print("Using compiled patterns:")
if email_match:
    print(f"  Email: {email_match.group()}")
if phone_match:
    print(f"  Phone: {phone_match.group()}")

print("\n=== DATA VALIDATION FUNCTIONS ===")

def validate_password(password):
    """Validate password strength"""
    # At least 8 characters, one uppercase, one lowercase, one digit
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

def validate_credit_card(card_number):
    """Basic credit card format validation"""
    # Remove spaces and dashes
    cleaned = re.sub(r'[\s-]', '', card_number)
    # Check if 13-19 digits
    pattern = r'^\d{13,19}$'
    return re.match(pattern, cleaned) is not None

def extract_ip_addresses(text):
    """Extract IP addresses from text"""
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ip_pattern, text)

# Test validation functions
passwords = ["weak", "StrongPass123", "short", "NoDigits", "NOLOWER123"]
print("Password validation:")
for pwd in passwords:
    is_valid = validate_password(pwd)
    print(f"  {pwd:15} - {'Valid' if is_valid else 'Invalid'}")

cards = ["1234-5678-9012-3456", "1234 5678 9012 3456", "123456789", "abcd-efgh-ijkl-mnop"]
print("\nCredit card validation:")
for card in cards:
    is_valid = validate_credit_card(card)
    print(f"  {card:20} - {'Valid' if is_valid else 'Invalid'}")

ip_text = "Server IPs: 192.168.1.1, 10.0.0.1, and 256.300.400.500"
ips = extract_ip_addresses(ip_text)
print(f"\nExtracted IPs: {ips}")

print("\n=== EXAM FOCUS: KEY PATTERNS ===")

exam_patterns = """
Essential regex patterns for exams:

1. Email: r'\\S+@\\S+\\.\\S+'
2. Phone: r'\\d{3}-\\d{3}-\\d{4}'
3. Digits: r'\\d+' 
4. Words: r'\\w+'
5. Whitespace: r'\\s+'
6. Start of line: r'^pattern'
7. End of line: r'pattern$'
8. Optional: r'colou?r' (matches 'color' or 'colour')
9. One or more: r'\\d+' (one or more digits)
10. Zero or more: r'\\d*' (zero or more digits)

Common functions:
- re.search(pattern, text): find first match
- re.findall(pattern, text): find all matches
- re.match(pattern, text): match from start
- re.sub(pattern, replacement, text): substitute
- re.compile(pattern): compile for reuse

Flags:
- re.IGNORECASE: case-insensitive
- re.MULTILINE: ^ and $ match line boundaries
- re.DOTALL: . matches newlines too
"""

print(exam_patterns)

# Quick exam example
exam_text = "Contact: user@example.com and admin@test.org"
exam_pattern = r'\\S+@\\S+\\.\\S+'
exam_matches = re.findall(exam_pattern, exam_text)
print(f"\\nExam example - emails found: {exam_matches}")

print("\\nRegular expressions mastered! ✓")