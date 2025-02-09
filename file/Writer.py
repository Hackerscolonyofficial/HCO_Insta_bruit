import time

def writer(text="No text. Please enter the text!", delay=0.05):
    for word in text:
        print(word, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == "__main__":
    writer()