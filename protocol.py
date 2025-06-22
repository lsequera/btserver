"""
Bluetooth Remote Control Protocol
==============================

Simple protocol for handling mouse and keyboard commands over Bluetooth.
Commands are sent as single byte codes followed by optional parameters.

Commands:
    0x01 - Mouse Move (dx, dy)
    0x02 - Mouse Click (button, action)
    0x03 - Mouse Scroll (dx, dy)
    0x10 - Key Press (keycode)
    0x11 - Key Release (keycode)
    0xFF - Protocol Version Request

Parameters:
    dx, dy: 16-bit signed integers (-32768 to 32767)
    button: 8-bit (1=left, 2=right, 3=middle)
    action: 8-bit (1=down, 0=up)
    keycode: 32-bit unsigned integer (X11 keycodes)
"""

import struct
from typing import Tuple, Optional
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Command codes
CMD_MOUSE_MOVE = 0x01
CMD_MOUSE_CLICK = 0x02
CMD_MOUSE_SCROLL = 0x03
CMD_KEY_PRESS = 0x10
CMD_KEY_RELEASE = 0x11
CMD_VERSION = 0xFF

# Protocol version
PROTOCOL_VERSION = 1


class ProtocolError(Exception):
    """Raised when there's an error in protocol handling."""
    pass


class RemoteControlProtocol:
    """Handler for Bluetooth remote control protocol."""
    
    def __init__(self):
        self._current_command = None
        self._remaining_bytes = 0
        self._buffer = bytearray()
        
    def parse(self, data: bytes) -> Optional[Tuple[int, bytes]]:
        """
        Parse incoming data according to the protocol.
        
        Args:
            data: Incoming bytes from the Bluetooth connection
            
        Returns:
            Tuple of (command_code, parameters) if a complete command was parsed,
            None if more data is needed.
            
        Raises:
            ProtocolError: If there's an error in the protocol
        """
        self._buffer.extend(data)
        
        while len(self._buffer) > 0:
            if self._current_command is None:
                # First byte is the command code
                if len(self._buffer) < 1:
                    break
                self._current_command = self._buffer[0]
                self._buffer = self._buffer[1:]
                
                # Determine expected parameter length based on command
                if self._current_command in [CMD_MOUSE_MOVE, CMD_MOUSE_SCROLL]:
                    self._remaining_bytes = 4  # 2 bytes dx + 2 bytes dy
                elif self._current_command == CMD_MOUSE_CLICK:
                    self._remaining_bytes = 2  # 1 byte button + 1 byte action
                elif self._current_command in [CMD_KEY_PRESS, CMD_KEY_RELEASE]:
                    self._remaining_bytes = 4  # 4 bytes keycode
                elif self._current_command == CMD_VERSION:
                    self._remaining_bytes = 0
                else:
                    raise ProtocolError(f"Unknown command: {self._current_command:02X}")
            
            if len(self._buffer) < self._remaining_bytes:
                break
                
            # We have a complete command
            params = self._buffer[:self._remaining_bytes]
            self._buffer = self._buffer[self._remaining_bytes:]
            
            # Reset for next command
            command = self._current_command
            self._current_command = None
            self._remaining_bytes = 0
            
            return command, params
            
        return None

    def encode_version_request(self) -> bytes:
        """Encode a protocol version request."""
        return bytes([CMD_VERSION])

    def encode_mouse_move(self, dx: int, dy: int) -> bytes:
        """Encode a mouse move command."""
        return bytes([CMD_MOUSE_MOVE]) + struct.pack("hh", dx, dy)

    def encode_mouse_click(self, button: int, action: int) -> bytes:
        """Encode a mouse click command."""
        return bytes([CMD_MOUSE_CLICK]) + struct.pack("BB", button, action)

    def encode_mouse_scroll(self, dx: int, dy: int) -> bytes:
        """Encode a mouse scroll command."""
        return bytes([CMD_MOUSE_SCROLL]) + struct.pack("hh", dx, dy)

    def encode_key_press(self, keycode: int) -> bytes:
        """Encode a key press command."""
        return bytes([CMD_KEY_PRESS]) + struct.pack("I", keycode)

    def encode_key_release(self, keycode: int) -> bytes:
        """Encode a key release command."""
        return bytes([CMD_KEY_RELEASE]) + struct.pack("I", keycode)

    def handle_command(self, command: int, params: bytes) -> None:
        """Handle a parsed command."""
        if command == CMD_VERSION:
            logger.info(f"Protocol version request received. Version: {PROTOCOL_VERSION}")
        else:
            logger.info(f"Received command {command:02X} with params: {params.hex()}")
            # TODO: Implement actual command handling using X11 or similar
            
    def reset(self) -> None:
        """Reset the protocol state."""
        self._current_command = None
        self._remaining_bytes = 0
        self._buffer.clear()
