# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(120)

    layout = dict()

    layout['bass'] = tracks.mk_midi(
        midi_out='Moog Minitaur',
        audio_in='Scarlett 18i20 USB',
        audio_chans=[5,6],
    )

    layout['beats'] = tracks.mk_sampler()

    tracks.setup(layout)


@loop('bass', beats=16)
def bassline():
    with midi.use_chan(1):
        for i in range(16):
            midi.note_on(40 + i)
            sleep(1)
            midi.note_off(40 + i)
