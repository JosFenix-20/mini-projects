def extraer_titulares(soup, selector="h2"):
    if not soup:
        return []

    elementos = soup.select(selector)
    titulares = [el.get_text(strip=True) for el in elementos if el.get_text(strip=True)]
    return titulares