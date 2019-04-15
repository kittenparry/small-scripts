# Small Scripts
Stuff I use around separated by file extensions* to different directories.

### [Batch](bat)
- `archive_downloader` - An attempt on moving downloads to archive folders (incomplete)
- `del` - Deletes unnecessary files from torrents in %dl%:\Archive\porn
- `logs_archive` - Copies myLogs.txt to Logs/ with dates
- `logs_backup` - Copies myLogs.txt and Logs/ to different partitions (this copies to latest_logs/)
- `logs_backup_with_dates` - Copies myLogs.txt and Logs/ to different partitions with dates (this copies to archived_logs/)
- `move` - Move different types of files into appropriate folders in general downloads directory
- `robocopy_x` - General back up scripts
- `rpa_extractor` - RPA Extractor command with a for loop to help the extraction of all files in a path (uses an external program for the extraction, this is only a loop)
- `search_everything_backup` - Copies Search Everything run and search history to dated folders in Google Drive
- `setup_archive` - Archive folder setup in different drives
- `setup_downloads` - Torrent downloads folder setup in different drives
- `sg_archive` - Zips SuicideGirls folders with appropriate names and moves zips to the Google Drive folder, then moves folders to the parent directory

### CSS
Custom styling for certain websites.

### HTML
- `ig_download_button` - Design of the button now used with [this user script](https://github.com/kittenparry/userscripts/tree/master/instagram_image_viewer)

### JSON
- `vscode_settings` - What it says

### Powershell
- `tree` - Creates a file tree for archive/downloads folders in each drive then copies them to the dated folders in Google Drive

### Python
- `7zipper` - Creates an archive with all the data in a folder, with password, encrypted file names, no compression and named after the hexadecimal value of the directory
- `pixieset_downloader` - Somewhat of a clunky but semi-automatic way of downloading images from pixieset.com
- `reader` - An attempt at creating manifest files for archive/downloads, replaced by `tree.ps1`
- `size_checker` - Prints out the number and total size of all files in a folder (not the folders)
- `word_counter` - Reads a .txt document, counts the number of words and outputs it, it's not the number of total words but rather a count of each individual word

### Python (pyw)
- `string-hex_converter` - A small GUI program to convert a string of text to hex and vice versa

### Rust
- `sensible-random-word-generator` - Generates random words based on given length and given repetition value as arguments

### Text
- `vscode_extensions` - Output of the command `code --list-extensions` (probably could be turned into a batch script)
