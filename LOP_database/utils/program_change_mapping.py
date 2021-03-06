#!/usr/bin/env python
# -*- coding: utf8 -*-

# program_change_mapping = {
#     'piano': 1,
#     'bright acoustic piano': 2,
#     'electric grand piano': 3,
#     'honky-tonk piano': 4,
#     'electric piano 1': 5,
#     'electric piano 2': 6,
#     'harpsichord': 7,
#     'clavi': 8,
#     'celesta': 9,
#     'glockenspiel': 10,
#     'music box': 11,
#     'vibraphone': 12,
#     'marimba': 13,
#     'xylophone': 14,
#     'tubular bells': 15,
#     'dulcimer': 16,
#     'drawbar organ': 17,
#     'percussive organ': 18,
#     'rock organ': 19,
#     'church organ': 20,
#     'reed organ': 21,
#     'accordion': 22,
#     'harmonica': 23,
#     'tango accordion': 24,
#     'acoustic guitar (nylon)': 25,
#     'acoustic guitar (steel)': 26,
#     'electric guitar (jazz)': 27,
#     'electric guitar (clean)': 28,
#     'electric guitar (muted)': 29,
#     'overdriven guitar': 30,
#     'distortion guitar': 31,
#     'guitar harmonics': 32,
#     'acoustic bass': 33,
#     'electric bass (finger)': 34,
#     'electric bass (pick)': 35,
#     'fretless bass': 36,
#     'slap bass 1': 37,
#     'slap bass 2': 38,
#     'synth bass 1': 39,
#     'synth bass 2': 40,
#     'violin': 41,
#     'viola': 42,
#     'cello': 43,
#     'contrabass': 44,
#     'tremolo strings': 45,
#     'pizzicato strings': 46,
#     'orchestral harp': 47,
#     'timpani': 48,
#     'string ensemble 1': 49,
#     'string ensemble 2': 50,
#     'synthstrings 1': 51,
#     'synthstrings 2': 52,
#     'choir aahs': 53,
#     'voice oohs': 54,
#     'synth voice': 55,
#     'orchestra hit': 56,
#     'trumpet': 57,
#     'trombone': 58,
#     'tuba': 59,
#     'muted trumpet': 60,
#     'horn': 61,
#     'brass section': 62,
#     'synthbrass 1': 63,
#     'synthbrass 2': 64,
#     'soprano sax': 65,
#     'alto sax': 66,
#     'tenor sax': 67,
#     'baritone sax': 68,
#     'oboe': 69,
#     'english horn': 70,
#     'bassoon': 71,
#     'clarinet': 72,
#     'piccolo': 73,
#     'flute': 74,
#     'recorder': 75,
#     'pan flute': 76,
#     'blown bottle': 77,
#     'shakuhachi': 78,
#     'whistle': 79,
#     'ocarina': 80,
#     'lead 1 (square)': 81,
#     'lead 2 (sawtooth)': 82,
#     'lead 3 (calliope)': 83,
#     'lead 4 (chiff)': 84,
#     'lead 5 (charang)': 85,
#     'lead 6 (voice)': 86,
#     'lead 7 (fifths)': 87,
#     'lead 8 (bass + lead)': 88,
#     'pad 1 (new age)': 89,
#     'pad 2 (warm)': 90,
#     'pad 3 (polysynth)': 91,
#     'pad 4 (choir)': 92,
#     'pad 5 (bowed)': 93,
#     'pad 6 (metallic)': 94,
#     'pad 7 (halo)': 95,
#     'pad 8 (sweep)': 96,
#     'fx 1 (rain)': 97,
#     'fx 2 (soundtrack)': 98,
#     'fx 3 (crystal)': 99,
#     'fx 4 (atmosphere)': 100,
#     'fx 5 (brightness)': 101,
#     'fx 6 (goblins)': 102,
#     'fx 7 (echoes)': 103,
#     'fx 8 (sci-fi)': 104,
#     'sitar': 105,
#     'banjo': 106,
#     'shamisen': 107,
#     'koto': 108,
#     'kalimba': 109,
#     'bag pipe': 110,
#     'fiddle': 111,
#     'shanai': 112,
#     'tinkle bell': 113,
#     'agogo': 114,
#     'steel drums': 115,
#     'woodblock': 116,
#     'taiko drum': 117,
#     'melodic tom': 118,
#     'synth drum': 119,
#     'reverse cymbal': 120,
#     'guitar fret noise': 121,
#     'breath noise': 122,
#     'seashore': 123,
#     'bird tweet': 124,
#     'telephone ring': 125,
#     'helicopter': 126,
#     'applause': 127,
#     'gunshot': 128,
#     #####
#     'percussion': 48,
#     'double bass': 44,
#     'bassoon bass': 71,
#     'clarinet bass': 72,
#     'trombone alto': 58,
#     'trombone bass': 58,
#     'violoncello': 43,
#     'harp': 47,
#     'cornet': 57,
#     'euphonium': 59,
#     'tam tam': 118,
#     'triangle': 81,
#     'voice': 54,
#     'voice alto': 54,
#     'voice tenor': 54,
#     'voice soprano': 54,
#     'voice bass': 54,
#     'cymbal': 120,
#     'saxophone soprano': 64,
#     'saxophone alto': 65,
#     'saxophone tenor': 66,
#     'saxophone baryton': 67,
#     'castanet': 30,
#     'drum': 40,
# }


