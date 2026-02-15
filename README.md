# it_sikkerhed_2026f
Dette er et projekt på **Zealand Næstved**. 

## Formål 
- IT-sikkerhed
- Git & GitHub
- VS Code

## Unit-testing i Python med pytest
Følgende skærmbilleder viser resultatet af kørsel med pytest, herunder beståelse, fejlede og skippede tests.

![Test 1](image1.png)

![Test 2](image2.png)

![Test 3](image3.png)

------------------------------------------------------------------
# Password-validering

Jeg vælger password som mit emne.  
Et login-system består af brugernavn + password, og for at sikre systemet mod svage passwords og misbrug, stilles der krav til længde, indhold og struktur.  
Password-validering er en vigtig del af IT-sikkerhed, fordi det er en af de mest almindelige angrebsflader i et system.

---

## Ækvivalensklasser

Regler:
- Password længde 8–20 tegn
- Indeholder mindst ét tal
- Indeholder mindst ét specialtegn

Ækvivalensklasser bruges til at opdele inputs i grupper, hvor systemet forventes at reagere ens.  
Det gør det lettere at teste mange forskellige typer inputs uden at teste alt.

| Eksempel        | Type              | Godkendt |
|-----------------|-------------------|----------|
| Sikkerhed123!   | Gyldig            | Godkendt |
| 1               | For kort          | Ikke godkendt |
| Over25TegnHer…  | For lang          | Ikke godkendt |
| Sikkerhed       | Intet tal         | Ikke godkendt |
| Sikkerhed123    | Intet specialtegn | Ikke godkendt |

Fordele:
- Giver hurtigt overblik over gyldige/ugyldige inputs  
- Reducerer antallet af nødvendige testcases  

Ulemper:
- Kan overse edge cases  
- Kræver korrekt opdeling af klasser  

Security gate: **Build & Test**

---

## Grænseværdier

Regler:
- Password længde 8–20 tegn

Grænseværdier bruges til at teste lige omkring de kritiske grænser, hvor fejl ofte opstår.

| Eksempel | Type                     | Godkendt |
|----------|---------------------------|----------|
| 7 tegn   | Lige under grænsen        | Ikke godkendt |
| 8 tegn   | Lige på grænsen           | Godkendt |
| 20 tegn  | Øvre grænse               | Godkendt |
| 21 tegn  | Lige over grænsen         | Ikke godkendt |

Fordele:
- Finder fejl tæt på kritiske grænser  
- God til input-validering  

Ulemper:
- Tester ikke hele inputområdet  
- Kræver præcis viden om grænserne  

Security gate: **Build & Test**

---

## CRUD(L)

CRUD bruges til at teste hele livscyklussen for password-håndtering i systemet.

| Operation | Testbeskrivelse                 | Forventet resultat |
|-----------|----------------------------------|---------------------|
| Create    | Opret bruger med stærkt password | Success             |
| Read      | Hent password-policy             | Returneres          |
| Update    | Skift password til for svagt     | Afvist              |
| Delete    | Slet bruger                      | Success             |
| List      | List password-krav               | Returneres          |

Fordele:
- Tester hele password-livscyklussen  
- Afslører fejl i backend-logik og datalagring  

Ulemper:
- Kræver database eller mock-miljø  
- Mere tidskrævende end unit tests  

Security gate: **Build & Test + Release**

---

## Cycle Process Test

Flow:
1. Opret bruger med gyldigt password  
2. Login  
3. Skift password  
4. Login igen  
5. Slet bruger  

Cycle tests bruges til at teste hele brugerrejsen og sikre, at systemet fungerer korrekt i praksis.

Formål:
- Sikre at password-krav overholdes i hele processen  
- Validere at systemet reagerer korrekt ved ændringer  

Fordele:
- Tester realistiske brugerflows  
- Fanger fejl i integrationen mellem funktioner  

Ulemper:
- Længere testtid  
- Sværere at isolere fejl  

Security gate: **Release + Operate**

---

## Testpyramiden

Testpyramiden bruges til at strukturere testarbejdet og sikre en god balance mellem hurtige og langsomme tests.

Unit-tests:
- Password-validering (længde, tal, specialtegn)

Integration-tests:
- Login-flow (API + database)

UI-tests:
- Fejlbeskeder i login-formular

Fordele:
- Hurtig eksekvering i bunden  
- God struktur og høj testdækning  
- UI-tests giver overblik over brugeroplevelsen  

Ulemper:
- UI-tests er langsomme  
- Fejl kan være svære at lokalisere  

Security gate: **Build & Test**

---

## Decision Table Test

Decision tables bruges til at få overblik over alle kombinationer af regler og deres resultater.

Krav:
- Brugernavn unikt  
- Password 8–20 tegn  
- Mindst ét tal  
- Mindst ét specialtegn  

