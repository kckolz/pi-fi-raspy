import bluetooth

print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=2, lookup_names=True,
                                            lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
