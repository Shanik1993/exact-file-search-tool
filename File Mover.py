import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import shutil
from pathlib import Path

class ExactFileSearchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exact Filename Search Tool")
        self.root.geometry("950x750")
        
        # Variables
        self.source_folder = tk.StringVar()
        self.destination_folder = tk.StringVar()
        self.extension_var = tk.StringVar(value=".xml")
        self.found_files = []
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Exact Filename Search Tool", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(0, 15))
        
        # Source folder selection
        ttk.Label(main_frame, text="Source Folder:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.source_folder, width=50).grid(row=1, column=1, padx=5, columnspan=2)
        ttk.Button(main_frame, text="Browse", command=self.browse_source).grid(row=1, column=3, padx=5)
        
        # Destination folder selection
        ttk.Label(main_frame, text="Destination Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.destination_folder, width=50).grid(row=2, column=1, padx=5, columnspan=2)
        ttk.Button(main_frame, text="Browse", command=self.browse_destination).grid(row=2, column=3, padx=5)
        
        # Extension section
        extension_frame = ttk.Frame(main_frame)
        extension_frame.grid(row=3, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(extension_frame, text="Add Extension:").pack(side=tk.LEFT, padx=(0, 5))
        extension_entry = ttk.Entry(extension_frame, textvariable=self.extension_var, width=10)
        extension_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(extension_frame, text="Add Extension", command=self.add_extension_to_filenames).pack(side=tk.LEFT, padx=5)
        
        # Instruction label
        ttk.Label(extension_frame, text="(Adds extension to all filenames in the list)", 
                 font=("Arial", 8), foreground="gray").pack(side=tk.LEFT, padx=10)
        
        # Filename input area
        ttk.Label(main_frame, text="Paste Filenames (one per line):").grid(row=4, column=0, sticky=tk.NW, pady=5)
        
        # Text area for pasting filenames
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=4, column=1, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=5)
        
        self.filename_text = scrolledtext.ScrolledText(text_frame, width=60, height=8, wrap=tk.WORD)
        self.filename_text.pack(fill=tk.BOTH, expand=True)
        
        # Example text in the text area
        example_text = """INNA010125TPAIA20259000022110
INNA010125TPAIA2025900005969X
INNA010125TPAIA20259000093509
INNA010425TPAIA20259000564539
INNA080125TPAIA20259023033926
INNA080725TPAIA20259024200272
INNA080825TPAIA20259024278625
INNA080825TPAIA20259024286087
INNA080825TPAIA20259024335823"""
        
        self.filename_text.insert("1.0", example_text)
        
        # Search button
        ttk.Button(main_frame, text="Search Files", command=self.search_exact_files).grid(row=5, column=1, pady=10)
        
        # Results frame
        results_frame = ttk.LabelFrame(main_frame, text="Found Files", padding="5")
        results_frame.grid(row=6, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        
        # Treeview for file list
        columns = ("filename", "status", "size", "full_path")
        self.tree = ttk.Treeview(results_frame, columns=columns, show="headings", height=10)
        
        # Define headings
        self.tree.heading("filename", text="Filename")
        self.tree.heading("status", text="Status")
        self.tree.heading("size", text="Size")
        self.tree.heading("full_path", text="Full Path")
        
        # Set column widths
        self.tree.column("filename", width=250)
        self.tree.column("status", width=100)
        self.tree.column("size", width=100)
        self.tree.column("full_path", width=350)
        
        # Scrollbars
        v_scrollbar = ttk.Scrollbar(results_frame, orient=tk.VERTICAL, command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(results_frame, orient=tk.HORIZONTAL, command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Grid layout
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        v_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        h_scrollbar.grid(row=1, column=0, sticky=(tk.W, tk.E))
        
        # Action buttons frame
        action_frame = ttk.Frame(main_frame)
        action_frame.grid(row=7, column=0, columnspan=4, pady=10)
        
        ttk.Button(action_frame, text="Select All", command=self.select_all).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Clear Selection", command=self.clear_selection).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Copy Selected", command=self.copy_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Move Selected", command=self.move_files).pack(side=tk.LEFT, padx=5)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready - Paste filenames and click 'Search Files'")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN)
        status_label.grid(row=8, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=5)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(4, weight=1)
        main_frame.rowconfigure(6, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        
        # Bind double-click to show file info
        self.tree.bind("<Double-1>", self.show_file_info)
    
    def browse_source(self):
        folder = filedialog.askdirectory(title="Select Source Folder")
        if folder:
            self.source_folder.set(folder)
    
    def browse_destination(self):
        folder = filedialog.askdirectory(title="Select Destination Folder")
        if folder:
            self.destination_folder.set(folder)
    
    def add_extension_to_filenames(self):
        """Add extension to all filenames in the text area"""
        extension = self.extension_var.get().strip()
        
        if not extension:
            messagebox.showwarning("Warning", "Please enter an extension first!")
            return
        
        # Ensure extension starts with a dot if not already
        if not extension.startswith('.'):
            extension = '.' + extension
        
        # Get current text content
        text_content = self.filename_text.get("1.0", tk.END).strip()
        if not text_content:
            messagebox.showwarning("Warning", "No filenames to add extension to!")
            return
        
        # Split by lines and process each line
        lines = text_content.split('\n')
        processed_lines = []
        
        for line in lines:
            line = line.strip()
            if line:  # Only process non-empty lines
                # Remove any existing extension and add the new one
                if '.' in line:
                    # Remove existing extension
                    base_name = line.rsplit('.', 1)[0]
                    processed_lines.append(base_name + extension)
                else:
                    # No existing extension, just add the new one
                    processed_lines.append(line + extension)
        
        # Update the text area with processed filenames
        self.filename_text.delete("1.0", tk.END)
        self.filename_text.insert("1.0", "\n".join(processed_lines))
        
        self.status_var.set(f"Added extension '{extension}' to {len(processed_lines)} filenames")
    
    def get_filenames_from_text(self):
        """Extract filenames from the text area"""
        text_content = self.filename_text.get("1.0", tk.END).strip()
        if not text_content:
            return []
        
        # Split by lines and remove empty lines
        filenames = [line.strip() for line in text_content.split('\n') if line.strip()]
        return filenames
    
    def search_exact_files(self):
        source = self.source_folder.get()
        filenames = self.get_filenames_from_text()
        
        if not source:
            messagebox.showerror("Error", "Please select a source folder first!")
            return
        
        if not filenames:
            messagebox.showwarning("Warning", "Please paste filenames in the text area!")
            return
        
        try:
            # Clear previous results
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            self.found_files = []
            found_count = 0
            not_found_count = 0
            
            # Search for each exact filename
            for filename in filenames:
                found = False
                file_path = ""
                
                # Search recursively through all subfolders
                for root_dir, _, files in os.walk(source):
                    if filename in files:
                        file_path = os.path.join(root_dir, filename)
                        file_size = os.path.getsize(file_path)
                        
                        # Add to treeview
                        self.tree.insert("", "end", values=(
                            filename, 
                            "✓ Found",
                            self.format_size(file_size),
                            file_path
                        ))
                        
                        self.found_files.append(file_path)
                        found_count += 1
                        found = True
                        break
                
                if not found:
                    # File not found
                    self.tree.insert("", "end", values=(
                        filename, 
                        "✗ Not Found",
                        "N/A",
                        "File not found in source folder"
                    ))
                    not_found_count += 1
            
            self.status_var.set(f"Search complete: {found_count} found, {not_found_count} not found")
            
            if not_found_count > 0:
                messagebox.showwarning("Some files not found", 
                                      f"{not_found_count} files were not found in the source folder.")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error searching files: {str(e)}")
    
    def format_size(self, size_bytes):
        """Convert file size to human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} TB"
    
    def select_all(self):
        # Select only found files (skip "not found" entries)
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values[1] == "✓ Found":  # Only select found files
                self.tree.selection_add(item)
    
    def clear_selection(self):
        self.tree.selection_set([])
    
    def get_selected_files(self):
        selected_items = self.tree.selection()
        selected_files = []
        
        for item in selected_items:
            values = self.tree.item(item, "values")
            if values[1] == "✓ Found":  # Only include found files
                selected_files.append(values[3])  # full_path is at index 3
        
        return selected_files
    
    def copy_files(self):
        self.process_files("copy")
    
    def move_files(self):
        self.process_files("move")
    
    def process_files(self, action):
        destination = self.destination_folder.get()
        selected_files = self.get_selected_files()
        
        if not destination:
            messagebox.showerror("Error", "Please select a destination folder first!")
            return
        
        if not selected_files:
            messagebox.showwarning("Warning", "Please select files to process!")
            return
        
        try:
            success_count = 0
            failed_files = []
            
            for file_path in selected_files:
                try:
                    file_name = os.path.basename(file_path)
                    dest_path = os.path.join(destination, file_name)
                    
                    # Handle duplicate files
                    counter = 1
                    base_name, ext = os.path.splitext(file_name)
                    while os.path.exists(dest_path):
                        new_name = f"{base_name}_{counter}{ext}"
                        dest_path = os.path.join(destination, new_name)
                        counter += 1
                    
                    if action == "copy":
                        shutil.copy2(file_path, dest_path)
                    else:  # move
                        shutil.move(file_path, dest_path)
                    
                    success_count += 1
                    
                except Exception as e:
                    failed_files.append(f"{os.path.basename(file_path)}: {str(e)}")
            
            # Update status
            if failed_files:
                error_msg = f"{action.capitalize()}ed {success_count} files successfully.\n\nFailed files:\n" + "\n".join(failed_files[:5])
                if len(failed_files) > 5:
                    error_msg += f"\n...and {len(failed_files) - 5} more"
                messagebox.showerror("Partial Success", error_msg)
            else:
                messagebox.showinfo("Success", f"{action.capitalize()}ed {success_count} files successfully!")
            
            self.status_var.set(f"{action.capitalize()}ed {success_count} files successfully")
            
            # Refresh search if files were moved
            if action == "move":
                self.search_exact_files()
                
        except Exception as e:
            messagebox.showerror("Error", f"Error processing files: {str(e)}")
    
    def show_file_info(self, event):
        selected = self.tree.selection()
        if selected:
            item = selected[0]
            values = self.tree.item(item, "values")
            messagebox.showinfo("File Information", 
                               f"Filename: {values[0]}\nStatus: {values[1]}\nSize: {values[2]}\nPath: {values[3]}")

def main():
    root = tk.Tk()
    app = ExactFileSearchApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