| # | Unikt brugernavn | 8–20 tegn | Tal | Specialtegn | Resultat                |
|---|------------------|-----------|-----|-------------|-------------------------|
| 1 | Ja               | Ja        | Ja  | Ja          | Bruger oprettes         |
| 2 | Ja               | Nej       | Ja  | Ja          | Afvist (WeakPassword)   |
| 3 | Ja               | Ja        | Nej | Ja          | Afvist (WeakPassword)   |
| 4 | Ja               | Ja        | Ja  | Nej         | Afvist (WeakPassword)   |
| 5 | Nej              | Ja        | Ja  | Ja          | Afvist (AlreadyExists)  |

Fordele:
- Giver komplet overblik over alle kombinationer  
- Nem at læse og forstå  
- Sikrer at ingen regler overses  

Ulemper:
- Kan blive stor ved mange regler  
- Kræver præcis definition af alle betingelser  

Security gate: **Build & Test**

---

## Security Gates (forklaring)

Security gates er kontrolpunkter i udviklingsprocessen, hvor man stopper op og vurderer kvalitet og sikkerhed, før man går videre.

**Build & Test:**  
- Fokus på validering, unit-tests og inputkontrol  
- Her fanges fejl i password-reglerne tidligt  
- Billigt at rette fejl her  

**Release:**  
- Systemet testes samlet  
- CRUD og cycle tests er relevante  
- Sikrer at funktionalitet og sikkerhed er stabil før deployment  

**Operate:**  
- Systemet kører i drift  
- Fokus på login-flow, brugeradfærd og fejl  
- Overvågning af misbrug, brute-force og fejl  

---
## Testresultater (PyTest)

Jeg har kørt mine automatiske tests med PyTest for at sikre, at password‑valideringen fungerer korrekt.  
Testene blev kørt med kommandoen:

python -m pytest


PyTest fandt i alt 10 tests, hvoraf:

- 6 tests **passed** (mine egne password‑tests)
- 2 tests **skipped** (kommer fra et andet bibliotek og er ikke relevante for projektet)
- 0 tests fejlede

![PyTest](image4.png)

### Hvad betyder resultatet?
At alle mine egne tests passer, viser at:

- password‑valideringen fungerer som forventet  
- alle data‑drevne testcases giver det rigtige resultat  
- funktionens logik er stabil og håndterer både gyldige og ugyldige passwords korrekt  

Det giver en høj grad af sikkerhed for, at password‑reglerne er implementeret korrekt, og at systemet reagerer rigtigt på forskellige typer input.

Security gate: **Build & Test**

---

## Testresultater for min flat_file_db

Jeg har implementeret en flat file‑database i Python, hvor brugerdata gemmes i en JSON‑fil.  
For at sikre at databasen fungerer korrekt, har jeg lavet automatiske unit tests med PyTest.


### Resultat
PyTest fandt i alt 8 tests:

- 2 tests fra min `flat_file_db` (alle **passed**)
- 6 tests fra mit password‑projekt (alle **passed**)

Det betyder, at **alle mine tests kørte uden fejl**, og at både min flat_file_db og mine password‑funktioner fungerer som forventet.

### Hvad viser resultatet?
- Min database kan oprette og hente brugere korrekt  
- Systemet håndterer situationer hvor en bruger ikke findes  
- JSON‑filen bliver oprettet og opdateret som den skal  
- Testene bekræfter, at funktionerne virker stabilt og uden fejl  

### Risiko hvis en test fejler
- Brugere kan blive gemt forkert  
- Systemet kan returnere forkerte data  
- Data kan gå tabt eller blive overskrevet  
- Funktionerne kan opføre sig uforudsigeligt i et større system  

### Screenshot
Her er et screenshot af mine testresultater (krav fra opgaven):

![flat_file_test](<image5.png>) 

# Kryptering, Hashing og Benchmarking

Dette projekt implementerer sikker håndtering af persondata ved hjælp af kryptering, hashing og automatiske tests. Formålet er at opfylde GDPR‑krav og sikre korrekt password‑beskyttelse.

Projektet indeholder:
- Symmetrisk kryptering (Fernet / AES‑128)
- Asymmetrisk kryptering (RSA‑2048 – til benchmarking)
- Hashing af passwords (bcrypt)
- Benchmarking af flere kryptografiske algoritmer
- Automatiske tests med pytest

---

## Algoritmer jeg havde at vælge imellem

### Symmetrisk kryptering
- AES‑128  
- AES‑256  
- Blowfish (128–448 bit)  
- Fernet (AES‑128 + HMAC)

### Asymmetrisk kryptering
- RSA‑2048  
- RSA‑4096  

### Hashing
- SHA‑256  
- SHA‑512  
- SHA3‑256  
- SHA3‑512  
- bcrypt  

