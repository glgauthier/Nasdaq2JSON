# can pull a csv of all stocks from here https://www.nasdaq.com/screening/company-list.aspx
# the above sends a GET request to the following
# https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download
import json,csv,urllib2,os


def getData(name,url):
    if not os.path.exists("data"):
        os.mkdir("data")
    response = urllib2.urlopen(url)

    f = open("data/"+name+".csv", "w")
    f.write(response.read().replace(",\r",""))
    f.close()

    csvfile = open("data/"+name+'.csv', 'r')
    jsonfile = open("data/"+name+'.json', 'w')
    fields = ("Symbol","Name","LastSale","MarketCap","IPOyear","Sector","Industry","SummaryQuote")
    reader = csv.DictReader( csvfile, fields)

    rows = list(reader)
    jsonfile.write("[")
    for i,row in enumerate(rows):
        if("Sector" in row["Sector"]):
            continue

        json.dump(row, jsonfile)
        if(i < len(rows)-1):
            jsonfile.write(',\n')
        else:
            jsonfile.write('\n]')
            
getData("NASDAQ",'https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nasdaq&render=download')
getData("AMEX","https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=amex&render=download")
getData("NYSE","https://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchange=nyse&render=download")
    