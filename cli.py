import sys
import os
from .parser import parse
from .executor import execute

def main():
    if len(sys.argv) < 2:
        filename = "data.mc"
    else:
        filename = sys.argv[1]

    if not os.path.exists(filename):
        print(f"Файл {filename} не найден. Создаю data.mc...")
        with open("data.mc", "w") as f:
            f.write("CREATE users (id INT, name STRING, age INT)\n")
            f.write("+users {1, \"Alex\", 28}\n")
            f.write("+users {2, \"Kate\", 22}\n")
            f.write("users:name(age>20)10\n")
            f.write("SAVE\n")
        print("✅ Создан data.mc с примерами.")

    with open(filename) as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith('//')]

    print(f"\n{'='*50}\n  Micql: {filename}\n{'='*50}\n")
    for line in lines:
        cmd = parse(line)
        if cmd:
            print(execute(cmd))
        else:
            print(f"Unknown: {line}")

if __name__ == "__main__":
    main()
