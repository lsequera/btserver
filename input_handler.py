"""
Input Handler Module
==================

Handles mouse and keyboard input simulation using X11.
"""

import Xlib.display
import Xlib.X
import Xlib.ext.xtest
import logging
from typing import Tuple

# Set up logging
logger = logging.getLogger(__name__)

class InputHandler:
    """Handles mouse and keyboard input simulation."""
    
    def __init__(self):
        self.display = Xlib.display.Display()
        self.screen = self.display.screen()
        
    def move_mouse(self, dx: int, dy: int) -> None:
        """
        Move the mouse cursor relative to its current position.
        
        Args:
            dx: Horizontal movement in pixels
            dy: Vertical movement in pixels
        """
        root = self.display.screen().root
        current = root.query_pointer()._data
        new_x = current['root_x'] + dx
        new_y = current['root_y'] + dy
        
        Xlib.ext.xtest.fake_input(
            self.display,
            Xlib.X.MotionNotify,
            x=new_x,
            y=new_y
        )
        self.display.sync()
        logger.info(f"Mouse moved to ({new_x}, {new_y})")

    def click_mouse(self, button: int, action: int) -> None:
        """
        Simulate mouse button click.
        
        Args:
            button: Mouse button (1=left, 2=right, 3=middle)
            action: Action (1=down, 0=up)
        """
        if action == 1:  # Button down
            Xlib.ext.xtest.fake_input(
                self.display,
                Xlib.X.ButtonPress,
                button
            )
        else:  # Button up
            Xlib.ext.xtest.fake_input(
                self.display,
                Xlib.X.ButtonRelease,
                button
            )
        self.display.sync()
        logger.info(f"Mouse button {button} {'pressed' if action == 1 else 'released'}")

    def scroll_mouse(self, dx: int, dy: int) -> None:
        """
        Simulate mouse scroll.
        
        Args:
            dx: Horizontal scroll amount
            dy: Vertical scroll amount
        """
        # Convert scroll values to button presses
        if dy > 0:
            for _ in range(abs(dy)):
                Xlib.ext.xtest.fake_input(
                    self.display,
                    Xlib.X.ButtonPress,
                    4  # Scroll up
                )
        elif dy < 0:
            for _ in range(abs(dy)):
                Xlib.ext.xtest.fake_input(
                    self.display,
                    Xlib.X.ButtonPress,
                    5  # Scroll down
                )
                
        if dx > 0:
            for _ in range(abs(dx)):
                Xlib.ext.xtest.fake_input(
                    self.display,
                    Xlib.X.ButtonPress,
                    6  # Scroll right
                )
        elif dx < 0:
            for _ in range(abs(dx)):
                Xlib.ext.xtest.fake_input(
                    self.display,
                    Xlib.X.ButtonPress,
                    7  # Scroll left
                )
        self.display.sync()
        logger.info(f"Mouse scrolled dx={dx}, dy={dy}")

    def press_key(self, keycode: int) -> None:
        """
        Simulate key press.
        
        Args:
            keycode: X11 keycode
        """
        Xlib.ext.xtest.fake_input(
            self.display,
            Xlib.X.KeyPress,
            keycode
        )
        self.display.sync()
        logger.info(f"Key {keycode} pressed")

    def release_key(self, keycode: int) -> None:
        """
        Simulate key release.
        
        Args:
            keycode: X11 keycode
        """
        Xlib.ext.xtest.fake_input(
            self.display,
            Xlib.X.KeyRelease,
            keycode
        )
        self.display.sync()
        logger.info(f"Key {keycode} released")
