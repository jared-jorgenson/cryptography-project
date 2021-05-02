import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

# Import ciphers
from ceaser_cipher import ceaser_encrypt, ceaser_decrypt
from atbash_cipher import atbash_encrypt, atbash_decrypt
from substitution_cipher import sub_encrypt, sub_decrypt

Builder.load_file("design.kv")


class MainLayout(TabbedPanel):

    message_ceaser = ObjectProperty(None)
    rotations_ceaser = ObjectProperty(None)
    message_atbash = ObjectProperty(None)
    message_sub = ObjectProperty(None)
    cipher_key_sub = ObjectProperty(None)

    def press_encrypt_ceaser(self):
        message_ceaser = self.message_ceaser.text
        rotations_ceaser = self.rotations_ceaser.text
        # Change the message box to the encryption
        self.message_ceaser.text = ceaser_encrypt(
            str(message_ceaser), int(rotations_ceaser))

    def press_decrypt_ceaser(self):
        message_ceaser = self.message_ceaser.text
        rotations_ceaser = self.rotations_ceaser.text
        # Change the message box to the decryption
        self.message_ceaser.text = ceaser_decrypt(
            str(message_ceaser), int(rotations_ceaser))

    def press_encrypt_atbash(self):
        message_atbash = self.message_atbash.text
        # Change the message box to the encryption
        self.message_atbash.text = atbash_encrypt(str(message_atbash))

    def press_decrypt_atbash(self):
        message_atbash = self.message_atbash.text
        # Change the message box to the decryption
        self.message_atbash.text = atbash_decrypt(str(message_atbash))

    def press_encrypt_substitution(self):
        message_sub = self.message_sub.text
        cipher_key_sub = self.cipher_key_sub.text
        # Change the input boxes with randomly generated key and encryption
        output = sub_encrypt(str(message_sub))
        self.message_sub.text = output[0]
        self.cipher_key_sub.text = output[1]

    def press_decrypt_substitution(self):
        message_sub = self.message_sub.text
        cipher_key_sub = self.cipher_key_sub.text
        # Change the message box to the decryption
        self.message_sub.text = sub_decrypt(
            str(message_sub), str(cipher_key_sub))


class CipherApp(App):

    def build(self):
        return MainLayout()


if __name__ == "__main__":
    CipherApp().run()
