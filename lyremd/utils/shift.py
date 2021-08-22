from mido import MidiFile

octave_interval = 12
keytable = "z?x?cv?b?n?m" + "a?s?df?g?h?j" + "q?w?er?t?y?u"

def find_best_shift(midi_iter, msg_filter) -> int:
    count_list = [0] * octave_interval
    octave_list = [0] * 11
    for msg in midi_iter:
        if not msg_filter(msg):
            continue
        for i in range(octave_interval):
            note_pitch = (msg.note + i) % octave_interval
            if keytable[note_pitch] != '?':
                count_list[i] += 1
                note_octave = (msg.note + i) // octave_interval
                octave_list[note_octave] +=1
    idx = max(range(len(count_list)), key=count_list.__getitem__)
    idx2 = 0
    count = 0
    i = 0
    while i + 3 <= len(octave_list):
        tmp = sum(octave_list[i:i+3])
        if tmp > count:
            count = tmp
            idx2 = i
        i += 1

    return idx + (4 - idx2) * octave_interval



