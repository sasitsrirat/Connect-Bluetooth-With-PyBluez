import bluetooth

def discover_nearby_devices():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    return nearby_devices

def main():
    print("Scanning for nearby Bluetooth devices...")
    devices = discover_nearby_devices()
    
    if not devices:
        print("No Bluetooth devices found nearby.")
    else:
        print("Found the following devices:")
        for addr, name in devices:
            print(f"Device Name: {name} (Address: {addr})")

if __name__ == "__main__":
    main()
