import requests
import secrets


def main():
    payload = {"access_key": secrets.API_KEY}

    response = requests.get(f"http://api.exchangeratesapi.io/v1/latest",
                            params=payload)
    payload = {"access_key": secrets.API_KEY}
    
    print(response.status_code)
    print(response.headers['Content-Type'])

    #print(response.text)
    #'{"key": "value"}'
    #string JSON -> Dictionary
    print(type(response.text))

    #print(secrets.API_KEY)
    response_json = response.json()
    print(type(response_json))
    #print(response_json['success'])
    #print(response_json['timestamp'])
    """
    받은 response를 dictionary화해서
    success는 뭐다
    timestamp는 몇이다
    base KRW 기준으로 달러는 얼마다
    """

    
  
    
if __name__ == "__main__":
    main()