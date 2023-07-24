import requests
import secrets



def main():
    payload = {"access_key": secrets.API_KEY}

    response = requests.get(f"http://api.exchangeratesapi.io/v1/latest",
                            params=payload)
    if response.status_code== 200:
        print('Error occured!')
        return
    
    
    print(response.status_code)
    print(response.headers['Content-Type'])
    print(type(response.text))
    response_dictionary = response.json()

    success = response_dictionary['success']
    timestamp = response_dictionary['timestamp']
    base = response_dictionary['base']
    date = response_dictionary['date']
    KRW = response_dictionary['rates']['KRW']
    AUD = response_dictionary['rates']['AUD']
    USD = response_dictionary['rates']['USD']


    print(f"성공 코드: {success}")
    print(f"timestamp: {timestamp}")
    print(f"base: {base}")
    print(f"date: {date}")
    print(f"KRW: {KRW}")
    print(f"AUD: {AUD}")
    print(f"USD: {USD}")

if __name__ == "__main__":
    main()