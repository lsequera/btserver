"""
Input Handler Module
==================

Handles mouse and keyboard input simulation using evdev and uinput.
"""

from evdev import UInput, ecodes
import logging
from typing import Tuple

# Set up logging
logger = logging.getLogger(__name__)

class InputHandler:
    """Handles mouse and keyboard input simulation."""
    
    def __init__(self):
        # Create a virtual input device
        self.ui = UInput(
            name='virtual-mouse',
            events={
                ecodes.EV_REL: [ecodes.REL_X, ecodes.REL_Y],
                ecodes.EV_KEY: [
                    ecodes.BTN_LEFT,
                    ecodes.BTN_RIGHT,
                    ecodes.BTN_MIDDLE,
                    ecodes.BTN_4,
                    ecodes.BTN_5,
                    ecodes.BTN_6,
                    ecodes.BTN_7
                ]
            }
        )
        
    def move_mouse(self, dx: int, dy: int) -> None:
        """
        Move the mouse cursor relative to its current position.
        
        Args:
            dx: Horizontal movement in pixels
            dy: Vertical movement in pixels
        """
        self.ui.write(ecodes.EV_REL, ecodes.REL_X, dx)
        self.ui.write(ecodes.EV_REL, ecodes.REL_Y, dy)
        self.ui.syn()
        logger.info(f"Mouse moved by ({dx}, {dy}) pixels")

    def click_mouse(self, button: int, action: int) -> None:
        """
        Simulate mouse button click.
        
        Args:
            button: Mouse button (1=left, 2=right, 3=middle)
            action: Action (1=down, 0=up)
        """
        # Map button numbers to evdev button codes
        button_map = {
            1: ecodes.BTN_LEFT,
            2: ecodes.BTN_RIGHT,
            3: ecodes.BTN_MIDDLE,
        }
        
        if button in button_map:
            self.ui.write(ecodes.EV_KEY, button_map[button], action)
            self.ui.syn()
            logger.info(f"Mouse button {button} {'pressed' if action == 1 else 'released'}")
        else:
            logger.warning(f"Unsupported mouse button: {button}")

    def scroll_mouse(self, dx: int, dy: int) -> None:
        """
        Simulate mouse scroll.
        
        Args:
            dx: Horizontal scroll amount
            dy: Vertical scroll amount
        """
        # Map scroll values to button presses
        if dy > 0:
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_4, 1)  # Scroll up
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_4, 0)
        elif dy < 0:
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_5, 1)  # Scroll down
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_5, 0)
                
        if dx > 0:
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_6, 1)  # Scroll right
            self.ui.write(ecodes.EV_KEY, ecodes.BTN_6, 0)
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
