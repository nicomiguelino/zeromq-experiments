import logging

def main():
    logging.info('Hello World')
    print('Hello World, Again')

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.info(e)
