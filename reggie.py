#!/usr/bin/env python3

import re


my_txt = """I want to SSH into 992.168.1.1 tonight.

And then I will also configure my 10.0.0.1 router.

Then, why not, ping 8.8.8.8 to check my connectivity?"""

pat = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

all_matches = re.findall(pat, my_txt)

print(all_matches)