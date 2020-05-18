# embedded-music-player

Using the standard audio output of the RPi, please build the music player.
The local buttons and LEDs should be used to switch on/off the player, to
select the song and to control volume. The web interface should be used to
cofigure the list songs, to download and to remove the song.

The subject of the assignment 4 is the implementation with the emulated Vexpress
A9 board a device equipped with two forms of user interface:
1. simple buttons and LEDs should be used to control basic functions;
2. web interface (or other network interface) should be used to control
advanced functions;
3. The design should include support for additional equipment connected to
the board. In the simplest version it can be a built-in audio output. In a
better version it can be an external USB audio card or other device.
Please remember that QEMU allows you to share USB devices with the
emulated board.
