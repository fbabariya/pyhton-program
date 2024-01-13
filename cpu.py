import platform
import cpuinfo

def cpu_model():
    try:

        cpu_info = cpuinfo.cpu_info()
        print(cpu_info)
        model = cpu_info["brand_raw"]
        return model
    except Exception as e:
        print(f"Error: {e}")
        #print("error"+e)
        return None

if __name__ == "__main__":
    fin_cpu_model = cpu_model()

    if fin_cpu_model:
        print(f"your CPU Model is: {fin_cpu_model}")
        #print("your CPU Model is: "+fin_cpu_model)
    else:
        print("Failed to load CPU model.")
