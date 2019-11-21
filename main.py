#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Jimmy Lin

import random

with open("num.txt","w",encoding="utf8") as f:
    for i in range(20):
        li = []
        for i2 in range(5):
            li.append(str(random.randrange(0, 10)))
        result = "".join(li)
        if i < 9:
            f.write("0" + str(i + 1) + " " * 2 + "|" + " " * 2 + str(result) + " " * 2 + "[  ]" + "\n")
        else:
            f.write(str(i + 1) + " " * 2 + "|" + " " * 2 + str(result) + " " * 2 + "[  ]" + "\n")