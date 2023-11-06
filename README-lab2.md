# Documentație Proiect Django - Sistem de Autentificare și Autorizare

## Cuprins

- [Introducere](#introducere)
- [Implementarea Autentificării](#implementarea-autentificării)
- [Actualizări Șablon de Autentificare](#actualizări-șablon-de-autentificare)
- [Personalizarea Vizualizării de Autentificare](#personalizarea-vizualizării-de-autentificare)
- [Gestionarea Erorilor](#gestionarea-erorilor)
- [Redirecționare la Înregistrare](#redirecționare-la-înregistrare)
- [Procedura de Testare](#procedura-de-testare)

## Introducere

Acest document servește ca ghid pentru implementarea sistemului de autentificare și autorizare în proiectul TO-DO creat anterior in Django. Include pașii pentru configurarea autentificării personalizate a utilizatorului și redirecționării după acțiuni de login și logout.

## Implementarea Autentificării

Am creat un formular de autentificare personalizat extinzând `AuthenticationForm` din Django. Câmpurile de utilizator și parolă au fost stilizate utilizând widget-uri personalizate.

## Actualizări Șablon de Autentificare

Șablonul `login.html` a fost actualizat pentru a include tokenul CSRF, care este esențial pentru protecția împotriva atacurilor de tip CSRF. Formularul este redat într-un format prietenos utilizând `{{ form.as_p }}`.

## Personalizarea Vizualizării de Autentificare

Am definit o clasă `CustomLoginView` care extinde `LoginView` standard din Django. Am specificat un șablon personalizat și am configurat o URL de redirecționare succes către pagina index folosind `reverse_lazy`.

## Gestionarea Erorilor

Am rezolvat o problemă comună cu redirecționarea incorectă după login prin setarea `LOGIN_REDIRECT_URL` în fișierul `settings.py`. A fost de asemenea verificată și corectată funcționalitatea de bază a vizualizării pentru a evita erorile de tip `AttributeError`.

## Redirecționare la Înregistrare

Am inclus în șablonul de login un link care permite utilizatorilor să navigheze către pagina de înregistrare, în cazul în care aceștia nu dețin deja un cont.

## Procedura de Testare

Au fost efectuate teste pentru a asigura că redirecționarea după login si logout funcționează corect și că utilizatorii sunt redirecționați către pagina index după autentificare. De asemena, am testat redirectionarile in cazul autentificarii reusite si esuate.

---

## Intrebari de Control
1. Ce reprezintă `Service Layer` în arhitectura Model-View-Controller (MVC) a aplicațiilor web și ce rol au ele în separarea logicii?

`Service Layer` este un concept în arhitectura Model-View-Controller (MVC) care se referă la o stratificare logică a aplicației ce gestionează regulile de afaceri și operațiile. Acesta acționează ca un intermediar între straturile de prezentare (View) și de acces la date (Model), ajutând la separarea și centralizarea logicii de afaceri a aplicației.

2. Explicați conceptele de autentificare și autorizare în dezvoltarea web. 

Autentificarea este procesul prin care se verifică identitatea unui utilizator, adesea prin solicitarea de credențiale precum nume de utilizator și parolă. Autorizarea, pe de altă parte, este procesul de a determina dacă un utilizator autentificat are permisiunea de a accesa o resursă sau de a efectua o anumită acțiune.

3. Cum se poate implementa autentificarea utilizatorilor și restricționarea accesului la anumite rute sau acțiuni înDjango?

Autentificarea utilizatorilor se poate implementa folosind mecanisme precum sesiuni, tokeni sau standarde de autentificare, cum ar fi OAuth. Framework-urile moderne oferă module și middleware-uri care facilitează implementarea acestor procese și permit restricționarea accesului la rute sau acțiuni specifice bazate pe statutul de autentificare al utilizatorului.

4. Care este diferența dintre testarea unitară (`Unit Tests`) și testarea de integrare (`Integration Tests`)?

Testele unitare sunt teste izolate care verifică comportamentul unei componente sau funcții specifice în mod individual. Testele de integrare, în schimb, sunt concepute pentru a testa interacțiunile și fluxurile de lucru între diferite module sau servicii pentru a verifica că sistemul funcționează corect ca un întreg.
