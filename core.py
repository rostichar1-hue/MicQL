from .parser import parse
from .executor import execute

def run_file(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('//')]

    output = [f"\n{'='*50}\n  MicroCode: {filename}\n{'='*50}\n"]
    for line in lines:
        cmd = parse(line)
        if cmd:
            output.append(execute(cmd))
        else:
            output.append(f"Unknown: {line}")
    return '\n'.join(output)
