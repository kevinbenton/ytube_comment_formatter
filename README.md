Youtube Comment Formatter
=======================

Script to help the struggling youtube commenter format comments into youtube-comment-compatible strings


Usage
-----
Send a colon-separated string via standard input into the script:

```
echo "North Korea:Doesn't even lift" | ./textstack.py
```

Outputs:
```
North Korea
North Kore
North Kor
North Ko
North K
North
Nort
Nor
No
N
D
Do
Doe
Does
Doesn
Doesn'
Doesn't
Doesn't e
Doesn't ev
Doesn't eve
Doesn't even
Doesn't even l
Doesn't even li
Doesn't even lif
Doesn't even lift
```

Alternatively, it can read colon-separated strings from a file:

```
textstack.py strings.txt
```
