<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "90d0d072cf26ccc1f271a580d3e45d70",
  "translation_date": "2025-07-16T14:45:47+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "ro"
}
-->
# Contribuții

Acest proiect primește cu plăcere contribuții și sugestii. Majoritatea contribuțiilor necesită să fii de acord cu un Acord de Licență pentru Contribuitori (CLA) prin care declari că ai dreptul și efectiv ne acorzi drepturile de a folosi contribuția ta. Pentru detalii, vizitează [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

Când trimiți un pull request, un bot CLA va determina automat dacă trebuie să furnizezi un CLA și va marca PR-ul corespunzător (de exemplu, verificare de status, comentariu). Urmează pur și simplu instrucțiunile oferite de bot. Va trebui să faci acest lucru o singură dată pentru toate repo-urile care folosesc CLA-ul nostru.

## Codul de conduită

Acest proiect a adoptat [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).  
Pentru mai multe informații, citește [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) sau contactează [opencode@microsoft.com](mailto:opencode@microsoft.com) pentru întrebări sau comentarii suplimentare.

## Atenție la crearea problemelor (issues)

Te rugăm să nu deschizi probleme pe GitHub pentru întrebări generale de suport, deoarece lista GitHub ar trebui folosită pentru cereri de funcționalități și rapoarte de erori. Astfel putem urmări mai ușor problemele reale sau bug-urile din cod și păstrăm discuțiile generale separate de codul efectiv.

## Cum să contribui

### Ghid pentru Pull Requests

Când trimiți un pull request (PR) către depozitul Phi-3 CookBook, te rugăm să urmezi următoarele recomandări:

- **Fork-uiește depozitul**: Întotdeauna fă fork la depozit în contul tău înainte de a face modificările.

- **Pull requests separate (PR)**:
  - Trimite fiecare tip de modificare într-un pull request separat. De exemplu, corecturi de erori și actualizări de documentație trebuie trimise în PR-uri diferite.
  - Corecturile de greșeli de tipar și actualizările minore de documentație pot fi combinate într-un singur PR, dacă este cazul.

- **Rezolvă conflictele de îmbinare**: Dacă PR-ul tău arată conflicte de îmbinare, actualizează ramura locală `main` pentru a reflecta depozitul principal înainte de a face modificările.

- **Trimiteri de traduceri**: Când trimiți un PR cu traduceri, asigură-te că folderul de traduceri include traduceri pentru toate fișierele din folderul original.

### Ghid pentru redactare

Pentru a asigura consistența în toate documentele, te rugăm să urmezi următoarele recomandări:

- **Formatarea URL-urilor**: Înconjoară toate URL-urile cu paranteze drepte urmate de paranteze rotunde, fără spații suplimentare în interior sau în jur. De exemplu: `[exemplu](https://www.microsoft.com)`.

- **Link-uri relative**: Folosește `./` pentru link-uri relative către fișiere sau foldere din directorul curent și `../` pentru cele din directorul părinte. De exemplu: `[exemplu](../../cale/catre/fișier)` sau `[exemplu](../../../cale/catre/fișier)`.

- **Locale fără specificare de țară**: Asigură-te că link-urile tale nu includ locale specifice unei țări. De exemplu, evită `/en-us/` sau `/en/`.

- **Stocarea imaginilor**: Păstrează toate imaginile în folderul `./imgs`.

- **Nume descriptive pentru imagini**: Denumește imaginile descriptiv folosind caractere englezești, cifre și cratime. De exemplu: `exemplu-imagine.jpg`.

## Fluxuri de lucru GitHub

Când trimiți un pull request, următoarele fluxuri de lucru vor fi declanșate pentru a valida modificările. Urmează instrucțiunile de mai jos pentru a te asigura că PR-ul tău trece verificările:

- [Verifică căile relative rupte](../..)  
- [Verifică că URL-urile nu au locale](../..)

### Verifică căile relative rupte

Acest flux de lucru se asigură că toate căile relative din fișierele tale sunt corecte.

1. Pentru a verifica dacă link-urile funcționează corect, efectuează următoarele în VS Code:
    - Plasează cursorul peste orice link din fișiere.
    - Apasă **Ctrl + Click** pentru a naviga către link.
    - Dacă dai click pe un link și nu funcționează local, va declanșa fluxul de lucru și nu va funcționa pe GitHub.

1. Pentru a remedia această problemă, urmează pașii de mai jos folosind sugestiile de cale oferite de VS Code:
    - Tastează `./` sau `../`.
    - VS Code îți va oferi opțiuni bazate pe ce ai tastat.
    - Urmează calea făcând click pe fișierul sau folderul dorit pentru a te asigura că calea este corectă.

După ce ai adăugat calea relativă corectă, salvează și împinge modificările.

### Verifică că URL-urile nu au locale

Acest flux de lucru se asigură că niciun URL web nu conține un locale specific unei țări. Deoarece acest depozit este accesibil global, este important să te asiguri că URL-urile nu conțin localele țării tale.

1. Pentru a verifica că URL-urile tale nu au locale de țară, efectuează următoarele:
    - Verifică dacă există texte precum `/en-us/`, `/en/` sau orice alt locale de limbă în URL-uri.
    - Dacă acestea nu sunt prezente, vei trece această verificare.

1. Pentru a remedia această problemă, urmează pașii:
    - Deschide fișierul indicat de fluxul de lucru.
    - Elimină localele de țară din URL-uri.

După ce elimini localele de țară, salvează și împinge modificările.

### Verifică URL-urile rupte

Acest flux de lucru se asigură că orice URL web din fișierele tale funcționează și returnează codul de stare 200.

1. Pentru a verifica dacă URL-urile funcționează corect, efectuează următoarele:
    - Verifică statusul URL-urilor din fișiere.

2. Pentru a remedia URL-urile rupte, efectuează următoarele:
    - Deschide fișierul care conține URL-ul rupt.
    - Actualizează URL-ul cu cel corect.

După ce ai corectat URL-urile, salvează și împinge modificările.

> [!NOTE]  
>  
> Pot exista cazuri în care verificarea URL-urilor eșuează chiar dacă linkul este accesibil. Acest lucru se poate întâmpla din mai multe motive, inclusiv:  
>  
> - **Restricții de rețea:** Serverele GitHub Actions pot avea restricții de rețea care împiedică accesul la anumite URL-uri.  
> - **Probleme de timeout:** URL-urile care răspund prea lent pot declanșa o eroare de timeout în fluxul de lucru.  
> - **Probleme temporare ale serverului:** Perioadele ocazionale de nefuncționare sau mentenanță pot face un URL temporar inaccesibil în timpul validării.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.