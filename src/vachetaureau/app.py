
from os.path import dirname, join
import random
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
from android.media import AudioManager, SoundPool


class VacheTaureauApp(toga.App):
    def startup(self):
        """Configure l'interface utilisateur et initialise l'application."""
        self.secret = str(random.randint(1000, 9999))
        self.attempts = 0
        self.max_attempts = 10
        self.current_guess = ""

        # Initialisation des sons
        try:
            self.soundpool = SoundPool(1, AudioManager.STREAM_MUSIC, 0)
            self.success_sound = self.soundpool.load(join(dirname(__file__), "resources", "son_reussite.mp3"), 1)
            self.failure_sound = self.soundpool.load(join(dirname(__file__), "resources", "son_echec.mp3"), 1)

        except Exception as e:
            self.soundpool = None
            print(f"Erreur lors de l'initialisation des sons : {e}")



        # Image du cadenas
        image_path = join(dirname(__file__), "resources", "cadenas.png")
        try:
            cadenas_image = toga.Image(image_path)
        except FileNotFoundError:
            cadenas_image = None

        image_widget = toga.ImageView(cadenas_image, style=Pack(width=150, height=150)) if cadenas_image else toga.Label(
            "Image cadenas introuvable"
        )

        # Zone d'affichage du code saisi
        self.display = toga.Label("", style=Pack(font_size=20, text_align=CENTER, padding=10))

        # Boutons numériques (0-9) sur deux lignes
        button_box_row1 = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding_top=5))
        button_box_row2 = toga.Box(style=Pack(direction=ROW, alignment=CENTER, padding_top=5))
        for i in range(10):
            button = toga.Button(
                str(i), on_press=lambda widget, val=i: self._add_digit(val),  # Associer chaque bouton à sa valeur
                style=Pack(width=50, height=50, padding=5)
            )
            if i < 5:
                button_box_row1.add(button)
            else:
                button_box_row2.add(button)

        # Boutons Vérifier et Rejouer
        check_button = toga.Button("Vérifier", on_press=self._check_guess, style=Pack(padding=5))
        reset_button = toga.Button("Rejouer", on_press=lambda x: self._reset_game(), style=Pack(padding=5))

        control_box = toga.Box(children=[check_button, reset_button], style=Pack(direction=ROW, alignment=CENTER, padding=5))

        # Résultats avec une zone de défilement
        self.result_scroll_container = toga.ScrollContainer(style=Pack(height=200, padding_top=10))
        self.result_box = toga.Box(style=Pack(direction=COLUMN))
        self.result_scroll_container.content = self.result_box

        # Layout principal
        main_box = toga.Box(
            children=[image_widget, self.display, button_box_row1, button_box_row2, self.result_scroll_container, control_box],
            style=Pack(direction=COLUMN, alignment=CENTER, padding=20),
        )

        # Configuration de la fenêtre principale
        self.main_window = toga.MainWindow(title="Jeu Vache-Taureau")
        self.main_window.content = main_box
        self.main_window.show()

    def _add_digit(self, digit):
        """Ajoute un chiffre au code actuel (jusqu'à 4 chiffres)."""
        if len(self.current_guess) < 4:
            self.current_guess += str(digit)  # Ajoute directement la valeur du chiffre
            self.display.text = self.current_guess  # Met à jour l'affichage

    def _reset_game(self):
        """Réinitialise le jeu avec un nouveau nombre secret."""
        self.secret = str(random.randint(1000, 9999))
        self.attempts = 0
        self.current_guess = ""
        self.display.text = ""

        # Remplacer le conteneur des résultats par un nouveau
        new_result_box = toga.Box(style=Pack(direction=COLUMN))
        self.result_scroll_container.content = new_result_box
        self.result_box = new_result_box

        # Message de confirmation
        self.main_window.info_dialog("Nouvelle Partie", "Un nouveau code secret a été généré. Bonne chance !")

    def _check_guess(self, widget):
        """Vérifie l'entrée utilisateur et met à jour les résultats."""
        if len(self.current_guess) != 4 or not self.current_guess.isdigit():
            self.main_window.error_dialog("Erreur", "Veuillez entrer un code à 4 chiffres.")
            return

        self.attempts += 1
        taureaux, vaches = self._calculate_score(self.current_guess)
        self.result_box.add(
            toga.Label(f"Essai {self.attempts}: {self.current_guess} → {taureaux} taureau(x), {vaches} vache(s)")
        )

        if self.current_guess == self.secret:
            if self.soundpool:
                self.soundpool.play(self.success_sound, 1, 1, 0, 0, 1)  # Jouer le son de succès
            self.main_window.info_dialog("Félicitations", f"Bravo ! Le code secret était {self.secret}.")
            self._reset_game()
        elif self.attempts >= self.max_attempts:
            if self.soundpool:
                self.soundpool.play(self.failure_sound, 1, 1, 0, 0, 1)  # Jouer le son d'échec
            self.main_window.info_dialog("Dommage", f"Désolé, vous avez dépassé les 10 essais. Le code secret était {self.secret}.")
            self._reset_game()
        else:
            self.current_guess = ""
            self.display.text = ""

    def _calculate_score(self, guess):
        """Calcule le nombre de taureaux et de vaches."""
        taureaux, vaches = 0, 0
        secret_temp = list(self.secret)
        guess_temp = list(guess)

        # Calcul des taureaux
        for i in range(4):
            if guess_temp[i] == secret_temp[i]:
                taureaux += 1
                secret_temp[i] = guess_temp[i] = None

        # Calcul des vaches
        for i in range(4):
            if guess_temp[i] is not None and guess_temp[i] in secret_temp:
                vaches += 1
                secret_temp[secret_temp.index(guess_temp[i])] = None

        return taureaux, vaches


def main():
    return VacheTaureauApp()
