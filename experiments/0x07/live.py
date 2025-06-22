# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

system.info()

@live()
def setup():
    bpm.set(120)

    layout = dict()
 
    if False:
        layout['bass'] = tracks.mk_midi(
            midi_out='Moog Minitaur',
            audio_in='Scarlett 18i20 USB',
            audio_chans=[5],
        )

    if True:
        layout['pads'] = tracks.mk_midi(
            midi_out='Elektron Digitone',
            audio_in='Scarlett 18i20 USB',
            audio_chans=[6, 7],
        )

    layout['beats'] = tracks.mk_sampler()

    tracks.setup(layout)


@loop('bass', beats=4)
def bassline():
    with midi.use_chan(1):
        midi.note_on(40)
        sleep(4)
        midi.note_off(40)
        log('ok')


@loop('pads', beats=16)
def digitone():
    with midi.use_chan(1):
        midi.note_on(40)
        sleep(16)
        midi.note_off(40)
