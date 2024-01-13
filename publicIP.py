import requests

def get_ip():
    try:
        
        response = requests.get('https://api64.ipify.org?format=json')
        data = response.json()
        public_ip = data['ip']
        return public_ip
    except Exception as e:
        #print(f"Error: {e}")
        print("error"+e)
        return None

if __name__ == "__main__":
    public_ip = get_ip()

    if public_ip:
        print(f"here is Public IP Address: {public_ip}")
    else:
        print("Failed to load public IP address")
