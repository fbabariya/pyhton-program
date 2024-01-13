import uuid

def mac_address():
    try:
        
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(2,7)][::-1])
        return mac_address
    except Exception as e:
        print(f"Error: {e}")
        #print("error"+e)
        return None

if __name__ == "__main__":
    fin_mac_address = mac_address()

    if fin_mac_address:
        #print(f"MAC Address: {fin_mac_address}")
        print("MAC address:"+str(fin_mac_address))
    else:
        print("Failed to retrieve MAC address.")
