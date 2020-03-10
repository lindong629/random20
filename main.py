#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Jimmy Lin

import random

with open("num.txt","w",encoding="utf8") as f:
    for i in range(20):
        li = []
        while True:
            num = str(random.randint(0, 9))
            if num not in li:
                li.append(num)
            if len(li) == 5:
                result = "".join(li)
                re1 = "".join(li[::-1])
                break
        if i < 9:
            f.write("0" + str(i + 1) + " " * 2 + "|" + " " * 2 + str(result) + " | " + str(re1) + " " * 2 + "[  ]" + "\n")
        else:
            f.write(str(i + 1) + " " * 2 + "|" + " " * 2 + str(result) + " | " + str(re1) + " " * 2 + "[  ]" + "\n")
