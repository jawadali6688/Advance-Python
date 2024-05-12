import requests

def fetch_api():
    url = "https://api.freeapi.app/api/v1/todos?query=reactjs&complete=false"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] or "data" in data:
        username = data["message"]
        print(username)
        return username, data
      
    else:
        raise Exception("Failed to fetch")
    
    
def main():
   try:
        username, data = fetch_api()
        print(username, data)
   except Exception as e:
       print(e)
       
if __name__ == "__main__":
    print("khan")
    main()