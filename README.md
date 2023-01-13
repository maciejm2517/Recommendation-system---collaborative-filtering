<h1> System rekomendacji produktów za pomocą collaborative filtering</h1>
<h2>Opis rzeczywistego problemu</h2>
Temat projektu odnosi się do dziedziny sztucznej inteligencji zajmującej się rekomendacją. Celem jest rekomendaja przedmiotów zgodnie z preferencjami użytkownika. Preferencje uzyskuję się przez interakcję użytkownika z aplikacją i zbieraniem związanym z tym meta danych. Przykładem są strony internetowe polecające artykuły które kupiły również inne osoby lub artykuły które są można kupić na podstawie ich cech wspólnych z innymi artykułami.

<h2>State of art</h2>
Do rozwiązania problemu rekomendacji mogą posłużyć metody rekomendacji oparte na dobieraniu produktów które są popularne - jest to jednak najprostsza metoda rekomendacji, która może być stosowana głównie do nowych użytkowników.

Do rekomendacji produków zgodne z wcześniejszymi wyborami użytkownika wykorzystuje się algorytmy content based. Algorytmy te są dobre do rekomendacji podobnych produktów, które przedtem wybrał użytkownik (opierają się na dobieraniu artykułów o podobnych cechach co wcześniejsze).

Inną formą rekomendacji są metody które rekomendują produkty zgodnie z preferencjami innych użytkowników - collaborative filtering. Używamy ich do rekomendacji przez dopasowanie danych testowych do modelu zapisanego na podstawie preferencji innych użytkowników - macierz interakcji user-item. Macierz tą możemy użyć do rekomendacji item-item (rekomendacja jest na podstawie przedmiotów, które inni użytkownicy wysoko ocenili) lub do rekomendacji user-user (rekomendacja jest na podstawie podobnych użytkowników do nas, a polecanymi przedmiotami są np. te które mają najwyższą średnią ocen wśród tych użytkowników. 

Można wyróżnić również algorytmy hybrydowe, które łączą collaborative filtering z content based filtering oraz algorytmy, które do rekomendacji korzystają z sieci neuronowych (np. ograniczona maszyna Boltzmanna). 

<h2>Opis wybranej koncepcji</h2>
Projekt polega na rekomendacji anime/filmów za pomocą metody collaborative filtering. Rekomendowane zostają pozycje na podstawie opinii innych użytkowników. Datasety zostały pobranane ze stron: https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database?datasetId=571 oraz https://www.kaggle.com/datasets/dev0914sharma/dataset?select=Dataset.csv
Dane o użytkowniku końcowym są zbierane na podstawie interakcji w aplikacji. System rekomendacji jest wbudowany w aplikację GUI napisaną w przez w module Tkinter.

Efektem działania aplikacji ma być dopasowanie najbardziej odpowiednich artykułów na podstawie metadanych użytkownika - każda interakcja z produktem aktualizuje jak bardzo użytkownik jest zainsteresowany danym produktem przez co rekomendacja może zostać lepiej dopasowana.

Metadane użytkownika są pogrupowane na podstawie odpowiednich wag (wyszukanie -  ocena 3, polubienie - ocena 4, kupno - ocena 5). Są to spekulacje jakie użytkownik wystawiłby danym produkcjom. Przyrównanie takie zawiera założenie że można uznać pozytywną recenzje danego przedmiotu jako efekt uprzedniego zainteresowania przedmiotem oraz negatywną recenzję jako brak zainteresowania (co jest pewnym uproszczeniem).

Dane  innych użytkowników są pozyskiwane przez scalanie danych z plików .csv. Danymi są oceny użytkowników o danej pozycji (rating.csv,ratings.csv) oraz baza filmów/anime (movies.csv, anime.csv). Następnie zostaje utworzona macierz user-item przez utworzenie tabeli przestawnej ze zgromadzonych danych.

Oceny obliczane na podsatawie wag są przyrównywane do macierzy item-item.
Macierz ta jest obliczana na postawie podobieństwa cosinusowego (ang. cosine similarity) 

$$\frac{\sum_{i=1}^{n}A_iB_i}{\sqrt{\sum_{i=1}^{n}A^2_i}\sqrt{\sum_{i=1}^{n}B^2_i}}$$

Rekomendacja polega na wybraniu odpowiednich produktów które są zapisane jako prawdopodobieństwo w wierszszu macierzy podobieństw.

Rekomendacja ta jest uproszczonym modelem na którego podstawie działają różne serwisy VOD lub sklepy internetowe rekomendujące produkty na podstawie ocen innych użytkowników oraz interakcji użytkownika z produktami. Do rzeczywistego rozwiązania problemu najlepiej skorzystać z hybrydowego systemu rekomendacji w którym jednocześnie można rekomendować ulubione cechy przedmiotów jak i prawdopodobieństwo wyboru przez innych użytkowników. Do testowania takiego rozwiązania można wykorzystać bota który będzie sprawdzał zarekomendowane produkty z inną, zewnętrzną bazą danych o produktacji i użytkownikach. 

Do testowania tego modelu można wykorzystać wiedzę o podobnych tytułach jakie rekomenduje model.  Np. jeśli dla datasetu o anime klikniemy oraz zaznaczymy "buy" dla pozycji "Dragon Ball" wtedy model rekomenduje nam inne anime które w nazwie również mają Dragon Ball. Innym przykładem jest zaznaczenie "Harry Potter and the Chamber of Secrets (2002)" oraz otrzymane rekomendacje które również są o Harrym Potterze. 
Model rekomenduje również na pierwszej pozycji tę samą pozycję co wybrał użytkownik - nie jest to błąd, bo pokazuje że to anime jest najbardziej odpowiednie do użytkownika. 

<h2>Proof of concept</h2>
**Uwagi do projektu**
<ol>
<li> Do rekomendacji anime potrzebny jest plik anime.csv oraz macierz item-item w formacie .pickle. Do pobrania są z dysku Google: https://drive.google.com/drive/folders/1Jp9tDUmJmDT9_qDLc8Qkiq-s67GRY0v7?usp=sharing Można również przetestować system rekomendacji na danych filmach - wtedy system rekomendacji jest tworzony w trakcie działa aplikacji.</li>
<li> Wybieranie produktów z listy często buguje się: pierwszym wyborem są  rekomendacje do pierwszego alfabetycznie tytułu - błąd tkintera z obsługą tak dużej ilości tekstu w module Listbox. Dlatego przed pierwszym wyszukaniem najlepiej użyć przycisku "Clear preferences"</li>
<li> Dataset o ocenach anime jest bardzo duży - ok. 100MB dla pliku .csv oraz ok. 200MB dla macierzy item-item która została skompresowana za pomocą modułu pickle. Dlatego obliczanie oraz wczytywanie macierzy nie jest robione bezpośrednio w aplikacji, a w jupiter notebooku new_notebook.ipynb</li>
</ol>
