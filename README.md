# git-commit-bot
Skrypt nie wymaga dodatkowych bibliotek Pythona, poza tymi domyślnie zainstalowanymi. Program automatycznie tworzy nowe pliki w:
```
['c', 'cpp', 'csharp', 'go', 'java', 'js', 'php', 'python', 'r', 'swift']
```
Zawierające podstawowe sformułowanie *"Hello world!"*, zapisane w każdym z tych języków. Następnie zapisuje je w odpowiednich folderach, 
a efekt swojej pracy umieszcza we wskazanym w *git init* repozytorium na gałęzi master. Moc skryptu w fazie testów wyniosła 2347 commitów na godzinę.
