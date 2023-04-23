import random

def handle_response(message) -> str:
    p_message = message.lower()


    if p_message =='hello':
        return 'hey there'
    

    if p_message == 'roll':
        return str(random.randint(1,6))
    
    
    if p_message==  'games':
        return 'https://store.epicgames.com/en-US/'
    

    if p_message == 'help':
        return "`this is a help message that you can modify.`"
    

    if p_message == 'game on sale':
        return 'https://store.epicgames.com/en-US/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierDiscouted&category=Game&count=40&start=0'
    

    if p_message == 'free games':
        return 'https://store.epicgames.com/en-US/browse?sortBy=releaseDate&sortDir=DESC&priceTier=tierFree&category=Game&count=40&start=0'
    

    if p_message == 'action games':
        return 'https://store.epicgames.com/en-US/browse?sortBy=releaseDate&sortDir=DESC&tag=Action&priceTier=tierFree&category=Game&count=40&start=0'
    

    if p_message == 'racing games':
        return 'https://store.epicgames.com/en-US/browse?sortBy=releaseDate&sortDir=DESC&tag=Action%7CRacing&priceTier=tierFree&category=Game&count=40&start=0'
    

    if p_message =='fps games':
        return 'https://store.epicgames.com/en-US/browse?sortBy=releaseDate&sortDir=DESC&tag=First%20Person&category=Game&count=40&start=0'
    

