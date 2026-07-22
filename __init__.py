cat > microcode/__init__.py << 'EOF'
from .core import run_file
from .parser import parse
from .executor import execute
from .storage import tables
EOF
