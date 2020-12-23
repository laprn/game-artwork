from igdb.wrapper import IGDBWrapper
import config

wrapper = IGDBWrapper(config.CLIENT_ID, config.ACCESS_TOKEN)

byte_array = wrapper.api_request(
    'games',
    'fields cover, name, artworks ; search "Cyberpunk 2077";'
)

cover_data = wrapper.api_request(
    'covers',
    'fields game, image_id; where id = 70754;'
)

artwork_data = wrapper.api_request(
    'artworks',
    'fields url; where id = (4940, 4941, 4942,4943,5034,5035,5036,5037,4940,5673,5674,8066,8743);'
)

print(byte_array)
print(cover_data)
print(artwork_data)