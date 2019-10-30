#!/bin/bash

git pull
git add --all
if [$# -gt 0];
then
    git commit -m $1
else
    git commit -m "wsswsswss"
fi
git push
