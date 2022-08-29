# Alza-Price-Guarantee
Alza.cz Price Guarantee even for unsupported competitor eshops which are not part of 'relevant competition'.

Alza.cz Garance nejlepší ceny i pro nepodporované eshopy, které nejsou součástí 'relevantní konkurence'.

![image](https://user-images.githubusercontent.com/13543580/187199442-d3f2e0c9-ba73-4091-9e0b-bf483ce218f3.png)

When using Price Guarantee you can only have the price matched to a product sold by 'relevant competition' which are preselected eshops Alza deems as relevant. This allows you to use any eshop you want.

Při použití Garance nejlepší ceny je cena garantována jen pro produkty prodávané 'relevantní konkurencí', což jsou vybrané eshopy, které Alza považuje za relevantní. Tento script vám umožní použít Garanci nejlepší ceny pro jakýkoli eshop.

-----------

- Clone repo
- `pip install -r requirements.txt`

Populate these four variables and run the script. / Vyplň tyto čtyři proměnné a spusť script.

```
my_email = "my@email.cz"
alza_url = "https://www.alza.cz/sport/big-boy-arasidovy-krem-gastro-1-kg-d5814312.htm"
competition_url = "https://www.fitness007.cz/big-boy-arasidovy-krem-1000-g-jemny/"
i_can_code = True
```

-----------

> __Note__
SET UP TO WORK ONLY FOR ALZA.CZ / NASTAVENO JEN PRO ALZA.CZ

For other countries `price_guarantee_url` would have to be updated, as well as `data['country']` and possibly `data['pgrik']`.

Pro ostatní země bude potřeba upravit `price_guarantee_url`, `data['country']` a možná i `data['pgrik']`.

-----------

> __Warning__
> DISCLAIMER:

This was created for illustration purposes only. Not intended to actually get a lower price.

Vytvořeno jen pro ilustrační účely. Není určeno ke skutečnému získání nižší ceny.
