import os

def main():
    for i in range(1, int(os.environ.get('NUM_FRAMES')) + 1):
        with open(f"graphics/frame_{i:04d}.grit", "w") as f:
            f.write("-gb -gB16")


if __name__ == "__main__":
    main()
