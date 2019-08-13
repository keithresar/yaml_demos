#!/usr/bin/env python

import yaml


document = """
---
- just a string 
- True
- true
- yes
- on
- off
- no
- !!bool true
- !!bool false
- !!bool "no"
- "no"
- 0
- 
  a: 1
  b: 2
- 
  - a
  - b
"""


print yaml.dump(yaml.load(document))


