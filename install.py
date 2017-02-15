from music21 import environment
MUSESCORE_PATH = '/usr/bin/musescore'

if __name__ == '__main__':
    environment.set('musicxmlPath', MUSESCORE_PATH)
    environment.set('musescoreDirectPNGPath', MUSESCORE_PATH)
