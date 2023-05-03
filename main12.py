from parser import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/news/', 'new.txt')
    pars.run()


if __name__ == '__main__':
    main()
