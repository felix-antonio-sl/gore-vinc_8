import os
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern

# Directorios que siempre queremos ignorar
DEFAULT_IGNORE = {
    'venv', 'env', '.env', '.venv', '__pycache__', 
    'node_modules', '.git', '.idea', '.vscode',
    'dist', 'build', 'eggs', '.eggs',
    'migrations', 'docsaux', 'ell_store'
}

def load_gitignore(path):
    """Carga las reglas del .gitignore"""
    gitignore_path = os.path.join(path, '.gitignore')
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            spec = PathSpec.from_lines(GitWildMatchPattern, f.readlines())
        return spec
    return None

def get_file_extension(filename):
    """Obtiene la extensión del archivo para el bloque de código"""
    ext = os.path.splitext(filename)[1].lower()
    ext_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.md': 'markdown',
        '.json': 'json',
        '.yml': 'yaml',
        '.yaml': 'yaml',
    }
    return ext_map.get(ext, '')

def generate_project_tree(start_path, output_file, relevant_files):
    """Genera un archivo Markdown con el árbol del proyecto y el contenido de archivos relevantes"""
    gitignore = load_gitignore(start_path)
    all_files = []
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Documentación del Proyecto\n\n')
        f.write('## Estructura del Proyecto\n\n```\n')
        
        for root, dirs, files in os.walk(start_path):
            # Filtrar directorios por defecto
            dirs[:] = [d for d in dirs if d not in DEFAULT_IGNORE]
            
            # Filtrar por gitignore
            rel_root = os.path.relpath(root, start_path)
            if gitignore:
                dirs[:] = [d for d in dirs if not gitignore.match_file(os.path.join(rel_root, d))]
                files = [f for f in files if not gitignore.match_file(os.path.join(rel_root, f))]
            
            # Guardar archivos para mostrar después
            for file in files:
                full_path = os.path.join(rel_root, file)
                if full_path != output_file:  # Evitar incluir el archivo de documentación
                    all_files.append(full_path)
            
            level = rel_root.count(os.sep)
            indent = '  ' * level
            if root != start_path:
                f.write(f'{indent}{os.path.basename(root)}/\n')
            subindent = '  ' * (level + 1)
            for file in files:
                f.write(f'{subindent}{file}\n')
        
        f.write('```\n\n')
        
        f.write('## Código Fuente\n\n')
        for file_path in sorted(all_files):
            if os.path.exists(file_path):
                ext = get_file_extension(file_path)
                f.write(f'### {file_path}\n\n```{ext}\n')
                try:
                    with open(file_path, 'r', encoding='utf-8') as source_file:
                        f.write(source_file.read())
                except UnicodeDecodeError:
                    f.write('// Archivo binario o con codificación no soportada\n')
                f.write('\n```\n\n')

if __name__ == '__main__':
    project_path = '.'
    relevant_files = [
        'app/chat/routes.py',
        'app/__init__.py',
        'app/chat/__init__.py'
    ]
    
    generate_project_tree(project_path, 'documentacion_proyecto.md', relevant_files)