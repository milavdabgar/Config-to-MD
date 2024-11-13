#!/bin/bash

# Function to generate a slug from filename
generate_slug() {
    echo "$1" | tr '[:upper:]' '[:lower:]' | sed 's/\./-/g' | tr ' ' '-'
}

# Function to get file extension
get_extension() {
    echo "${1##*.}"
}

# Function to process markdown configuration file
process_config() {
    local config_file="$1"
    local temp_dir="$2"
    
    # Initialize arrays
    declare -a include_exts
    declare -a exclude_dirs
    declare -a scan_dirs
    
    # Process the configuration file
    while IFS= read -r line; do
        if [[ $line =~ ^-[[:space:]]*exclude:[[:space:]]*(.*) ]]; then
            exclude_dirs+=("${BASH_REMATCH[1]}")
        elif [[ $line =~ ^-[[:space:]]*include_ext:[[:space:]]*(.*) ]]; then
            # Split the extensions and add to array
            IFS=' ' read -ra EXTS <<< "${BASH_REMATCH[1]}"
            for ext in "${EXTS[@]}"; do
                # Remove any dots from the extension
                ext="${ext#.}"
                include_exts+=("$ext")
            done
        elif [[ $line =~ ^-[[:space:]]*exclude_ext:[[:space:]]*(.*) ]]; then
            continue  # Skip exclude_ext as we're using include_ext
        elif [[ $line =~ ^-[[:space:]]*(/.+) ]]; then
            scan_dirs+=("${BASH_REMATCH[1]}")
        fi
    done < "$config_file"
    
    # Create find command for each directory
    for dir in "${scan_dirs[@]}"; do
        if [ ! -d "$dir" ]; then
            echo "Warning: Directory $dir does not exist, skipping..."
            continue
        fi
        
        # Start building find command
        find_cmd="find \"$dir\" -type f"
        
        # Add extension filters
        ext_filter=""
        for ext in "${include_exts[@]}"; do
            if [ -z "$ext_filter" ]; then
                ext_filter="\\( -name \"*.$ext\""
            else
                ext_filter="$ext_filter -o -name \"*.$ext\""
            fi
        done
        if [ ! -z "$ext_filter" ]; then
            find_cmd="$find_cmd $ext_filter \\)"
        fi
        
        # Add exclude directory filters
        for exclude in "${exclude_dirs[@]}"; do
            if [ ! -z "$exclude" ]; then
                find_cmd="$find_cmd -not -path \"$exclude*\""
            fi
        done
        
        # Execute find command and save results
        echo "Scanning $dir..."
        eval "$find_cmd" | sort >> "$temp_dir/files.txt"
    done
}

# Function to generate markdown documentation
generate_markdown() {
    local files_list="$1"
    local output_file="$2"
    
    # Start markdown file
    echo "# Project Documentation" > "$output_file"
    echo "Generated on: $(date '+%Y-%m-%d %H:%M:%S')" >> "$output_file"
    echo >> "$output_file"
    
    # Generate TOC
    echo "## Table of Contents" >> "$output_file"
    echo >> "$output_file"
    
    # Process each file and create TOC
    current_dir=""
    while IFS= read -r file; do
        dir=$(dirname "$file")
        if [ "$dir" != "$current_dir" ]; then
            echo -e "\n### ${dir#*/}" >> "$output_file"
            current_dir="$dir"
        fi
        
        filename=$(basename "$file")
        slug=$(generate_slug "$filename")
        echo "- [$filename](#$slug)" >> "$output_file"
    done < "$files_list"
    
    # Add separator
    echo -e "\n---\n" >> "$output_file"
    
    # Add file contents
    while IFS= read -r file; do
        filename=$(basename "$file")
        echo -e "## $filename" >> "$output_file"
        echo "Path: \`$file\`" >> "$output_file"
        echo >> "$output_file"
        
        # Get file extension
        ext=$(get_extension "$filename")
        
        # Add file content with appropriate markdown formatting
        echo '```'"$ext" >> "$output_file"
        
        # Read file content into variable and ensure it ends with a newline
        content=$(cat "$file"; echo)
        
        # Remove the extra newline we added if the file already ended with one
        content=${content%$'\n'}
        
        # Append the content
        echo "$content" >> "$output_file"
        
        # Ensure there's a newline before the closing backticks
        echo >> "$output_file"
        echo '```' >> "$output_file"
        echo >> "$output_file"
    done < "$files_list"
}

# Main script
main() {
    if [ "$#" -ne 2 ]; then
        echo "Usage: $0 input.md output.md"
        exit 1
    fi
    
    input_file="$1"
    output_file="$2"
    
    # Create temporary directory
    temp_dir=$(mktemp -d)
    trap 'rm -rf "$temp_dir"' EXIT
    
    # Process configuration and find files
    process_config "$input_file" "$temp_dir"
    
    # Check if any files were found
    if [ ! -s "$temp_dir/files.txt" ]; then
        echo "No files found matching the criteria!"
        exit 1
    fi
    
    # Generate markdown documentation
    generate_markdown "$temp_dir/files.txt" "$output_file"
    
    echo "Documentation generated successfully: $output_file"
}

# Run main function
main "$@"
