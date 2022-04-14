from datetime import datetime
import sys

def logger(msg: str):
    # print time and message
    print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}] {msg}')
    
def get_timestr_mil_sec() -> str:
    # get milliseconds from datetime 
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    
def check_command(num_args, correct_command, exit_code=1):
    if len(sys.argv) != num_args:
        logger(msg=f"🔥Not acceptable🔥 use {correct_command}")
        sys.exit(exit_code)

if __name__ == '__main__':
    # test
    logger('Hello World')
    