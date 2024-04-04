import time
import requests


class StashParser:
    def __init__(self, config):

        self.config = config

        self.POESESSID = config["POESESSID"]
        self.league = config["league"]
        self.realm = config["realm"]
        self.accountName = config["accountName"]
        self.tab_names = config["tab_names"]

        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': f'POESESSID={self.POESESSID}',
            'referer': f'https://www.pathofexile.com/account/view-profile/{self.accountName}/stashes',
            'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': '"123.0.2420.53"',
            'sec-ch-ua-full-version-list': '"Microsoft Edge";v="123.0.2420.53", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.59"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
            'x-requested-with': 'XMLHttpRequest'
        }
    
    def _get_tab_index(self, tab_names):

        tab_try = self._get_stash(tabIndex=0)

        return [tab['i'] for tab in tab_try['tabs'] if tab['n'] in tab_names]

    def _get_stash(self, tabs=1, tabIndex=0):

        url = "https://www.pathofexile.com/character-window/get-stash-items"
        payload = {}

        # skip system proxy
        proxies = {
            "http" : None,
            "https" : None
        }

        params = {
            "tabs" : tabs,
            "tabIndex" : tabIndex,
            "league" : self.league,
            "realm" : self.realm,
            "accountName" : self.accountName
        }

        response = requests.request("GET", url, headers=self.headers, data=payload, proxies=proxies, params=params)

        return response.json()

    def get_items(self, tab_names, filter=None):

        tab_index = self._get_tab_index(tab_names)
        time.sleep(0.5)

        items = []
        for i in tab_index:
            tmp = self._get_stash(tabIndex=i)['items']

            # TODO: filter items
            pass

            items.extend(tmp)
            time.sleep(0.5)

        return items
    
    def get_coffins(self):
        items = self.get_items(self.tab_names)

        coffins = list(filter(lambda x: x["baseType"] == "Filled Coffin", items))
        coffins = [{
            'name' : c['properties'][0]['values'][0][0],
            'level' : int(c['properties'][1]['values'][0][0]),
            'category' : c['properties'][2]['values'][0][0],
            'implicit' : c['implicitMods'][0],
        } for c in coffins]
    
        return coffins


if __name__ == "__main__":
    import json

    with open("config.json", "r") as f:
        config = json.load(f)

    parser = StashParser(config)

    print(parser.get_coffins())