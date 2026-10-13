# Zelda3 — fork pour Z3-Launcher

Ce dépôt est un fork de [snesrev/zelda3](https://github.com/snesrev/zelda3), une réimplémentation en C de **The Legend of Zelda: A Link to the Past**.

**Ce fork a pour seul but de fournir les exécutables et les outils de ressources utilisés par [Z3-Launcher](https://github.com/legluondunet/Z3-Launcher).** Il permet au launcher de télécharger le jeu déjà compilé et de préparer ses ressources sans imposer une compilation à l'utilisateur.

L'utilisation avec Z3-Launcher est recommandée. Le programme reste utilisable directement : un tutoriel est fourni ci-dessous.

Aucune ROM ni ressource extraite du jeu n'est incluse dans les téléchargements. Pour jouer, vous devez fournir votre propre ROM américaine et en extraire les ressources.

## Différences avec le projet d'origine

| Ajout ou modification dans ce fork | Objectif |
|---|---|
| Workflow GitHub Actions | Compiler automatiquement les exécutables Linux et Windows en x86_64 et fabriquer une AppImage Linux. |
| Publication de paquets ZIP dans les Releases | Fournir des téléchargements directement utilisables par Z3-Launcher. |
| Bibliothèques nécessaires incluses | Fournir les DLL Windows et embarquer SDL2 dans l'AppImage. |
| Extracteur autonome dans `extractor/` | Générer les ressources sans installer séparément Python, Pillow ou PyYAML. |
| Script `tools/extract-assets.py` | Préparer un répertoire de travail et appeler l'outil de ressources du projet d'origine ; proposer également une vérification de la langue de la ROM. |
| Script `tools/package-release.py` | Créer des ZIP avec des chemins relatifs et conserver les permissions Unix des exécutables. |
| Correction dans `assets/tables.py` | Éviter un avertissement Python lié aux séquences d'échappement. |
| Version du fork et informations de compilation | Identifier chaque publication par sa version et son commit ; fournir `VERSION`, `BUILD-INFO.txt` et `SHA256SUMS`. |
| Licence des nouveaux fichiers | Utiliser GPL-3.0-or-later pour les ajouts de legluondunet, en conservant les licences et crédits du code d'origine. |

Le moteur de jeu et ses fonctionnalités — écran large, shaders, mode 7 amélioré, audio MSU-1 et options de gameplay — proviennent du projet d'origine. Ils ne sont pas présentés comme des ajouts de ce fork.

## Version et téléchargements

La version actuelle du fork est **0.1.0**, définie dans [VERSION](VERSION). Elle est indépendante de la version de Z3-Launcher.

Les publications portent un nom comme `Zelda3 0.1.0 (abcdef0)` et un tag comme `v0.1.0-abcdef0`. Le commit identifie exactement les sources utilisées pour la compilation.

Téléchargements : [Releases](https://github.com/legluondunet/zelda3/releases).

| Système | Paquet public |
|---|---|
| Linux x86_64 | `zelda3-linux-x86_64.zip`, contenant `zelda3.AppImage` et l'extracteur autonome. |
| Windows x86_64 | `zelda3-windows-x86_64.zip`, contenant `zelda3.exe`, les DLL et l'extracteur autonome. |

Le workflow fournit aussi un exécutable Linux classique dans ses [artifacts GitHub Actions](https://github.com/legluondunet/zelda3/actions), sous le nom `zelda3-linux-x86_64`. Cette version nécessite SDL2 installé sur le système.

## Utilisation sans Z3-Launcher

### 1. Télécharger et décompresser

Depuis les Releases, téléchargez le ZIP correspondant à votre système. Décompressez **tout son contenu** dans un répertoire où vous avez le droit d'écrire.

Conservez le dossier `extractor/` complet, notamment son sous-dossier `_internal/`. L'extracteur en dépend pour fonctionner.

Préparez votre ROM américaine de **A Link to the Past**. Dans les exemples, elle se nomme `zelda3.sfc` ; adaptez son chemin à votre installation.

### 2. Générer les ressources sous Linux

Ouvrez un terminal dans le répertoire décompressé et exécutez :

```bash
chmod +x ./extractor/zelda3-extractor ./zelda3.AppImage

./extractor/zelda3-extractor \
  --workspace "$PWD/resources" \
  --extract-from-rom \
  --rom "/chemin/vers/zelda3.sfc"

cp ./resources/zelda3_assets.dat ./zelda3_assets.dat
```

Le chemin de la ROM doit être absolu : l'outil change de répertoire pendant l'extraction. Les guillemets permettent de gérer les espaces dans les chemins.

Une fois `zelda3_assets.dat` créé et copié à côté de l'AppImage, lancez :

```bash
./zelda3.AppImage
```

Si votre système affiche une erreur liée à FUSE, essayez :

```bash
./zelda3.AppImage --appimage-extract-and-run
```

Avec l'exécutable Linux classique téléchargé depuis les artifacts, placez également `zelda3_assets.dat` et `zelda3.ini` dans son répertoire, installez SDL2 avec le gestionnaire de paquets de votre distribution, puis lancez `./zelda3` depuis ce répertoire.

### 3. Générer les ressources sous Windows

Ouvrez **PowerShell** dans le répertoire décompressé et exécutez :

```powershell
.\extractor\zelda3-extractor.exe --workspace "$PWD\resources" --extract-from-rom --rom "C:\chemin\vers\zelda3.sfc"

Copy-Item .\resources\zelda3_assets.dat .\zelda3_assets.dat

.\zelda3.exe
```

Adaptez le chemin absolu de la ROM. Gardez les DLL fournies à côté de `zelda3.exe`.

Après cette préparation, vous pouvez aussi lancer le jeu en double-cliquant sur `zelda3.exe`.

### 4. Configurer et jouer

Le fichier `zelda3.ini` permet de modifier les contrôles, le rendu, le plein écran, l'audio et les options de jeu. Fermez le jeu avant de modifier ce fichier.

Les touches par défaut correspondent à un clavier QWERTY :

| Action | Touche |
|---|---|
| Déplacements | Flèches |
| Start | Entrée |
| Select | Maj droite |
| Boutons A / B / X / Y | X / Z / S / A |
| Boutons L / R | C / V |
| Plein écran | Alt + Entrée |
| Pause | P |
| Sauvegarder un état | Maj + F1 à F10 |
| Charger un état | F1 à F10 |

Pour un clavier AZERTY, utilisez la ligne `Controls` prévue à cet effet dans la section `[KeyMap]` de `zelda3.ini`, en désactivant l'autre ligne `Controls`.

Pour les shaders `.glsl` ou `.glslp`, définissez `OutputMethod = OpenGL` et renseignez leur chemin dans `Shader`, dans la section `[Graphics]`.

Le programme a besoin de `zelda3_assets.dat` à chaque lancement. La ROM n'est plus nécessaire pour jouer une fois les ressources générées. Les données de jeu et la configuration doivent rester dans un répertoire accessible en écriture ; avec l'AppImage, elles sont utilisées dans le répertoire de l'AppImage.

### En cas de problème

- **Ressources introuvables** : vérifiez que `zelda3_assets.dat` se trouve à côté de l'exécutable ou de l'AppImage. Avec l'exécutable classique, lancez le jeu depuis ce répertoire.
- **Extraction impossible** : vérifiez le chemin absolu de la ROM, sa compatibilité avec la version américaine attendue et la présence du dossier `extractor/_internal/`.
- **Permission refusée sous Linux** : vérifiez les permissions d'exécution et les droits d'écriture du répertoire.
- **DLL manquante sous Windows** : décompressez de nouveau le ZIP complet et conservez les DLL fournies avec le jeu.

## Sources et crédits

Le travail de réimplémentation du jeu appartient au projet [snesrev/zelda3](https://github.com/snesrev/zelda3). Il utilise notamment les implémentations PPU et DSP de [LakeSnes](https://github.com/elzo-d/LakeSnes), ainsi que des travaux de documentation et de désassemblage cités par le projet d'origine.

Les sources et les instructions de compilation restent disponibles dans ce dépôt, notamment dans [BUILDING.md](BUILDING.md). Les ajouts de ce fork concernent principalement la compilation automatique, la distribution et l'intégration avec Z3-Launcher.

## Licences

- **Fork dans son ensemble et nouveaux fichiers originaux de legluondunet** : GNU GPL version 3 ou ultérieure, identifiant `GPL-3.0-or-later`. Copyright © 2026 legluondunet. Voir [LICENSE.txt](LICENSE.txt) pour le périmètre et [COPYING](COPYING) pour le texte complet.
- **Fichiers hérités du projet d'origine** : leurs licences et auteurs sont conservés, y compris lorsqu'ils sont modifiés dans ce fork. La licence MIT et les mentions de **snesrev** et **elzo_d** sont préservées dans [LICENSE.upstream.txt](LICENSE.upstream.txt).
- **Opus et autres composants tiers** : ils conservent leurs propres licences et mentions de copyright. Voir notamment [la licence d'Opus](third_party/opus-1.3.1-stripped/COPYING) et les notices présentes dans les fichiers de `third_party/`. Les bibliothèques embarquées dans les paquets restent régies par leurs licences respectives.
- **ROM et ressources extraites du jeu** : elles ne sont pas couvertes par les licences du code de ce dépôt et ne sont pas distribuées avec les paquets.
