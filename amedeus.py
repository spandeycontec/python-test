from amadeus import Client, ResponseError

amadeus = Client(
    client_id='rwNwBBAAO2Pnb6xpaWlTCdE653Gtkvuv',
    client_secret='pCdaGggama2iG9p8'
)

try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='MAD',
        destinationLocationCode='ATH',
        departureDate='2024-11-01',
        max=1,
        adults=1)
    print(response.data)
except ResponseError as error:
    print(error)