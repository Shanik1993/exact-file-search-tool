Exact Filename Search Tool
==========================

A comprehensive Python GUI application for searching, managing, and organizing files by exact filename matching. This tool provides an intuitive interface for batch file operations across directories.

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-GNU-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

📋 Table of Contents
--------------------

-   Features

-   Screenshots

-   Installation

-   Usage

-   Detailed Guide

-   File Operations

-   Troubleshooting

-   Technical Details

-   Contributing

-   License

✨ Features
----------

### 🔍 Advanced Search Capabilities

-   Exact filename matching with recursive directory scanning

-   Batch processing of multiple filenames from text input

-   Real-time results with visual status indicators (✓ Found / ✗ Not Found)

-   File size display in human-readable format (B, KB, MB, GB)

### 📁 File Management

-   Copy files with duplicate handling (auto-renaming)

-   Move files with automatic conflict resolution

-   Extension management - add/change extensions to multiple files

-   Bulk operations - select all found files or clear selection

### 🎯 User Experience

-   Intuitive GUI built with Tkinter

-   Detailed file information on double-click

-   Comprehensive status updates and progress tracking

-   Error handling with meaningful error messages

-   Cross-platform compatibility (Windows, Linux, macOS)

🖼️ Screenshots
---------------

<img width="949" height="778" alt="image" src="https://github.com/user-attachments/assets/6b5d25d2-5a76-472b-92d8-73c3c1fcb6fd" />

```text
[Main Interface] - Show the main application window
[Search Results] - Display search results with found/not found status
[File Operations] - Demonstrate copy/move operations
```
🚀 Installation
---------------

### Prerequisites

-   Python 3.6 or higher

-   tkinter (usually included with Python standard library)

### Method 1: Direct Download

1.  Download the `File Mover.py` file from this repository

2.  Navigate to the downloaded directory

3.  Run the application:

 ```bash
   python "File Mover.py"
```
### Method 2: Git Clone

```bash

# Clone the repository
git clone https://github.com/yourusername/exact-file-search-tool.git

# Navigate to the directory
cd exact-file-search-tool

# Run the application
python "File Mover.py"
```

1.  Download the latest release from the Releases section

2.  Extract the zip file

3.  Run `File Mover.exe`

📖 Usage
--------

### Basic Workflow

1.  Launch the Application

    ```bash

    python "File Mover.py"

2.  Configure Source and Destination

    -   Click "Browse" next to "Source Folder" to select where to search for files

    -   Click "Browse" next to "Destination Folder" to select where to copy/move files

3.  Input Filenames

    -   Paste your filenames in the text area (one filename per line)

    -   Use the example format provided or your own list

4.  Manage File Extensions (Optional)

    -   Enter desired extension (e.g., `.xml`, `.txt`, `.pdf`)

    -   Click "Add Extension" to apply to all filenames

5.  Search for Files

    -   Click "Search Files" to begin the search process

    -   Review results in the "Found Files" section

6.  Perform File Operations

    -   Use "Select All" to select all found files

    -   Use "Clear Selection" to deselect all files

    -   Click "Copy Selected" to copy files to destination

    -   Click "Move Selected" to move files to destination

🔧 Detailed Guide
-----------------

### Filename Input Format

The application accepts filenames in a simple text format:

```text
filename1
filename2
filename3
```
Example:

```text
INNA010125TPAIA20259000022110.xml
INNA010125TPAIA2025900005969X.xml
INNA010125TPAIA20259000093509.xml
```
### Extension Management

The "Add Extension" feature automatically:

-   Adds the specified extension to all filenames

-   Removes any existing extensions before adding the new one

-   Handles both extensions with and without leading dot

Examples:

-   Input: `document` + Extension: `.txt` → Output: `document.txt`

-   Input: `file.pdf` + Extension: `.xml` → Output: `file.xml`

### Search Behavior

-   Recursive Search: Searches through all subdirectories of the source folder

-   Exact Match: Requires exact filename match (case-sensitive on Linux/macOS)

-   Multiple Instances: Returns the first found instance of each filename

-   Status Tracking: Clearly indicates found and missing files

### File Operations

#### Copy Files

-   Creates duplicates in the destination folder

-   Preserves original files in source location

-   Auto-renames duplicates: `file.txt` → `file_1.txt` → `file_2.txt`

#### Move Files

-   Relocates files from source to destination

-   Removes original files from source location

-   Same duplicate handling as copy operation

📊 File Operations
------------------

### Supported File Types

-   All file types are supported

-   No restrictions on file extensions

-   Handles both small and large files efficiently

### Performance Considerations

-   Search Speed: Depends on number of files and directory depth

-   Operation Speed: Copy/move speed depends on file sizes and storage medium

-   Memory Usage: Minimal memory footprint, suitable for large file lists

### Error Handling

-   Missing Source: Clear error message if source folder doesn't exist

-   Missing Destination: Prompt to select destination folder

-   Permission Issues: Detailed error messages for access problems

-   File in Use: Graceful handling of locked files

🛠️ Troubleshooting
-------------------

### Common Issues

1\. Application Won't Start

```bash
# Check Python installation
python --version

# Ensure tkinter is available
python -m tkinter
```
2\. Files Not Found

-   Verify source folder contains the files

-   Check filename spelling and case sensitivity

-   Ensure correct file extensions

3\. Permission Errors

-   Run as administrator (Windows) or use sudo (Linux/macOS)

-   Check folder write permissions

-   Ensure files aren't open in other applications

4\. Duplicate File Handling

-   The application automatically renames duplicates

-   Original files are never overwritten

-   New names follow pattern: `filename_counter.extension`

### Performance Tips

-   Large Directories: Be patient with deep directory structures

-   Many Files: Search operations may take time with 10,000+ files

-   Network Drives: Operations may be slower on network locations

🔬 Technical Details
--------------------

### Architecture

-   GUI Framework: Tkinter for cross-platform compatibility

-   File Operations: Python's `shutil` and `os` modules

-   Search Algorithm: Recursive directory traversal with exact matching

### Code Structure

```text
ExactFileSearchApp
├── __init__() - Initialize GUI and variables
├── create_widgets() - Build user interface
├── search_exact_files() - Core search functionality
├── process_files() - Handle copy/move operations
└── Helper methods for extensions, selection, etc.
```
### Dependencies

-   Python Standard Library Only:

    -   `tkinter` - GUI components

    -   `os` - File system operations

    -   `shutil` - File copy/move operations

    -   `pathlib` - Path manipulation

🤝 Contributing
---------------

We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup

1.  Fork the repository

2.  Create a feature branch: `git checkout -b feature/new-feature`

3.  Commit your changes: `git commit -am 'Add new feature'`

4.  Push to the branch: `git push origin feature/new-feature`

5.  Submit a pull request

### Suggested Improvements

-   Add regular expression support

-   Implement file preview functionality

-   Add progress bars for large operations

-   Support for file content search

-   Dark mode theme

📄 License
----------

This project is licensed under the GNU License - see the [LICENSE] file for details.

📞 Support
----------

If you encounter any issues or have questions:

1.  Check this README for troubleshooting tips

2.  Open an Issue on GitHub with detailed description

3.  Include: Python version, OS, error messages, and steps to reproduce

🎯 Use Cases
------------

### Ideal For:

-   Data Migration: Moving specific files between systems

-   File Organization: Sorting and categorizing files

-   Backup Operations: Selective backup of important files

-   Batch Processing: Preparing files for other applications

-   Data Analysis: Extracting specific datasets from large directories

* * * * *

⭐ If you find this tool useful, please consider giving it a star on GitHub!
