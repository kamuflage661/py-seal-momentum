import loaddata as loaddata
import backtestsinglestock as backtestsinglestock

def main():
    data = loaddata.readTicker('kgh')
    backtestsinglestock.runBacktests(data)

if __name__ == "__main__":
    main()
