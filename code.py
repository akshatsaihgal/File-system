import pickle

class InMemoryFileSystem:
    def __init__(self):
        self.root = Directory("/")
        self.current_directory = self.root

    def mkdir(self, name):
        if not name:
            print("Invalid directory name.")
            return
        new_directory = Directory(name)
        self.current_directory.add_entry(new_directory)

    def cd(self, path):
        if not path:
            print("Invalid path.")
            return
        if path == "/":
            self.current_directory = self.root
        elif path.startswith("/"):
            directory = self.root.find_directory_by_path(path)
            if directory:
                self.current_directory = directory
            else:
                print(f"Directory '{path}' not found.")
        else:
            directory = self.current_directory.find_directory_by_path(path)
            if directory:
                self.current_directory = directory
            else:
                print(f"Directory '{path}' not found.")

    def ls(self, path="."):
        if not path:
            print("Invalid path.")
            return
        target_directory = self.current_directory.find_directory_by_path(path)
        if target_directory:
            target_directory.list_entries()
        else:
            print(f"Directory '{path}' not found.")

    def grep(self, pattern, filename):
        if not pattern or not filename:
            print("Invalid pattern or filename.")
            return
        file = self.current_directory.find_file_by_name(filename)
        if file:
            file.grep(pattern)
        else:
            print(f"File '{filename}' not found.")

    def cat(self, filename):
        if not filename:
            print("Invalid filename.")
            return
        file = self.current_directory.find_file_by_name(filename)
        if file:
            file.display_contents()
        else:
            print(f"File '{filename}' not found.")

    def touch(self, filename):
        if not filename:
            print("Invalid filename.")
            return
        new_file = File(filename)
        self.current_directory.add_entry(new_file)

    def echo(self, text, filename):
        if not text or not filename:
            print("Invalid text or filename.")
            return
        file = self.current_directory.find_file_by_name(filename)
        if file:
            file.write_text(text)
        else:
            print(f"File '{filename}' not found.")

    def mv(self, source_path, destination_path):
        if not source_path or not destination_path:
            print("Invalid source or destination path.")
            return
        source_entry = self.current_directory.find_entry_by_path(source_path)
        destination_directory = self.current_directory.find_directory_by_path(destination_path)

        if source_entry and destination_directory:
            destination_directory.add_entry(source_entry)
            self.current_directory.remove_entry(source_entry)
        else:
            print("Invalid source or destination.")

    def cp(self, source_path, destination_path="."):
        if not source_path or not destination_path:
            print("Invalid source or destination path.")
            return
        source_entry = self.current_directory.find_entry_by_path(source_path)
        destination_directory = self.current_directory.find_directory_by_path(destination_path)

        if source_entry and destination_directory:
            new_entry = source_entry.clone()
            destination_directory.add_entry(new_entry)
        else:
            print("Invalid source or destination.")

    def rm(self, path):
        if not path:
            print("Invalid path.")
            return
        entry = self.current_directory.find_entry_by_path(path)

        if entry:
            self.current_directory.remove_entry(entry)
        else:
            print(f"Entry at '{path}' not found.")

    def save_state(self, filename="filesystem_state.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self.root, file)

    def load_state(self, filename="filesystem_state.pkl"):
        try:
            with open(filename, "rb") as file:
                self.root = pickle.load(file)
                self.current_directory = self.root
        except FileNotFoundError:
            print(f"File '{filename}' not found. Creating a new file system.")

class Directory:
    def __init__(self, name):
        self.name = name
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def remove_entry(self, entry):
        self.entries.remove(entry)

    def find_entry_by_path(self, path):
        if path == "/":
            return self
        components = path.split("/")
        current_directory = self
        for component in components:
            if component == "..":
                current_directory = current_directory.parent
            elif component:
                entry = current_directory.find_entry_by_name(component)
                if isinstance(entry, Directory):
                    current_directory = entry
                elif isinstance(entry, File):
                    return entry
                else:
                    return None
        return current_directory

    def find_directory_by_path(self, path):
        entry = self.find_entry_by_path(path)
        return entry if isinstance(entry, Directory) else None

    def find_entry_by_name(self, name):
        for entry in self.entries:
            if entry.name == name:
                return entry
        return None

    def list_entries(self):
        for entry in self.entries:
            print(entry.name, end=" ")
        print()

class File:
    def __init__(self, name):
        self.name = name
        self.contents = ""

    def display_contents(self):
        print(self.contents)

    def write_text(self, text):
        self.contents = text

    def grep(self, pattern):
        lines = self.contents.split("\n")
        for i, line in enumerate(lines, start=1):
            if pattern in line:
                print(f"{self.name}:{i}: {line}")

    def clone(self):
        new_file = File(self.name)
        new_file.contents = self.contents
        return new_file

# Example Usage:
fs = InMemoryFileSystem()

# Perform operations...

# Save the file system state to a file
fs.save_state()

# Load the file system state from the file
fs.load_state()
