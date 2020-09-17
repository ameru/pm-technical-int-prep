# CASES I 
s.capitalize() -> capitalizes 'hello' to 'Hello'
s.lower() -> lowercases all 'HELLO' to 'hello'
s.swapcase() -> swap cases of all characters in 'Hello' to 'hELLO'
s.title() -> titlecase 'hello world' to 'HELLO WORLD'
s.upper() -> uppercase 'hello' to 'HELLO'

# CASES II
s.casefold() -> casefold s (aggressive lowercasing for caseless matching) 'ßorat' => 'ssorat'
s.islower() -> returns true if s is lowercase
s.istitle() -> returns true if s is titlecased 'Hello World'
s.isupper() -> returns true if s is uppercase

# SEQUENCE OPERATIONS I
s2 in s -> return true if s contains s2
s + s2 -> concat s and s2
len(s) -> finds length of s
min(s) -> smallest character of s
max(s) -> largest character of s

# SEQUENCE OPERATIONS II
s2 not in s -> return true if s does not contain s2
s * integer -> return integer copies of s concatenated 'hello' becomes 'hellohellohello'
s[index] -> character at index of s
s[i:j:k] -> slice of s from i to j with step k
s.count(s2) -> count of s2 in s

# WHITESPACE I
s.center(width) -> center s with blank padding of width 'hi' to ' hi '
s.isspace() -> return true if s only contains whitespace characters
s.ljust(width) -> left justify s with total size of width 'hello' becomes 'hello '
s.rjust(width) -> right justify s with total size of width 'hello' becomes ' hello'
s.strip() -> remove leading and trailing whitespace from ' hello ' becomes 'hello'

# WHITESPACE II
s.center(width, pad) -> Center s with padding pad of width # 'hi' => 'padpadhipadpad'
s.expandtabs(integer) -> Replace all tabs with spaces of tabsize integer # 'hello\tworld' => 'hello world'
s.lstrip() -> Remove leading whitespace from s # ' hello ' => 'hello '
s.rstrip() -> Remove trailing whitespace from s # ' hello ' => ' hello'
s.zfill(width) -> Left fill s with ASCII '0' digits with total length width # '42' => '00042'

# FIND/REPLACE
s.index(s2,i,j) -> index of first occurence of s2 in s after index i and before index j
s.find(s2) -> find and return lowest index of s2 in s
s.index(s2) -> return lowest index of s2 in s (but raise ValueError if not found)
s.replace(s2,s3) -> replace s2 with s3 
s.replace(s2,s3,count) -> replace s2 with s3 in s at most count times
s.rfind(s2) -> return highest index of s2 in s
s.rindex(s2) -> return highest index of s2 in s (raise ValueError if not found)

# INSPECTION I 
s.endswith(s2) -> returns true if s ends with s2
s.isalnum() -> return true if s is alphanumeric
s.isalpha() -> return true if s is alphabetic
s.isdecimal() -> return true if s is decimal
s.isnumeric() -> return true if s is numeric
s.startswith(s2) -> return true if s starts with s2

# INSPECTION II
s[i:j] -> Slice of s from i to j
s.endswith((s1,s2,s3)) -> Return true if s ends with any of string tuple s1, s2, and s3
s.isdigit() -> Return true if s is digit
s.isidentifier() -> Return true if s is a valid identifier
s.isprintable() -> Return true is s is printable

# SPLITTING
s.join('123') -> return s joined by iterable '123' 'hello' becomes '1hello2hello3'
s.partition(sep) -> Partition string at sep and return 3-tuple with part before, the sep itself, and part after # 'hello' => ('he', 'l', 'lo')
s.rpartition(sep) -> Partition string at last occurrence of sep, return 3-tuple with part before, the sep, and part after # 'hello' => ('hel', 'l', 'o')
s.rsplit(sep, maxsplit) -> Return list of s split by sep with rightmost maxsplits performed
s.split(sep, mazsplit) -> Return list of s split by sep with leftmost maxsplits performed
s.splitlines() -> Return a list of lines in s # 'hello\nworld' => ['hello', 'world']
