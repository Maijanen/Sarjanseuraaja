# Harjoitustyö: Sarjanseuraaja-tietokantasovellus
## Syksy 2019
Maija Huotari

# Sarjanseuraaja
 Sovellus sarjojen edistymisen hallintaan ja muistamiseen

 Sovelluksen tehtävänä on hallinnoida hakutoimintoineen ja edistymistietoineen listausta sellaisista televisio- tai nettisarjoista, joita käyttäjä seuraa, on seurannut tai aikoo tulevaisuudessa vielä jonain päivänä seurata.

 Käyttäjät kirjautuvat sisään sovellukseen ja saavat listauksen siitä, mitä sarjoja kyseisellä käyttäjällä on sillä hetkellä kesken. Editymistiedot päivitetään sovellukseen käsin. Hakutoimintoja käyttämällä voi myös etsiä jo kokonaan katsottuja tai päättyneitä sarjoja tai muiden käyttäjien tietokantaan lisäämiä sarjoja. Edistymistietojen lisäksi käyttäjä voi antaa sarjalle oman arvosanan ja tämäkin tieto on käyttäjäkohtainen ja arvosanaa voidaan käyttää hakukriteerinä. Muiden käyttäjien edistymistietoja tai arvosteluja ei pääse katselemaan ilman pääkäyttäjän oikeuksia.
  
 Jokainen käyttäjä voi myös lisätä tietokantaan uusia sarjoja. Sarjaa voi muokata jälkikäteen tai poistaa sovelluksen tietokannasta vain pääkäyttäjä, mutta jokainen peruskäyttäjä voi poistaa sarjan omalta katselulistaltaan. Sarjaa tietokantaan lisättäessä sille annetaan tieto nimen, ilmestymisvuoden, genrejen ja kuvauksen lisäksi myös palveluntarjoajista, eli siitä mitä kautta sarjaa voi seurata. Genrejä ja palveluntarjoajia hallinnoi vain pääkäyttäjä ja ne lisätään valmiiksi suoraan tietokantaan, sillä niitä käytetään myös hakukriteereinä ja tästä syystä määrää ja kirjoitusasua tulee kontrolloida.

 ## Toimintoja:

   * Kirjautuminen
   * Sarjan lisääminen tietokantaan
   * Sarjan poistaminen tietokannasta pääkäyttäjäoikeuksin
   * Sarja lisääminen omalle katselulistalle
   * Sarjan poistaminen katselulistalta
   * Omalla katselulistalla olevan sarjan arvostelu
   * Omalla katselulistalla olevan sarjan edistymistietojen päivittäminen
   * Sarjojen hakeminen vapaasanahaulla
   * Sarjojen hakeminen genren tai palveluntarjoajan perusteella
   * Katselulistan haku/listaustoiminnot käyttäjäkohtaisten attribuuttien (vaihe, arvosana) perusteella
   * Katselulistan haku/listaustoiminnot vapaasanahaulla tai genren tai palveluntarjoajan perusteella


## Tietokantakaavio:
 

![Tietokantakaavio](https://github.com/Maijanen/Sarjaseuraaja/blob/master/documentation/Tietokantakaavio.png "Tietokantakaavio")


## Käyttötapauksia:

### Rekisteröityminen

Voin rekisteröityä palveluun käyttäjäksi.

### Kirjautuminen

Voin kirjautua sisään palveluun antamalla käyttäjätunnukseni ja salasanani.

### Sarjan lisääminen tietokantaan

Kirjautuneena käyttäjänä voin lisätä sarjan tietokantaan.

### Sarjan tietojen muokkaaminen

Kirjautuneena käyttäjänä voin muokata tietokannassa olevan sarjan tietoja.

### Sarjojen listaus

Kirjautuneena käyttäjänä voin selata listaa kaikista tietokannan sarjoista

### Sarjojen hakeminen tietokannasta

Kirjautuneena käyttäjänä voin hakea sarjoja tietokannasta erilaisilla hakuehdoilla

### Sarjan lisääminen omalle katselulistalle

Kirjautuneena käyttäjänä voin lisätä sarjan omalle katselulistalle

### Sarjan poistaminen omalta katselulistalta

Kirjautuneena käyttäjänä voin poistaa sarjan omalta katselulistalta

### Katselulistalla olevan sarjan tietojen päivittäminen

Kirjautuneena käyttäjänä voin muokata ja päivittää omalla listalla olevan sarjan katselutietoja ja arvostelua.

### Sarjan hakeminen omalta katselulistalta

Kirjautuneena käyttäjänä voin hakea omalta katselulistaltani sarjoja erilaisilla hakuehdoilla.

### Sarjan poistaminen tietokannasta

Kirjautuneena pääkäyttäjänä voin poistaa sarjan tietokannasta.

### Palveluntarjoajan lisääminen, muokkaaminen ja poistaminen

Kirjautuneena pääkäyttäjänä voin lisätä, poistaa ja muokata palveluntarjoajia tietokannassa.

### Genren lisääminen, muokkaaminen ja poistaminen

Kirjautuneena pääkäyttäjänä voin lisätä, poistaa ja muokata genrejä tietokannassa.
