#include "frame_0001.h"
#include "tonc_core.h"
#include "tonc_memdef.h"
#include "tonc_memmap.h"
#include "tonc_types.h"
#include <tonc.h>
#include "frames.h"

void set_frame(u32 frame_no) {
    memcpy32(vid_mem, bitmap_arr[frame_no - 1], frame_0001BitmapLen / sizeof(u32));
}

int main() {

    // Init interrupts and VBlank irq.
	irq_init(NULL);
	irq_add(II_VBLANK, NULL);

    REG_DISPCNT = DCNT_MODE3 | DCNT_BG2;

    u32 wait_timer = 0;
    u32 ii = 0;

    while (true) {
        VBlankIntrWait();
        if (wait_timer % 2 == 0) {
                set_frame(ii);
                ii++;
        }
        wait_timer++;
        if (ii == bitmap_arr_len) {
            ii = 0;
        }
    }

    return 0;
}
