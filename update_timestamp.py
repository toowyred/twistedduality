#!/usr/bin/env python3
"""
Update the build timestamp in index.html before git push.
Replaces the build-tag div with current date/time.
"""
import os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from datetime import datetime

html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Get current date/time in MMDD / HHMM format
now = datetime.now()
date_str = now.strftime('%m%d')
time_str = now.strftime('%H%M')
new_tag = f'{date_str}<br>{time_str}'

# Find and replace the build-tag div
import re
pattern = r'<div id="build-tag">[^<]*<br>[^<]*</div>'
replacement = f'<div id="build-tag">{new_tag}</div>'

updated_content = re.sub(pattern, replacement, content)

if updated_content != content:
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print(f'✓ Updated build timestamp to {date_str} / {time_str}')
else:
    print('✗ Could not find build-tag div')
    exit(1)
