import os
import sys
from urllib.request import urlopen
from urllib.parse import urlparse
from datetime import datetime

def get_code_block_language(filename):
    """Determine the appropriate code block language based on file extension or name"""
    extensions = {
        '.conf': 'ini',  # Most .conf files are INI-style
        '.cfg': 'ini',
        '.ini': 'ini',
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
    
    # First check specific config files
    filename_lower = filename.lower()
    if any(name in filename_lower for name in ['nginx.conf', 'nginx', 'sites-available', 'sites-enabled']):
        return 'nginx'
    if any(name in filename_lower for name in ['apache2', 'httpd']):
        return 'apache'
    if 'postfix' in filename_lower:
        return 'ini'
    if 'dovecot' in filename_lower:
        return 'ini'
    if any(name in filename_lower for name in ['my.cnf', 'mysql']):
        return 'ini'
    if any(name in filename_lower for name in ['.service', '.socket']):
        return 'ini'
    
    # Check file extension
    _, ext = os.path.splitext(filename)
    return extensions.get(ext.lower(), 'plaintext')

def extract_urls_from_markdown(markdown_file):
    """Extract URLs (file paths) from markdown file"""
    urls = []
    with open(markdown_file, 'r') as f:
        for line in f:
            # Look for bullet points with file paths
            if line.strip().startswith('- /'):
                # Extract the path (everything after "- ")
                path = line.strip()[2:].strip()
                urls.append(path)
    return urls

def read_content(path):
    """Read content from file path"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file {path}: {str(e)}"

def create_markdown(markdown_input, output_file):
    """Generate markdown documentation from markdown input file containing paths"""
    
    # Extract URLs from markdown
    urls = extract_urls_from_markdown(markdown_input)
    
    if not urls:
        print("No file paths found in the markdown file")
        return
    
    # Create markdown content
    markdown_content = [
        f"# Server Configuration Documentation",
        f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## Table of Contents\n"
    ]
    
    # Generate TOC first
    for path in urls:
        filename = os.path.basename(path)
        heading = filename.replace('.', ' ').title()
        markdown_content.append(f"- [{heading}](#{heading.lower().replace(' ', '-')})")
    
    markdown_content.append("\n---\n")
    
    # Process each file path
    for path in urls:
        filename = os.path.basename(path)
        content = read_content(path)
        language = get_code_block_language(filename)
        
        heading = filename.replace('.', ' ').title()
        
        markdown_content.extend([
            f"## {heading}",
            f"Source: `{path}`\n",
            f"Edit Source: `sudo nano {path}`\n",
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
        print("Usage: python script.py input.md output.md")
        print("  input.md: Markdown file containing bullet points with file paths")
        print("  output.md: Output file for the generated documentation")
        sys.exit(1)
    
    create_markdown(sys.argv[1], sys.argv[2])
