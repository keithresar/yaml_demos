#!/usr/bin/env bash

. demo_magic.sh

DEMO_PROMPT="${GREEN}> "
clear

pe "cat json_schema.yaml"

pe "python -c \"from yaml import load, Loader; load(open('json_schema.yaml'), Loader=Loader)\""
clear


cat json_schema.yaml

pe "yamllint json_schema.yaml"

pe "yamllint -d relaxed json_schema.yaml"


p ""

