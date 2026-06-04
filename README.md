#  Katalog her (Game Database)

> **Ročníkový projekt** > 
> Školní rok: 2025/2026

---

##  Autor
* **Jméno:** Jan Lhotský
* **Třída:** IT3 P2
* **Projekt:** Ročníkový projekt – Webový katalog a databáze videoher

---

##  Popis projektu
Webová aplikace vytvořená v Pythonu za použití robustního frameworku **Django**. Projekt slouží jako přehledný katalog videoher, kde lze sledovat jednotlivé tituly, jejich autory (vydavatele) a žánrové zařazení. Aplikace plně využívá databázové vztahy (1:N a M:N) a klade důraz na validaci uživatelských vstupů a čisté uživatelské rozhraní.

### Klíčové entity projektu:
*  **Vydavatelé (Publishers)** – Evidence studií a jejich webových stránek.
*  **Kategorie (Categories)** – Žánrové zařazení her (RPG, FPS, Strategie...).
*  **Hry (Games)** – Hlavní entita obsahující detaily, rok vydání a přebal hry.

---

##  Použité technologie

| Technologie | Využití v projektu |
| :--- | :--- |
| **Python 3** | Hlavní programovací jazyk backendu |
| **Django 6.0** | Webový framework (MVC architektura, ORM, Admin) |
| **SQLite3** | Relační databáze pro ukládání dat |
| **Bootstrap 5** | Frontend framework pro responzivní design |
| **HTML5 & CSS3** | Struktura a stylování šablon |

---

##  Funkce aplikace

* **Kompletní administrace (Django Admin):** Bezpečná správa her, vydavatelů a žánrů přes vestavěné rozhraní pro správce.
* **Robustní backend validace:** Kontrola vstupních dat přímo na úrovni databázových modelů (ochrana proti záporným hodnotám u letopočtů, minimální délka popisku hry).
* **Dynamická hlavní strana:** Obsahuje počítadlo, které v reálném čase zobrazuje celkový počet her v databázi.
* **Responzivní katalog her:** Přehledný výpis všech her ve formě moderních Bootstrap karet včetně nahrávaných obrázků.
* **Detail hry:** Samostatná dynamická stránka pro každou hru s kompletními informacemi, žánrovými štítky a vazbou na vydavatele.
* **Správa médií:** Bezpečné nahrávání herních přebalů ošetřené proti nechtěnému přepisování souborů se stejným názvem na disku.

---

##  Instalační příručka

Pro zprovoznění projektu na lokálním počítači postupujte podle následujících kroků v terminálu:

### 1. Příprava prostředí
Vytvoření virtuálního prostředí Pythonu:
bash
python -m venv .venv
Bash
.venv\Scripts\activate
Instalace potřebných knihoven a závislostí:

Bash
pip install -r requirements.txt
### 2. Inicializace databáze
Generování a aplikace databázových migrací:

Bash
python manage.py makemigrations catalogue
python manage.py migrate
Načtení připravených ukázkových dat (her, žánrů a vydavatelů) z fixtures:

Bash
python manage.py loaddata catalogue/fixtures/games_data.json
Vytvoření administrátorského účtu pro přístup do /admin:

Bash
python manage.py createsuperuser
### 3. Spuštění projektu
Spuštění lokálního vývojového serveru:

Bash
python manage.py runserver
