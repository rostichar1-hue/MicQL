cat > microcode/executor.py << 'EOF'
from tabulate import tabulate
from .storage import create, insert, select, tables

def execute(cmd):
    if cmd['cmd'] == 'CREATE':
        create(cmd['table'], cmd['fields'])
        return f"Table '{cmd['table']}' created"

    if cmd['cmd'] == 'INSERT':
        insert(cmd['table'], cmd['values'])
        return f"Inserted into '{cmd['table']}'"

    if cmd['cmd'] == 'SELECT':
        rows = select(
            cmd['table'],
            cmd['fields'],
            cmd.get('condition', ''),
            cmd.get('limit', 10)
        )
        if rows:
            return tabulate(rows, headers='keys', tablefmt='grid')
        return "No data"

    return "Unknown command"
EOF
