# File-system
An in-memory file system implementation in a language of your choice to accommodate the functionalities. This needs to run an infinite loop with an exit code. And it should implement the commands as you would in a terminal.

Class InMemoryFileSystem: 

Initialization (__init__): Creates an instance of the InMemoryFileSystem class.
 Initializes the root directory (self.root) and sets the current directory (self.current_directory) to the root directory.

mkdir(name): Creates a new directory with the specified name in the current directory.
 Adds a new directory using the current directory's add_entry method.

cd(path): Changes the current directory to the specified path.
 If the path is "/",  the current directory is set to the root directory.
 If the path starts with '/', the directory is searched using the path  from the root directory.
 Otherwise, directories are searched based on the path starting from the current directory.

ls(path="."): Lists the contents of the specified directory path.
 If no path is specified, the current directory is used by default.
 Call the list_entries method on the target directory.
 grep(pattern, filename): Search the contents of a file for the specified pattern.
 If the target file exists, call the grep method on the file.

cat(filename): Display the contents of the file.
 If the target file exists, call the display_contents method of the file.

touch(filename): Creates a new empty file with the specified name in the current directory.
 Adds a new file using the current directory's add_entry method.
 echo(text, filename): Writes the specified text to the file.
 If the file exists, call the target file's write_text method.

mv(source path, destination path): Moves a file or directory from the source path to the destination path.
 Use the add_entry method to add an entry to the target directory and remove it from the source directory.
 
cp(source_path, destination_path="."): Copies a file or directory from a source path to a destination path.
 Creates a new entry with the same content and name as the source entry in the target directory.

rm(path): Removes the file or directory specified by  path.
 Removes an entry using the current directory's remove_entry method.

Directory class: 
Initialization (__init__): Creates an instance of the Directory class with the specified name.
 Initializes an empty list (self.entries) to store entries (files and subdirectories).

add_entry(entry): Adds a file or directory entry to the entry list.

Remove_entry(entry): Removes a file or directory entry from the entry list.

find_entry_by_path(path): Finds an entry (file or subdirectory) in the specified path.
 Handle special cases such as ".." to move to  parent directory.

find_directory_by_path(path): Finds subdirectories based on the specified path.

find_entry_by_name(name): Finds an entry (file or subdirectory) using the specified name.

list_entries(): List the names of all entries in a directory.

Class File: Initialization (__init__): Creates an instance of the File class with the specified name.
 Initializes an empty string (self.contents) to store the contents of the file.

display_contents(): Displays the contents of a file.

write_text(text): Writes the specified text to a file.

grep(pattern): Search the contents of a file for the specified pattern.
 Print the line number and  line where the pattern is found.

clone(): Creates a new instance of the File class with the same name and contents as the original file.
 
Example usage: 
 Create an instance of InMemoryFileSystem (fs).
 Perform various operations on the in-memory file system, including: B.
 Create directories and files, move directories, and edit file contents.
 This in-memory file system example provides a basic representation of a file system.


