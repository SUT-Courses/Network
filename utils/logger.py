from datetime import datetime

def logger(msg: str):
    # print time and message
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] {msg}')
    
def get_timestr_mil_sec() -> str:
    # get milliseconds from datetime 
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
    

if __name__ == '__main__':
    # test
    logger('Hello World')
    