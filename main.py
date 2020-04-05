import sys
sys.path.insert(1, 'src')
from src.gen_key import Pass_key
from src.colors1 import get_colors
def main():
    try:
        Pass_key.run()
    except KeyboardInterrupt as ky:
        print(get_colors.yellow()+get_colors.red() + "\n[!] CTRL+C Detected \n"+get_colors.cyan()+"Thanks For Usage :)")
if __name__ == "__main__":
    main()                
