import time
def dowork():
    for x  in range(1,34):
        current_progress = (x+1)/34
        update_progress_bar(current_progress)
        time.sleep(1)
    print("\ndone")



def update_progress_bar(current_progress):
    pbar_length = 40
    current_filled_length = int(pbar_length * current_progress)
    pbar = '░' * current_filled_length + ' '*(pbar_length - current_filled_length)
    print(f'|{pbar}|{current_progress*100:.2f}%',end='\r')


if __name__ == "__main__":
    dowork()