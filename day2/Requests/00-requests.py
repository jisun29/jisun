import requests

def main():
    response = requests.get("http://www.google.com/dldsfijg")
    print(response)
    print(response.status_code)
    print(type(response.headers['Content-Type']))
    print("Content:", response.text)

if __name__== "__main__":
    main()

