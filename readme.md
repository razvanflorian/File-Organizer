File Organizer

Am creat aceasta aplicatie cu scopul de a organiza si sorta diferite tipuri de fisiere din folder-ul Downloads. Mai exact aplicatia indentifica tipul de fisier in funtie de extensia acestuia, spre ex. ".pdf" , creaza un folder specific acestui tip de fisier, spre ex. "pdf_files", iar la final fisierul este trecut in mod automat in folder-ul corespunzator. In plus am creat o mica interfata pentru o interactiune mai interactiva atunci cand iterez blocul de cod.

Pentru relizarea acesteia am folosit urmatoarele module:
- os
- shutil
- tkinter (simpledialog, messagebox)

Din punct de vedere tehnic aplicatia implica:
- primirea ca input o cale catre un anumit folder(cazul nostru "Downloads"), unde eu vreau sa fac aceasta organizare si contine doua constante: 
  - DIR_NAMES (tipul de fiser)
  - FILE EXTENSION(extensiile corespunzatoare)
  Cu ajutorul acestora, folosind biblioteca os si shutil am creat anumite functii pentru a crea directoarele si pentru a manipula fisiere dupa nevoie. 
  
In final am creat o interfata grafica cu ajutorul tkinter:

  - Fereastra Principală:
      - Codul creează o fereastră principală utilizând Tkinter, cu titlul "Organizator de Fișiere". Aceasta servește ca punct de plecare pentru utilizator
  - Introducerea Căii:
      - Există un câmp de text (Entry) unde utilizatorul poate introduce calea către directorul pe care dorește să-l organizeze. Acest câmp este etichetat corespunzător pentru a ghida utilizatorul
  - Buton pentru Organizare:
      - Un buton etichetat "Organizează Fișiere" permite utilizatorului să inițieze procesul de organizare. Când este apăsat, codul verifică validitatea căii introduse și începe mutarea fișierelor
  - Adăugarea Tipurilor de Directoare
      - Un alt buton, "Adaugă Directoare și Extensii", deschide o fereastră secundară unde utilizatorul poate introduce noi tipuri de directoare (ex. "Imagini", "Video"). Aceste tipuri sunt folosite pentru a organiza fișierele în funcție de extensiile lor.
   - Adăugarea Extensiilor de Fișiere:
      - În aceeași fereastră secundară, utilizatorul poate introduce extensii noi de fișiere, de exemplu ".jpg", ".mp4", etc. Aceste extensii sunt asociate tipurilor de directoare pentru a facilita mutarea fișierelor.
   - Notificări:
      - Pe parcursul procesului, utilizatorul primește notificări prin messagebox-uri. Acestea includ:
           1. Erori (de exemplu, dacă un fișier nu poate fi mutat).
           2. Avertismente (de exemplu, dacă un fișier nu se potrivește cu niciun director).
           3. Mesaje de succes (când fișierele sunt mutate cu succes sau când se adaugă noi tipuri/extensii).
