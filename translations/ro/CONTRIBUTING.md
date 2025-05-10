<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9f71f15fee9a73ecfcd4fd40efbe3070",
  "translation_date": "2025-05-09T03:44:29+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuții

Acest proiect primește cu plăcere contribuții și sugestii. Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență pentru Contribuitor (CLA) prin care declari că ai dreptul și într-adevăr ne acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Când trimiți un pull request, un bot CLA va determina automat dacă trebuie să furnizezi un CLA și va marca PR-ul corespunzător (de exemplu, verificare de stare, comentariu). Urmează pur și simplu instrucțiunile oferite de bot. Va trebui să faci acest lucru o singură dată pentru toate repo-urile care folosesc CLA-ul nostru.

## Codul de Conduită

Acest proiect a adoptat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Pentru mai multe informații, citește [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) sau contactează [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Atenție la crearea issue-urilor

Te rugăm să nu deschizi issue-uri pe GitHub pentru întrebări generale de suport, deoarece lista GitHub ar trebui folosită pentru cereri de funcționalități și raportări de bug-uri. Astfel putem urmări mai ușor problemele sau erorile reale din cod și menținem discuțiile generale separate de codul efectiv.

## Cum să contribui

### Ghid pentru Pull Requests

Când trimiți un pull request (PR) către depozitul Phi-3 CookBook, te rugăm să urmezi aceste recomandări:

- **Fork-uiește Repository-ul**: Întotdeauna fă fork la repository în contul tău înainte de a face modificările.

- **Pull requests separate (PR)**:
  - Trimite fiecare tip de modificare în propriul pull request. De exemplu, corectările de bug-uri și actualizările documentației trebuie trimise în PR-uri separate.
  - Corecturile de typo-uri și actualizările minore ale documentației pot fi combinate într-un singur PR, acolo unde este potrivit.

- **Rezolvă conflictele de merge**: Dacă pull request-ul tău are conflicte de merge, actualizează ramura locală `main` pentru a reflecta repository-ul principal înainte de a face modificările.

- **Trimiteri pentru traduceri**: Când trimiți un PR de traducere, asigură-te că folderul de traducere include traduceri pentru toate fișierele din folderul original.

### Ghid pentru traduceri

> [!IMPORTANT]
>
> Când traduci text în acest depozit, nu folosi traduceri automate. Voluntariază-te doar pentru limbile în care ești fluent.

Dacă stăpânești o limbă care nu este engleza, poți ajuta la traducerea conținutului. Urmează acești pași pentru a te asigura că contribuțiile tale la traduceri sunt integrate corect:

- **Creează un folder de traducere**: Navighează la folderul secțiunii corespunzătoare și creează un folder pentru limba în care contribui. De exemplu:
  - Pentru secțiunea de introducere: `PhiCookBook/md/01.Introduce/translations/<language_code>/`
  - Pentru secțiunea quick start: `PhiCookBook/md/02.QuickStart/translations/<language_code>/`
  - Continuă acest model pentru celelalte secțiuni (03.Inference, 04.Finetuning, etc.)

- **Actualizează căile relative**: Când traduci, ajustează structura folderelor adăugând `../../` la începutul căilor relative din fișierele markdown pentru ca link-urile să funcționeze corect. De exemplu, schimbă:
  - `(../../imgs/01/phi3aisafety.png)` în `(../../../../imgs/01/phi3aisafety.png)`

- **Organizează traducerile**: Fiecare fișier tradus trebuie plasat în folderul de traducere al secțiunii corespunzătoare. De exemplu, dacă traduci secțiunea de introducere în spaniolă, vei crea:
  - `PhiCookBook/md/01.Introduce/translations/es/`

- **Trimite un PR complet**: Asigură-te că toate fișierele traduse pentru o secțiune sunt incluse într-un singur PR. Nu acceptăm traduceri parțiale pentru o secțiune. Când trimiți un PR de traducere, verifică că folderul de traducere conține traducerile pentru toate fișierele din folderul original.

### Ghid pentru redactare

Pentru a asigura consistență în toate documentele, te rugăm să urmezi aceste recomandări:

- **Formatarea URL-urilor**: Încadrează toate URL-urile în paranteze drepte urmate de paranteze rotunde, fără spații suplimentare în interior sau în jur. De exemplu: `[example](https://www.microsoft.com)`.

- **Link-uri relative**: Folosește `./` pentru link-uri relative către fișiere sau foldere din directorul curent și `../` pentru cele din directorul părinte. De exemplu: `[example](../../path/to/file)` sau `[example](../../../path/to/file)`.

- **Locale fără specificare de țară**: Asigură-te că link-urile tale nu includ locale specifice unei țări. De exemplu, evită `/en-us/` sau `/en/`.

- **Stocarea imaginilor**: Păstrează toate imaginile în folderul `./imgs`.

- **Nume descriptive pentru imagini**: Denumește imaginile descriptiv folosind caractere în engleză, cifre și cratime. De exemplu: `example-image.jpg`.

## Fluxuri de lucru GitHub

Când trimiți un pull request, următoarele fluxuri de lucru vor fi declanșate pentru a valida modificările. Urmează instrucțiunile de mai jos pentru a te asigura că pull request-ul tău trece verificările fluxului de lucru:

- [Check Broken Relative Paths](../..)
- [Check URLs Don't Have Locale](../..)

### Check Broken Relative Paths

Acest flux de lucru verifică dacă toate căile relative din fișierele tale sunt corecte.

1. Pentru a te asigura că link-urile funcționează corect, efectuează următoarele sarcini în VS Code:
    - Plasează cursorul peste orice link din fișierele tale.
    - Apasă **Ctrl + Click** pentru a naviga către link.
    - Dacă dai click pe un link și acesta nu funcționează local, va declanșa fluxul de lucru și nu va funcționa pe GitHub.

1. Pentru a rezolva această problemă, urmează pașii sugerați de VS Code:
    - Tastează `./` sau `../`.
    - VS Code îți va oferi opțiuni pe baza textului tastat.
    - Urmează calea alegând fișierul sau folderul dorit pentru a te asigura că calea este corectă.

După ce ai adăugat calea relativă corectă, salvează și împinge modificările.

### Check URLs Don't Have Locale

Acest flux de lucru verifică că niciun URL web nu conține un locale specific unei țări. Deoarece acest depozit este accesibil global, este important ca URL-urile să nu includă locale de țară.

1. Pentru a verifica că URL-urile tale nu conțin locale de țară, efectuează următoarele:
    - Caută texte precum `/en-us/`, `/en/` sau orice alt locale de limbă în URL-uri.
    - Dacă acestea nu sunt prezente în URL-uri, vei trece verificarea.

1. Pentru a rezolva această problemă:
    - Deschide fișierul indicat de fluxul de lucru.
    - Elimină localele de țară din URL-uri.

După ce elimini localele de țară, salvează și împinge modificările.

### Check Broken Urls

Acest flux de lucru verifică dacă orice URL web din fișierele tale funcționează și returnează codul de stare 200.

1. Pentru a verifica dacă URL-urile funcționează corect:
    - Verifică starea URL-urilor din fișiere.

2. Pentru a remedia URL-urile rupte:
    - Deschide fișierul care conține URL-ul defect.
    - Actualizează URL-ul cu cel corect.

După ce ai corectat URL-urile, salvează și împinge modificările.

> [!NOTE]
>
> Pot exista cazuri în care verificarea URL-urilor eșuează chiar dacă link-ul este accesibil. Acest lucru se poate întâmpla din mai multe motive, inclusiv:
>
> - **Restricții de rețea:** Serverele GitHub Actions pot avea restricții de rețea care blochează accesul la anumite URL-uri.
> - **Probleme de timeout:** URL-urile care răspund lent pot declanșa o eroare de timeout în fluxul de lucru.
> - **Probleme temporare ale serverului:** Uneori, serverele pot fi indisponibile temporar din cauza mentenanței sau problemelor tehnice în timpul validării.

**Declinare a responsabilității**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.