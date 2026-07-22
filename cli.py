import sys
from microcode.parser import parse
from microcode.executor import execute

def run_file(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('//')]

    out = [f"\n{'='*50}\n  MicroCode: {filename}\n{'='*50}\n"]
    for line in lines:
        cmd = parse(line)
        if cmd:
            out.append(execute(cmd))
        else:
            out.append(f"Unknown: {line}")
    return '\n'.join(out)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: micro <file.mc>")
        sys.exit(1)
    print(run_file(sys.argv[1]))
