#!/bin/bash
# 26/6/2011
# by b4d
# Script that downloads all 8 episodes of BBS documentary


for num in {1..8}
do
   wget http://www.archive.org/download/BBS.The.Documentary/BBS.The.Documentary.ep${num}.avi
done

