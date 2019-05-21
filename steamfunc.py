
def get_reviews(appid, start_offset=0, fil='updated', review_type='all'):
    url = 'https://store.steampowered.com'
    reviews = '/appreviews/'
    p = {'day_range':'9223372036854775807', 
         'start_offset':start_offset, 
         'language':'english', 
         'filter':fil, 
         'review_type':review_type,
         'purchase_type':'all'}
    r = requests.get(url+reviews+str(appid)+'?json=1?', params=p).json()
    return r

def get_review_content(df):
    return [df['reviews'][i]['review'] for i in range(len(df['reviews']))]

def get_hrs_playtime(df):
    time = [df['reviews'][i]['author']['playtime_forever'] for i in range(len(df['reviews']))]
    hours = [round(time[j]/60,2) for j in range(len(time))]
    return hours

def get_voted(df):
    return [df['reviews'][i]['voted_up'] for i in range(len(reviews['reviews']))]

def epoch_convert(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))

def get_steamlist():
    return requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v0002/').json()

def get_appid(name, games):
    for i in range(len(games['name'])):
        if games['name'][i].title() == name.title():
            return games['appid'][i]
    return "Did not find"

def get_gamename(appid, games):
    for i in range(len(games['name'])):
        if games['appid'][i] == appid:
            return games['name'][i]
    return "Did not find"

def get_game_info(appid):
    url = 'https://store.steampowered.com'
    ids = str(appid)
    r = requests.get(url+'/api/appdetails?appids='+ids).json()
    return r

