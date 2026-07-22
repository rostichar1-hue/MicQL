cat > microcode/executor.py << 'EOF'
from tabulate import tabulate

tables = {}

def execute(cmd):
    if cmd['cmd'] == 'CREATE':
        tables[cmd['table']] = {'rows': []}
        return f"Table '{cmd['table']}' created"

    if cmd['cmd'] == 'INSERT':
        row = dict(zip(cmd.get('fields', []), cmd['values']))
        tables[cmd['table']]['rows'].append(row)
        return f"Inserted into '{cmd['table']}'"

    if cmd['cmd'] == 'SELECT':
        rows = tables.get(cmd['table'], {}).get('rows', [])
        if cmd.get('condition'):
            if '=' in cmd['condition']:
                key, val = cmd['condition'].split('=', 1)
                rows = [r for r in rows if str(r.get(key.strip())) == val.strip().strip('"')]
            elif '>' in cmd['condition']:
                key, val = cmd['condition'].split('>', 1)
                rows = [r for r in rows if int(r.get(key.strip(), 0)) > int(val)]
        rows = rows[:cmd.get('limit', 10)]
        return tabulate(rows, headers='keys', tablefmt='grid') if rows else "No data"

    return "Unknown command"
EOF
