# 📊 Filtrowanie wyników modeli ML  

### Opis  
Program filtruje wyniki modeli ML na podstawie trzech parametrów:  
- **C** – czas inferencji (musi być mniejszy lub równy, aby usunąć wynik),  
- **P** – zużycie pamięci (musi być mniejsze lub równe),  
- **J** – jakość rozpoznania (musi być większa lub równa).  

Jeśli istnieje inny wynik, który spełnia te warunki, dany rekord zostaje usunięty.  

### 🔧 Uruchomienie  
1. Umieść dane wejściowe w `input.txt` w formacie:  
   ```
   5
   300 2 10
   20 1 2
   4 2 10
   200 1 1
   200 1 11
   ```  
2. Uruchom program:  
   ```bash
   python filter_results.py
   ```  
3. Wynik zostanie zapisany w `output.txt`.  

### 📌 Przykład  
Dla powyższego `input.txt`, wynik to:  
```
3
```  
