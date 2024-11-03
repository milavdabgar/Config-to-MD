import os
import sys
from urllib.request import urlopen
from urllib.parse import urlparse
from datetime import datetime

def get_code_block_language(filename):
    """Determine the appropriate code block language based on file extension or name"""
    extensions = {
        '.conf': 'conf',
        '.nginx': 'nginx',
        '.php': 'php',
        '.py': 'python',
        '.sh': 'bash',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.sql': 'sql',
        '.xml': 'xml',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.json': 'json'
    }
    
    # Special cases for specific filenames
    if 'nginx' in filename.lower():
        return 'nginx'
    if 'apache' in filename.lower():
        return 'apache'
    if 'php' in filename.lower():
        return 'php'
    
    # Check file extension
    _, ext = os.path.splitext(filename)
    return extensions.get(ext.lower(), 'plaintext')

def generate_heading(filename):
    """Generate a readable heading from filename"""
    # Remove extension and path
    base = os.path.basename(filename)
    name = os.path.splitext(base)[0]
    
    # Convert dashes and underscores to spaces
    name = name.replace('-', ' ').replace('_', ' ')
    
    # Capitalize words
    return name.title()

def read_content(path):
    """Read content from either URL or local file"""
    # Check if it's a URL
    if path.startswith(('http://', 'https://')):
        try:
            with urlopen(path) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            return f"Error fetching URL {path}: {str(e)}"
    
    # Handle local file
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {path}: {str(e)}"

def create_markdown(files_list, output_file):
    """Generate markdown documentation from list of files/URLs"""
    
    # Read paths from file
    with open(files_list, 'r') as f:
        paths = [line.strip() for line in f if line.strip()]
    
    # Create markdown content
    markdown_content = [
        f"# Server Configuration Guide",
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## Table of Contents\n"
    ]
    
    # Generate TOC first
    for path in paths:
        filename = os.path.basename(path)
        heading = generate_heading(filename)
        markdown_content.append(f"- [{heading}](#{heading.lower().replace(' ', '-')})")
    
    markdown_content.append("\n---\n")
    
    # Process each path
    for path in paths:
        filename = os.path.basename(path)
        content = read_content(path)
        language = get_code_block_language(filename)
        
        heading = generate_heading(filename)
        
        markdown_content.extend([
            f"## {heading}",
            f"Source: `{path}`\n",
            f"```{language}",
            content,
            "```\n"
        ])
    
    # Write to output file
    with open(output_file, 'w') as f:
        f.write('\n'.join(markdown_content))
    
    print(f"Documentation generated successfully: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py files_list.txt output.md")
        sys.exit(1)
    
    create_markdown(sys.argv[1], sys.argv[2])
