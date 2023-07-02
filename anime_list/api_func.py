import requests

#keeping these modular on purpose for now
#might come back and add functionality to directly input an id skipping the search

#initial api call to get the id, necessary for all others when adding a series
def get_id(title):
    title = title.replace(" ", "%20")
    try: 
        url = f"https://myanimelist.p.rapidapi.com/anime/search/{title}"
        headers = {
	        "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	        "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data[0]["myanimelist_id"]
    except:
        return "Series not found, please try again."


#synopsis function
def get_synopsis(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["synopsis"]

#episodes function
def get_episodes(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["information"]["episodes"]

#rank function
def get_rank(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["statistics"]["ranked"]


#rating function
def get_rating(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["information"]["rating"]

#aired function
def get_airdates(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["information"]["aired"]

#status function
def get_status(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["information"]["status"]

#score function
def get_score(anime_id):
    url = f"https://myanimelist.p.rapidapi.com/anime/{anime_id}"
    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data["statistics"]["score"]

#top upcoming anime for home page
#CURRENTLY DEFUNCT, MAY COME BACK AND ADD FUNCTIONALITY
def top_upcoming(index):
    url = "https://myanimelist.p.rapidapi.com/anime/top/upcoming"

    headers = {
	    "X-RapidAPI-Key": "b8bd7899e7msh07e0ad2abe72116p1374c6jsndbe2e976064c",
	    "X-RapidAPI-Host": "myanimelist.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    return data[index]["title"] + ": " + data[index]["aired_on"]