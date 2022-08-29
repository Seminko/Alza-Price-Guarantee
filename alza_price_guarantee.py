# %%
"IMPORTS"

import requests
import json
import re
from user_agent import generate_user_agent
from urllib.parse import urlparse

# %%
"PŘED SPUŠTĚNÍM VYPLNIT / FILL OUT BEFORE RUNNING"

# Vyplň email, na který se má odeslat odpověď Alzy / Fill out email you want Alza's response sent to
my_email = ""

# Vyplň URL Alza produktu / Fill out Alza product URL
alza_url = "https://www.alza.cz/sport/big-boy-arasidovy-krem-gastro-1-kg-d5814312.htm"

# Vyplň URL produktu s lepší cenou / Fill out competition better price product URL
competition_url = "https://www.fitness007.cz/big-boy-arasidovy-krem-1000-g-jemny/"

# Umíš python? Jestli ne, změň na 'i_can_code = False' - v případě problému se vypíšou čitelné instrukce / poznámky v češtině.
# Do you know python? If not, change to 'i_can_code = False' - script will generate readable instruction / notes in case of errors.
i_can_code = True


# %%
"FUNCTIONS"
def send_competition_request(my_email, alza_url, competition_url, i_can_code = True):
    """
    EN: prepares and sends request for price check to alza.cz eshop even for unsupported competitor eshops
    CZ: připraví a pošle požadavek na kontrolu ceny do eshopu alza.cz, a to i pro nepodporované konkurenční eshopy
    """
    if my_email == "":
        raise Exception("Vyplň 'my_email' / Fill out 'my_email'")
        
    if alza_url == "":
        raise Exception("Vyplň 'alza_url' / Fill out 'alza_url'")
        
    if competition_url == "":
        raise Exception("Vyplň 'competition_url' / Fill out 'competition_url'")

        
    timeout = 30
    
    if not i_can_code:
        try:
            alza_product_id = re.search("\d+(?=\.html?$)", alza_url)[0]
        except:
            raise Exception("Z 'alza_url' nejde vytáhnout ID produktu. Zkontroluj 'alza_url' / Cannot get product ID from 'alza_url'.")
    else:
        alza_product_id = re.search("\d+(?=\.html?$)", alza_url)[0]

    price_guarantee_url = f"https://www.alza.cz/api/catalog/v1/products/{str(alza_product_id)}/priceGuarantee/lowerPrice"
    
    d = urlparse(competition_url).netloc
    if d == "":
        domain_error = "Domain cannot be parsed" if i_can_code else "Doménu nelze extrahovat z 'alza_url'. Zkontroluj, jestli je 'alza_url' správně. \
                                                                   / Domain can't be extracted from 'alza_url'. Check if 'alza_url' is correct."
        raise Exception(domain_error)
    competition_domain = '.'.join(d.split('.')[-2:])
    
    data = {
        "competitionEshop":[competition_domain],
        "competitionLink":competition_url,
        "userEmail":my_email,
        "country":"CZ",
        "pgrik":"mAAI"
    }
    
    headers = {
        "user-agent": generate_user_agent(os='win', navigator='chrome'),
        "origin": "https://www.alza.cz",
        "referer": alza_url,
    }
    
    if not i_can_code:
        try:
            response = requests.post(price_guarantee_url, data=data, headers=headers, timeout=timeout)
        except:
            raise Exception("Posláni se nezdařilo. Zkus to znovu. / Sending failed. Try again.")
    else:
        response = requests.post(price_guarantee_url, data=data, headers=headers, timeout=timeout)
        
    if response.status_code != 200:
        status_code_error = f"HTTP status: {str(response.status_code)}" if i_can_code else "Špatný status. Něco je špatně NEBO alza změnila systém. Zkus to znovu. \
                                                                                            Incorrect status. Something is wrong OR alza changed its system. Try again."
        raise Exception(status_code_error)
    
    if not i_can_code:
        try:
            o_json = json.loads(response.text)
        except:
            raise Exception("Špatná odpověď. Nedá se svítit.")
    else:
        o_json = json.loads(response.text)
        
    if o_json["title"].lower() != "žádost odeslána":
        json_error = f"Unexpected response, check manually:\n{o_json}" if i_can_code else f"Nečekaná odpověď. Zkontroluj jestli dává smysl, např 'title:Žádost odeslána'. \
                                                                                            Unexpected response. Check if it makes sense, ie: 'title:Žádost odeslána':\n{o_json}"
        raise Exception(json_error)
        
    print(o_json["title"])


send_competition_request(my_email, alza_url, competition_url, i_can_code)
