import requests

for year in range(1977, 2023):
    url = f'https://www.berkshirehathaway.com/letters/{year}ltr.pdf'
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f'{year}ltr.pdf', 'wb') as f:
            f.write(response.content)
            print(f'Successfully saved {year}ltr.pdf')
    else:
        print(f'Error: Could not download {year}ltr.pdf')
