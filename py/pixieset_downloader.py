import urllib.request
import os
import time
import sys

'''
    Usage in command line:
    >pixieset_downloader.py date name
    Example:
    >pixieset_downloader.py 19-01-14 serenity
    
    DOCS:
        SRC: path to the source file.
    !!! !!! !!! You need to manually add links to the SRC file.
            Use Firefox, ALT + T + I, select all media and paste it into SRC file.
        STRS: dictionary of string messages.
        ASSETS: list of unnecessary links that will be removed from the source list.
        strings(s): returns a select string from STRS dictionary to print out information.
        start(): starts the whole process, need 2 arguments from the command line.
            date: first command line argument, suggested input YY-MM-DD
            set_name: second command line argument, name of the set
            path: current working directory + \sets\date-set_name\
                this is where the images will be downloaded
            links: temporary list of links taken from SRC
            new_links: list of links with a replaced URL for the high resolution image.
                note "medium" might need to be something else.
        archive_links(path): moves SRC to the path along with the downloaded images.
            creates a new SRC file in its place. 
            name: SRC file will be renamed to this at path
            var: a variation value in case there's a copy of the archive from before.
        get_opener(): user-agent
        download_images(links, path): downloads images from the list of new_links to the path.
            total_time: to keep the track of all time that has passed downloading.
            name: splits the URL to get the file name
            start: beginning time of the download
            urllib.request.urlretrieve(): download link to path + name
            end: ending time of the download
            passed: time passed for one image download.
'''
SRC = r"source.txt"
STRS = {
    "err_args": "2 arguments are needed. Example:\npixieset_downloader.py 19-01-14 serenity",
    "err_io": f"I/O ERROR: {SRC} is not found or inaccessible.",
    "down": "Downloading %s.",
    "comp": "Complete. Took %.2f seconds.",
    "all_comp": "---\nDownloading %d images took %.2f seconds to complete.",
}
ASSETS = [
    "https://static.pixieset.com/favicon.ico",
    "https://assets.pixieset.com/images/site/image-protect.gif",
    "https://assets.pixieset.com/images/site/cover-arrow.png",
]

def strings(s):
    return STRS.get(s)

def start():
    if len(sys.argv) == 3:
        date = sys.argv[1]
        set_name = sys.argv[2]
        path = os.getcwd() + f"\\sets\\{date}--{set_name}\\"
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except NotADirectoryError as e:
            print(f"NotADirectoryError: {e}")
            return
        except OSError as e:
            print(f"OSError: {e}")
            return
        try:
            links = open(SRC).read().split('\n')
        except IOError:
            print(strings("err_io"))
            return
        for link in ASSETS:
            try:
                links.remove(link)
            except:
                pass
        new_links = []
        for link in links:
            new_links.append(link.replace("medium", "xxlarge"))
        archive_links(path)
        download_images(new_links, path)
    else:
        print(strings("err_args"))

def archive_links(path):
    name = "_Archive-%s.txt" % path.split('\\')[-2]
    var = 1
    while os.path.isfile(path + name):
        name = name.split(".")[-2]
        try:
            name = name.split("+")[-2]
        except:
            pass
        name += f"+{var}.txt"
        var += 1
    os.rename(SRC, path + name)
    open(SRC, 'a').close()

def get_opener():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')]
    urllib.request.install_opener(opener)

def download_images(links, path):
    total_time = 0
    get_opener()
    for link in links:
        name = link.split('/')[-1]
        print(strings("down") % link)
        start = time.time()
        urllib.request.urlretrieve(link, path + name)
        end = time.time()
        passed = end - start
        total_time += passed
        print(strings("comp") % passed)
    print(strings("all_comp") % (len(links), total_time))


if __name__ == '__main__':
    start()
