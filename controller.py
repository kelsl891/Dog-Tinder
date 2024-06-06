import requests

def get_doggy_image(breed):
    # Define the API endpoint URL
    url = 'https://dog.ceo/api/breed/'+breed+'/images/random'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts["message"]
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:

        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None
    

def get_random_dog():
    # Define the API endpoint URL
    url = 'https://dog.ceo/api/breeds/images/random'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts["message"]
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:

        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None