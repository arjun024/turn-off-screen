#include <CoreFoundation/CoreFoundation.h>
#include <IOKit/IOKitLib.h>

/* Returns 0 on success and 1 on failure. */
int main(void)
{
    io_registry_entry_t reg = IORegistryEntryFromPath(kIOMasterPortDefault, "IOService:/IOResources/IODisplayWrangler");
    if (reg) {
                IORegistryEntrySetCFProperty(reg, CFSTR("IORequestIdle"), kCFBooleanTrue);
                IOObjectRelease(reg);
        } else {
                return 1;
        }
        return 0;
}
