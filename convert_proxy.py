# convert_proxy.py
import re

def convert(input_file, output_file):
    with open(input_file, "r") as src, open(output_file, "w") as out:
        for line in src:
            clean = re.sub(r"http[s]?://", "", line.strip())  # remove http:// or https://
            clean = clean.rstrip(",")  # remove trailing comma
            if clean:
                out.write(clean + "\n")
    print(f"[+] Converted proxies saved to: {output_file}")


# Example Usage:
# convert("raw_proxy.txt", "clean_proxy.txt")