---

## Algoritmer jeg valgte og hvorfor

### ✔ Symmetrisk kryptering: Fernet (AES‑128)
Jeg valgte Fernet, fordi den:
- bygger på AES‑128 (sikker og moderne)
- håndterer IV, nøgler og integritet automatisk
- er nem at implementere korrekt
- er velegnet til små systemer og flat‑file databaser

---

### ✔ Asymmetrisk kryptering: RSA‑2048 (kun til benchmarking)
Jeg bruger ikke RSA i selve databasen, men jeg benchmarker den for at vise forskellen mellem symmetrisk og asymmetrisk kryptering.

---

### ✔ Hashing: bcrypt
Jeg valgte bcrypt, fordi:
- den er langsom med vilje (god mod brute‑force)
- den bruger salt automatisk
- den er standard til password‑sikkerhed
- SHA‑algoritmerne er for hurtige til passwords

---

## Hvornår og hvorfor jeg krypterer data

Jeg krypterer persondata **inden de gemmes** i databasen for at:
- beskytte mod datatyveri
- forhindre uautoriseret adgang
- opfylde GDPR’s krav om dataminimering og databeskyttelse

Felter der krypteres:
- fornavn  
- efternavn  
- by  
- email  
- telefon  

---

## Hvornår og hvorfor jeg dekrypterer data

Jeg dekrypterer kun data:
- når brugeren skal vises
- når data skal opdateres

Jeg dekrypterer **aldrig hele databasen på én gang**, kun det felt der skal bruges.  
Dette reducerer risikoen for datalæk og følger GDPR’s princip om dataminimering.

---

## Hvornår og hvorfor jeg fjerner dekrypteret data fra hukommelsen

Dekrypterede værdier fjernes fra hukommelsen så snart de er brugt, fordi:
- GDPR kræver dataminimering
- dekrypterede data er sårbare, hvis programmet crasher
- det reducerer risikoen for memory‑dump angreb
- det sikrer, at følsomme oplysninger ikke ligger frit i RAM

---

## Bør jeg tage hensyn til noget andet?

Ja, følgende sikkerhedspunkter er vigtige:

- Krypteringsnøglen (key.key) skal opbevares sikkert og må ikke uploades til GitHub  
- Passwords må aldrig kunne dekrypteres (kun hashes)  
- Kryptering skal ske før data forlader applikationen  
- Dekryptering skal kun ske i RAM og kun når nødvendigt  
- Logs må ikke indeholde følsomme oplysninger  
- Backup‑filer skal også krypteres  
- Brugere skal have stærke password‑krav  

---

## Benchmarking af algoritmer

Jeg har benchmarked både symmetriske, asymmetriske og hashing‑algoritmer for at måle CPU‑tid og RAM‑forbrug.

### Resultater

| Algoritme | CPU‑tid | RAM | Kommentar |
|----------|---------|------|-----------|
| **Fernet (AES‑128)** | ~6.98 ms | ~14 KB | Sikker, nem, inkluderer integritet |
| **AES‑128 (rå)** | ~0.22 ms | ~2.7 KB | Meget hurtig, men kræver manuel håndtering |
| **RSA‑2048** | ~2.72 ms | ~11 KB | Langsom, bruges kun til små datamængder |
| **bcrypt** | ~327 ms | ~0.09 KB | Langsom med vilje, perfekt til passwords |
| **SHA‑256** | ~0.058 ms | ~0.03 KB | Meget hurtig, ikke egnet til passwords |

### Konklusion på benchmarking
- Symmetrisk kryptering (AES/Fernet) er hurtigst  
- Asymmetrisk kryptering (RSA) er tungest  
- bcrypt er langsommere end SHA‑256 (som forventet)  
- bcrypt er det sikre valg til passwords  
- Fernet er det bedste valg til persondata  

![benchmark_resultater](<image7.png>)
---

## Test af kryptering og hashing

Jeg har lavet automatiske tests med pytest, som sikrer:
- at kryptering og dekryptering virker korrekt
- at hashing og password‑validering fungerer
- at data ikke ændres under kryptering/dekryptering

Alle tests passer.

![Test af kryptering og hashing](<image6.png>)
---

## Samlet konklusion

Jeg har implementeret en sikker løsning, der opfylder kravene i opgaven:

- Persondata krypteres med en moderne og sikker algoritme (Fernet/AES‑128)  
- Passwords hashes med bcrypt  
- Data dekrypteres kun når nødvendigt  
- Dekrypterede data fjernes hurtigt fra hukommelsen  
- Jeg har benchmarked flere algoritmer og valgt de mest sikre og praktiske  
- Jeg har testet alle funktioner automatisk med pytest  

Systemet lever dermed op til både **GDPR**, **sikkerhedsstandarder** og **opgavens krav**.
