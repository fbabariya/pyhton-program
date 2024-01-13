import speedtest

def checking_speed():
    speed = speedtest.Speedtest()
    
    download_speed = speed.download()
    upload_speed = speed.upload()

    print(f"Download Speed: {download_speed / 10**6:.2f} Mbps")
    print(f"Upload Speed: {upload_speed / 10**6:.2f} Mbps")

if __name__ == "__main__":
    checking_speed()
