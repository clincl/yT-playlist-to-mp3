from googleapiclient.discovery import build
import csv
import config
#REQUIRED INFO
#API KEY
api_key = config.api_key
#PLAYLIST ID
pId = config.pId
#CSV FILE
CSV_FILE = 'youtube_links.csv'

#Connect to Youtube API and get a response from request
yt = build ('youtube','v3',developerKey = api_key)
req = yt.playlistItems().list(
    part = 'snippet',
    maxResults = 1,
    playlistId = pId
)
res = req.execute()

#Reset the response to the next page given a response
def reset(res):
    #print('\nnext token')
    #print(res['nextPageToken'])
    req = yt.playlistItems().list(
    part = 'snippet',
    pageToken = res['nextPageToken'],
    maxResults = 1,
    playlistId = pId
    )
    res = req.execute()
    return res

#Clear file
def clear():
    with open(CSV_FILE,'w') as f:
        w = csv.writer(f)
        f.close()
def write(res):
    with open(CSV_FILE, 'a', newline = '', encoding = 'utf8') as f:
        w = csv.writer(f)
        for vid in res['items']:
            print(vid['snippet']['title'])
            #print(vid['snippet']['resourceId']['videoId'])
            w.writerow([vid['snippet']['title'], vid['snippet']['resourceId']['videoId']])
        if 'nextPageToken' in res:
            res = reset(res)
            f.close()
            write(res)

#Main
def main():
    clear() #clear csv
    write(res) #write to csv
main()