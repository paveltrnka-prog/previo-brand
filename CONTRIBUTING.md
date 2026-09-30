# Jak přispívat

## Workflow

```bash
git clone https://github.com/paveltrnka-prog/previo-brand.git
git checkout -b nazev-zmeny        # nová větev pro každou úpravu
# ... úpravy v previo-brand/ ...
git add -A
git commit -m "popis změny"
git push -u origin nazev-zmeny
gh pr create                       # vytvoří pull request na GitHubu
```

Změny se nemergují přímo do `main` — vždy přes pull request, aby je mohl někdo zkontrolovat.

## Balíček ke stažení (.skill)

Soubor `previo-brand-v3.skill` (ZIP balíček pro instalaci do Claude) se do gitu necommituje — je to build artefakt generovaný ze souborů ve složce `previo-brand/`. Šablony v `templates/` se generují ze `src/` příkazem `python3 previo-brand/build.py` — uprav `src/`, ne `templates/`. Aktuální verze je vždy ke stažení v sekci [Releases](https://github.com/paveltrnka-prog/previo-brand/releases).

Po úpravě zdrojových souborů je potřeba balíček znovu zabalit a nahrát jako nový Release.

## Přístup

Pro pushnutí větve a vytvoření PR potřebuješ být přidaný jako collaborator na repu (GitHub → repo → Settings → Collaborators).
