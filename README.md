# Web Scraper GUI

Une petite application Python moderne pour récupérer le contenu HTML d'une page web, l'afficher, extraire les informations principales (title, meta, titres...), et sauvegarder le résultat dans un fichier.  
Interface graphique **dark mode** avec boutons stylés grâce à **CustomTkinter**.

## Fonctionnalités

- Saisie d'une URL à scraper
- Récupération du code HTML de la page
- Aperçu du contenu récupéré (HTML brut)
- Extraction rapide :
  - Titre de la page (`<title>`)
  - Meta description et mots-clés
  - Titres (`<h1>`, `<h2>`, `<h3>`)
- Sauvegarde du contenu dans un fichier `.html`
- Design moderne et responsive (coins arrondis, hover, dark mode)

## Prérequis

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter)

### Installation des dépendances

Créer (optionnel) et activer un environnement virtuel, puis :

```bash
pip install -r requirements.txt
````

**Ou manuellement :**

```bash
pip install requests beautifulsoup4 customtkinter
```

## Utilisation

1. **Lance l'application :**

   ```bash
   python scraper_gui.py
   ```

2. **Entre l'URL** à scraper dans le champ dédié.

3. Clique sur **Scraper** pour voir le HTML brut.

4. Clique sur **Extraire infos (titres, meta)** pour un résumé des informations principales.

5. Clique sur **Sauvegarder dans un fichier** pour enregistrer le résultat.

## Création d'un exécutable (.exe)

Pour générer un exécutable Windows :

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole --icon=web.ico scraper_gui.py
```

L'exécutable sera disponible dans le dossier `dist/`.

## Limitations

* Certains sites protègent leur contenu (ex: Cloudflare, CAPTCHA, JavaScript…) et peuvent retourner une erreur 403 ou autre.
* Le scraping doit respecter les règles du site ciblé (robots.txt, CGU...).

## Astuces

* Pour scraper des sites protégés, un header `User-Agent` est déjà inclus dans le script.
* Pour scraper des pages dynamiques (JavaScript), utilisez Selenium ou Playwright.

---

## Auteur

**Mardovitch Dzmitryi**

Si vous avez des questions ou des propositions, vous pouvez me contacter :

* Email : [dmardovitch@gmail.com](mailto:dmardovitch@gmail.com)
* LinkedIn : https://www.linkedin.com/in/dzmitryi-mardovitch/
* GitHub : https://github.com/DzmitryiKorjik


