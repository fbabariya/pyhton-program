import ctypes

def resolution():
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize

if __name__ == "__main__":
    final_resolution =resolution()
    print(f"Screen Resolution: {final_resolution[0]} x {final_resolution[1]} pixels")
   