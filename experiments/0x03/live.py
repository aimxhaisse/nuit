# █▀ █▀█ █ █▀█
# ▄█ █▄█ █ █▀▄ @ https://soir.dev

@live()
def setup():
    bpm.set(130)

    ctrls.mk_lfo('x1', 0.25, low=0.1, high=0.6)

    tracks.setup({
        'trk-1': tracks.mk_sampler(fxs={})
    })

drumnibus = sampler.new('drumnibus')
oberheim = sampler.new('oberheim')

@loop(track='trk-1', beats=4)
def beat():
    patterns = [
        '........s...............s.......',
        'k.......k.......k.......k.......',
        '....H.......H.......H.......H...',
        '........K...................K...',
    ]

    for i in range(32):
        for p in patterns:
            if p[i] == 'k':
                drumnibus.play(sampler.samples('drumnibus')[0].name)
            if p[i] == 's':
                drumnibus.play(sampler.samples('drumnibus')[30].name)
            if p[i] == 'H':
                drumnibus.play(sampler.samples('drumnibus')[46].name)
            if p[i] == 'K':
                drumnibus.play(sampler.samples('drumnibus')[132].name, start=0.2)
                drumnibus.play(sampler.samples('drumnibus')[132].name, rate=2, start=0.05)
                drumnibus.play(sampler.samples('drumnibus')[132].name, rate=0.5)
        sleep(0.125)
