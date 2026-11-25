import os

LINE = "My phone dies at 4 p.m. daily, like clockwork \u2014 the only thing in my life with a reliable routine is the thing that quits on me."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
