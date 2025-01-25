# Jeu Vache-Taureau

Bienvenue dans le **Jeu Vache-Taureau** développé par **Studio KATEB & Papa** avec le framework [BeeWare](https://beeware.org/) ! Ce projet propose une version interactive et amusante du jeu classique, disponible sur Android grâce à BeeWare.

---

## Description du jeu

Le **Jeu Vache-Taureau** est un jeu de logique où le joueur doit deviner un code secret à 4 chiffres. À chaque essai :

- Un **taureau (🐂)** signifie qu'un chiffre est correct et bien placé.
- Une **vache (🐄)** signifie qu'un chiffre est correct mais mal placé.

Le but est de trouver le code secret en un maximum de 10 essais.

---

## Fonctionnalités

- Interface utilisateur avec champs de saisie alignés.
- Historique des essais dynamique et défilant.
- Sons de réussite et d'échec pour une meilleure immersion.
- Support d'images, comme un cadenas représentant le code secret.
- Bouton **Rejouer** pour recommencer une partie.

---

## Installation

### Prérequis
- Python 3.8+
- Le framework BeeWare
- Un appareil Android ou un émulateur pour tester l'application

### Étapes

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/kattouba/VacheTaureau
   cd vache-taureau
   ```

2. Installez les dépendances avec BeeWare :
   ```bash
   briefcase dev
   ```

3. Placez les fichiers suivants dans le répertoire `resources` :
   - `son_reussite.mp3`
   - `son_echec.mp3`
   - `son_vache.mp3`
   - `cadenas.png`

4. Lancez l'application en mode développement :
   ```bash
   briefcase run android
   ```

---

## Utilisation

1. Entrez un code de 4 chiffres dans les champs de saisie.
2. Appuyez sur **Vérifier** pour soumettre votre essai.
3. Consultez l'historique des essais pour voir vos taureaux et vaches.
4. Continuez jusqu'à trouver le code ou atteindre la limite des 10 essais.
5. Appuyez sur **Rejouer** pour une nouvelle partie.

---

## Structure du projet

```
├── app.py               # Fichier principal de l'application
├── resources/           # Répertoire des ressources
│   ├── cadenas.png      # Image utilisée pour l'interface
│   ├── son_reussite.mp3 # Son joué lors de la victoire
│   ├── son_echec.mp3    # Son joué en cas d'échec
│   └── vache.mp3    # Son joué lorsqu'une vache est trouvée
└── README.md            # Ce fichier
```

---

## Améliorations futures

- Ajouter une option multijoueur.
- Support de niveaux de difficulté (codes plus longs).
- Interface plus personnalisée avec des thèmes.

---

## Contributions

Les contributions sont les bienvenues ! Pour signaler un problème ou proposer une amélioration, ouvrez une issue ou soumettez une pull request.

---

## Auteurs

Développé avec ❤️ par **Studio KATEB & Papa**.

- **Site web** : [https://studiokatebetpapa.rf.gd/?i=1](https://studiokatebetpapa.rf.gd/?i=1)
- **Dépôt GitHub** : [https://github.com/kattouba/VacheTaureau](https://github.com/kattouba/VacheTaureau)
- **Page de contact** : [https://studiokatebetpapa.rf.gd/contact/](https://studiokatebetpapa.rf.gd/contact/)

---

## Licence

Ce projet est sous licence GNU v2. Vous êtes libre de l'utiliser et de le modifier selon vos besoins.
