#!/bin/bash

prepend="<link rel=\"stylesheet\" type=\"text/css\" href=\"aho.css\">"
find . -name '*.html' -exec sed -i.old "1s;^;$prepend;" {} \;

