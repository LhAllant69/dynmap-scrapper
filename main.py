if __name__ == "__main__":
    from get_request import get_info
    from save_data import save
    from time import sleep
    from utils import read_file_content

    config = read_file_content("config.txt").split(" ")

    while True:
        try:
            save(get_info(config[0], config[1]))
        except:
            #I don't care what the error is I just want to try again
            pass
        sleep(30)
