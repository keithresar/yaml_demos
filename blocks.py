#!/usr/bin/env python

import yaml


document = """
---
- foo: |1
         Line 1
         Line 2

"""


print yaml.dump(yaml.load(document))


