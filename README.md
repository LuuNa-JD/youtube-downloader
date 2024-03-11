# YouTube Downloader

YouTube Downloader est un outil simple écrit en Python pour télécharger une liste de vidéos depuis YouTube. Il permet aux utilisateurs de sauvegarder leurs vidéos préférées en format video/audio maximal sur leur appareil local rapidement et facilement.

## Fonctionnalités

- Téléchargement de vidéos à partir d'URL YouTube.
- Sélection automatique de la qualité video (format maximal supporté par la video en question.
- Interface en ligne de commande simple et intuitive.

## Prérequis

Avant de commencer, assurez-vous d'avoir les prérequis suivants installés sur votre système :

- Python 3.8 ou supérieur
- ffmpeg

## Installation

### Installer Python et pip

Assurez-vous d'avoir Python et pip installés sur votre système. Vous pouvez télécharger Python depuis [le site officiel de Python](https://www.python.org/downloads/). L'installation de Python devrait également installer `pip` automatiquement.

### Installer ffmpeg

`ffmpeg` est nécessaire pour le traitement des fichiers médias. Suivez les instructions spécifiques à votre système d'exploitation pour installer `ffmpeg` :

- **Windows :** [Instructions d'installation ffmpeg pour Windows](https://ffmpeg.org/download.html#build-windows)
- **MacOS :** Vous pouvez installer `ffmpeg` en utilisant [Homebrew](https://brew.sh/) avec la commande `brew install ffmpeg`.
- **Linux :** La plupart des distributions Linux peuvent installer `ffmpeg` via le gestionnaire de paquets. Par exemple, sur Ubuntu, vous pouvez utiliser `sudo apt install ffmpeg`.

### Installer les dépendances Python

Après avoir cloné le dépôt et vous être assuré que `ffmpeg` est installé, installez la dépendance Python nécessaire en exécutant :

```bash
cd chemin_vers_youtube-downloader
pip install pytube
