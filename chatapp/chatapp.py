"""Welcome to Reflex!."""

from chatapp import styles

# Import all the pages.
from chatapp.pages import *

import reflex as rx

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
