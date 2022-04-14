from datetime import datetime

def logger(msg: str):
    # print time and message
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] {msg}')
    
    
if __name__ == '__main__':
    # test
    logger('Hello World')
    