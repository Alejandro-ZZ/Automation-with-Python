# Regex Examples

Scripts using `re` module to compile regular expression (regex) using Python. The examples includes three methods: 

1. `re.search()` Scan through string looking for the first location where the regular expression pattern produces a match, and return a corresponding match object. Return None if no position in the string matches the pattern; note that this is different from finding a zero-length match at some point in the string.

2. `re.findall()` Return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.

3. `re.sub()` Return the string obtained by replacing the leftmost non-overlapping occurrences of a pattern in string by a replacement text. If the pattern isn’t found, string is returned unchanged. 