program_change_mapping = {
    "Piccolo": 73,
    "Flute": 74,
    "Alto-Flute": 74,
    "Soprano-Flute": 74,
    "Bass-Flute": 74,
    "Contrabass-Flute": 74,
    "Pan Flute": 76,
    "Recorder": 74,
    "Ocarina": 80,
    "Oboe": 69,
    "Oboe-dAmore": 69,
    "Oboe de Caccia": 69,
    "English-Horn": 70,
    "Heckelphone": 0,
    "Piccolo-Clarinet-Ab": 72,
    "Clarinet": 72,
    "Clarinet-Eb": 72,
    "Clarinet-Bb": 72,
    "Piccolo-Clarinet-D": 72,
    "Clarinet-C": 72,
    "Clarinet-A": 72,
    "Basset-Horn-F": 61,
    "Alto-Clarinet-Eb": 72,
    "Bass-Clarinet-Bb": 72,
    "Bass-Clarinet-A": 72,
    "Contra-Alto-Clarinet-Eb": 72,
    "Contrabass-Clarinet-Bb": 72,
    "Bassoon": 71,
    "Contrabassoon": 71,
    "Soprano-Sax": 65,
    "Alto-Sax": 66,
    "Tenor-Sax": 67,
    "Baritone-Sax": 68,
    "Bass-Sax": 68,
    "Contrabass-Sax": 68,
    "Horn": 61,
    "Harmonica": 23,
    "Piccolo-Trumpet-Bb": 57,
    "Piccolo-Trumpet-A": 57,
    "High-Trumpet-F": 57,
    "High-Trumpet-Eb": 57,
    "High-Trumpet-D": 57,
    "Cornet": 57,
    "Trumpet": 57,
    "Trumpet-C": 57,
    "Trumpet-Bb": 57,
    "Cornet-Bb": 57,
    "Alto-Trumpet-F": 57,
    "Bass-Trumpet-Eb": 57,
    "Bass-Trumpet-C": 57,
    "Bass-Trumpet-Bb": 57,
    "Clarion": 57,
    "Trombone": 58,
    "Alto-Trombone": 58,
    "Soprano-Trombone": 58,
    "Tenor-Trombone": 58,
    "Bass-Trombone": 58,
    "Contrabass-Trombone": 58,
    "Euphonium": 59,
    "Tuba": 59,
    "Bass-Tuba": 59,
    "Contrabass-Tuba": 59,
    "Flugelhorn": 0,
    "Piano": 1,
    "Celesta": 9,
    "Organ": 20,
    "Harpsichord": 7,
    "Accordion": 22,
    "Bandoneone": 22,
    "Harp": 47,
    "Guitar": 25,
    "Bandurria": 25,
    "Mandolin": 25,
    "Lute": 25,
    "Lyre": 25,
    "Violin": 41,
    "Violins": 41,
    "Viola": 42,
    "Violas": 42,
    "Viola de gamba": 42,
    "Viola de braccio": 42,
    "Violoncello": 43,
    "Violoncellos": 43,
    "Contrabass": 44,
    "Basso continuo": 44,
    "Bass drum": 35,
    "Glockenspiel": 10,
    "Xylophone": 14,
    "Vibraphone": 12,
    "Marimba": 13,
    "Maracas": 70,
    "Bass-Marimba": 13,
    "Tubular-Bells": 15,
    "Clave": 75,
    "Bombo": 0,
    "Hi-hat": 42,
    "Triangle": 81,
    "Ratchet": 0,
    "Drum": 0,
    "Snare drum": 38,
    "Steel drum": 115,
    "Tambourine": 54,
    "Tam tam": 54,
    "Timpani": 48,
    "Cymbal": 49,
    "Castanets": 0,
    "Percussion": 0,
    "Voice": 54,
    "Voice soprano": 54,
    "Voice mezzo": 54,
    "Voice alto": 54,
    "Voice contratenor": 54,
    "Voice tenor": 54,
    "Voice baritone": 54,
    "Voice bass": 54,
    "Ondes martenot": 0,
    "Unknown": 0,
}
