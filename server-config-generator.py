import os
import sys
from datetime import datetime
import subprocess
import pexpect
from getpass import getpass

class SudoReader:
    def __init__(self, password):
        self.password = password
        self._sudo_timestamp_touched = False

    def _ensure_sudo(self):
        """Ensure sudo timestamp is updated to prevent repeated password prompts"""
        if not self._sudo_timestamp_touched:
            try:
                child = pexpect.spawn('sudo -v')
                i = child.expect(['password for.*:', pexpect.EOF])
                if i == 0:
                    child.sendline(self.password)
                    child.expect(pexpect.EOF)
                self._sudo_timestamp_touched = True
            except Exception as e:
                print(f"Error establishing sudo session: {str(e)}")
                return False
        return True

    def read_file(self, filepath):
        """Read file content using sudo if necessary"""
        try:
            # First try reading normally
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except PermissionError:
            # If permission denied, try using sudo
            if self._ensure_sudo():
                try:
                    cmd = f'sudo cat "{filepath}"'
                    child = pexpect.spawn(cmd)
                    i = child.expect(['password for.*:', pexpect.EOF], timeout=2)
                    if i == 0:
                        child.sendline(self.password)
                    content = child.read().decode()
                    child.close()
                    return content
                except Exception as e:
                    return f"Error reading file {filepath} with sudo: {str(e)}"
            return f"Error: Could not establish sudo access for {filepath}"
        except Exception as e:
            return f"Error reading file {filepath}: {str(e)}"

def get_code_block_language(filepath):
    """Determine the appropriate code block language based on file path and name"""
    filename = os.path.basename(filepath)
    filepath_lower = filepath.lower()
    filename_lower = filename.lower()
    
    # Nginx configurations
    if 'nginx/sites-available' in filepath_lower or 'nginx/sites-enabled' in filepath_lower:
        return 'nginx'
    
    # Postfix configurations
    if 'postfix' in filepath_lower and filename_lower.endswith('.cf'):
        return 'ini'
    
    # Check specific paths and files
    path_language_map = {
        '/etc/postfix/main.cf': 'ini',
        '/etc/postfix/master.cf': 'ini',
        '/etc/dovecot/dovecot.conf': 'ini',
        '/etc/opendkim.conf': 'ini',
        '/etc/netplan/50-cloud-init.yaml': 'yaml',
        '/etc/roundcube/config.inc.php': 'php',
        '/etc/postfixadmin/config.inc.php': 'php',
    }
    
    if filepath in path_language_map:
        return path_language_map[filepath]
        
    # Check extensions
    extensions = {
        '.conf': 'ini',
        '.cf': 'ini',
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
    
    # Get extension
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

def create_markdown(markdown_input, output_file, sudo_reader):
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
        content = sudo_reader.read_file(path)
        language = get_code_block_language(path)
        
        heading = filename.replace('.', ' ').title()
        
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
        print("Usage: python script.py input.md output.md")
        print("  input.md: Markdown file containing bullet points with file paths")
        print("  output.md: Output file for the generated documentation")
        sys.exit(1)

    # Initialize sudo reader with password
    sudo_reader = SudoReader('seagate')
    
    create_markdown(sys.argv[1], sys.argv[2], sudo_reader)