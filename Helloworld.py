import re
pattern= r"(.)\1"

match=re.match(pattern, "abc spam")
if match:
    print("Match 1")
match=re.match(pattern, "?! ?!")
if match:
    print("Match 2")
match=re.match(pattern, "abc cde")
if match:
    print("Match 3")
