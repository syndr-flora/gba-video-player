import os

FRAME_COUNT = int(os.environ.get('NUM_FRAMES'))

def main():
    with open("build/frames.h", "w") as f:
        # #include's
        for i in range(1, FRAME_COUNT + 1):
                f.write(f"#include \"frame_{i:04d}.h\"\n")

        # arr of bitmap arrs
        # !!DATA SHOULD NOT GO IN A HEADER FILE!!
        # !!DON'T DO THIS!!
        f.write(f"extern const unsigned int* bitmap_arr[{FRAME_COUNT}] = {{\n")
        for i in range(1, FRAME_COUNT + 1):
            f.write(f"\tframe_{i:04d}Bitmap,\n")
        f.write("};\n")

        # arr len
        f.write(f"extern const unsigned int bitmap_arr_len = {FRAME_COUNT};")


if __name__ == "__main__":
    main()
