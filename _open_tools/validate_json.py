import json, glob, os
print('Running basic JSON syntax check...')
for f in glob.glob('**/*.json', recursive=True):
    try:
        with open(f) as fh: json.load(f)
    except Exception as e:
        print(f'⚠️  Invalid JSON in {f}: {e}')
print('✓ JSON syntax check complete.')
